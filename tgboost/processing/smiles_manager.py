from typing import List

import numpy as np
import pandas as pd  # type: ignore
from gensim.models import word2vec  # type: ignore
from mol2vec import features as m2v  # type: ignore
from rdkit import Chem  # type: ignore
from rdkit.Chem import PandasTools  # type: ignore
from sklearn.base import BaseEstimator, TransformerMixin  # type: ignore

from tgboost.config.core import TRAINED_MODEL_DIR, config


class DatabaseExtractor:
    """
    Class for file and database extraction
    """

    def __init__(self):
        pass

    def extract(self, file, smiles=None, target=None, translator=False):
        extension = file.split("/")[-1]
        extension = extension.split(".")[1]

        if extension == "xlsx":
            frame = pd.read_excel(file)
        elif (extension == "csv") or (extension == "txt"):
            frame = pd.read_csv(file)
        elif extension == "pkl":
            frame = pd.read_pickle(file)
        elif extension == "sdf":
            frame = PandasTools.LoadSDF(
                file, smilesName=smiles, molColName=None, includeFingerprints=False
            )
            self.target_param = target

            if translator:
                frame[target] = frame[target].apply(lambda x: self.get_target_param(x))

        if len(frame.columns) == 1:
            frame.columns = [[config.model_config.smiles_to_embed]]

        # print(frame.head())

        return frame

    def get_target_param(self, cell):

        text = cell.strip().split()
        mp_mean = []

        for val in text:
            try:
                val = float(val)
            except Exception:
                try:
                    val = float(val[1:])
                except Exception:
                    continue
            mp_mean.append(val)

        if len(text) == 0:
            print(text)

        mp = np.array(mp_mean)
        mp = mp.mean()

        return mp


class CanonSmilesList(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X: pd.Series, y: pd.Series = None) -> pd.Series:
        return self

    def transform(self, X: pd.Series) -> pd.Series:

        X = X.copy()
        X_canon = []
        error_smiles = []

        for smile in X.tolist():
            try:
                canon_smile = self.get_canon_smiles(smile)
                X_canon.append(canon_smile)
            except Exception:
                error_smiles.append(smile)

        return pd.Series(X_canon), error_smiles

    def get_canon_smiles(self, smi):
        try:
            m = Chem.MolFromSmiles(smi)
            canon_smi = Chem.MolToSmiles(m, isomericSmiles=True, canonical=True)
        except Exception:
            print("SMILE not convertable:", smi)
            canon_smi = np.nan

        return canon_smi


class SmilesWrapper(BaseEstimator, TransformerMixin):
    """
    Main class that transforms the SMILES in input df into
    canonical SMILES representations and drops the unreadable
    ones
    """

    def __init__(self, variables: List[str], param_scaler: bool):
        self.variables = variables
        self.param_scaler = param_scaler

        if not isinstance(variables, list):
            raise ValueError(
                "Must be initialized with df vars list (i.e. SMILES & property names)"
            )

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        smiles = self.variables[0]

        X_ref = X.copy()
        X = X.copy()

        try:
            canon_list = list(
                X[smiles].squeeze().apply(lambda smi: self.get_canon_smiles(smi))
            )
        except Exception:
            canon_list = list(X[smiles].apply(lambda smi: self.get_canon_smiles(smi)))

        if len(X.columns) > 1:
            # *** actions for preparing df with SMILES list and target param
            # create canon SMILES column
            X[smiles] = canon_list

            # remove double SMILES and get average values of target param
            X = X.groupby(by=smiles).mean().reset_index()

            # scale Temp param to Kelvin
            if self.param_scaler is True:
                target_property = self.variables[1]
                X[target_property] = X[target_property] + 273.15

            # create a list of not convertable SMILES and their location
            idx_bad_smiles = X[X[smiles].isnull()].index.tolist()
            self.idx_bad_smiles = idx_bad_smiles
            self.bad_smiles = X_ref[smiles].iloc[idx_bad_smiles].tolist()

            # Prepare cleaned dataset
            X.dropna(subset=self.variables, inplace=True)
            X = X[self.variables]

        else:
            # *** actions for prediction on single SMILES lists
            # set unique values of the SMILES
            unique_canon = list(set(canon_list))

            # remove eventual NaN values from the prediction list
            unique_canon = [
                x for x in unique_canon if pd.isnull(x) is False and x != "nan"
            ]

            # transform into a df and set the columns title
            X = pd.DataFrame(unique_canon)
            X.columns = [[config.model_config.smiles_to_extract]]

        return X

    def get_canon_smiles(self, smi):
        try:
            m = Chem.MolFromSmiles(smi)
            canon_smi = Chem.MolToSmiles(m, isomericSmiles=True, canonical=True)
        except Exception:
            canon_smi = np.nan

        return canon_smi


class SmilesEmbedder(BaseEstimator, TransformerMixin):
    """
    Embedder that transforms SMILES into molecular embeddings
    It takes a df and it returns a df with SMILES and embeddings
    """

    def __init__(self, variables: List[str]):
        self.variables = variables

        if not isinstance(variables, list):
            raise ValueError(
                "Must be init. with target df vars list (i.e. SMILES & property names)"
            )

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        smiles = self.variables[0]

        X = X.copy()

        # Squeeze df into list
        try:
            aa_smis = X[smiles].squeeze().tolist()
        except Exception:
            aa_smis = X[smiles].values.flatten().tolist()

        # Get Mol2vec sentences from RDKit Morgan fingerprints of SMILES
        aas = [Chem.MolFromSmiles(x) for x in aa_smis]
        aa_sentences = [m2v.MolSentence(m2v.mol2alt_sentence(x, 1)) for x in aas]

        #   *** SPECIFY which trained mol2vec model to use for molecular embeddings
        #   Embed RDKit molecules
        model = word2vec.Word2Vec.load(str(TRAINED_MODEL_DIR) + "/model_300dim.pkl")
        embedding = [
            m2v.DfVec(x) for x in m2v.sentences2vec(aa_sentences, model, unseen="UNK")
        ]
        vec = [x.vec for x in embedding]
        embeddings_list = [np.array(x) for x in vec]

        X["embeddings"] = embeddings_list

        return X


class EmbeddingTransformer(BaseEstimator, TransformerMixin):
    """
    Class to transform the embedding column into a numpy array
    with single np.array for embedded vectors
    """

    def __init__(self, variables: List[str]):
        self.variables = variables

        if not isinstance(variables, list):
            raise ValueError("Must be init. with embeddings column name")

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):

        X = X.copy()
        X = X[self.variables].values
        X = np.array(list(X))

        return X
