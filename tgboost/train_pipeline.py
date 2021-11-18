from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split  # type: ignore

import tgboost.processing.smiles_manager as sm
from tgboost.config.core import DATASET_DIR, config
from tgboost.processing.data_manager import save_pipeline
from tgboost.regressor import regressor_pipe
from tgboost.transformer import trans_pipe

# sys.path.insert(2, '/Users/tommaso/Desktop/tgboost')


def run_training() -> None:
    """Train the model."""

    dataset_to_use = str(Path(f"{DATASET_DIR}/{config.app_config.training_data_file}"))
    print("DATASET: ", dataset_to_use, "\n")

    # Extracting the database and training data
    print("*** EXTRACTION step")
    my_extractor = sm.DatabaseExtractor()
    data = my_extractor.extract(
        dataset_to_use,
        config.model_config.smiles_to_extract,
        config.model_config.target,
        config.model_config.translator_activation,
    )
    print("n_input SMILES: ", len(data[config.model_config.smiles_to_extract]), "\n")

    print("*** TRANSFORMING step")
    df_smiles = trans_pipe.fit_transform(data)

    print(
        "n_output SMILES: ", len(df_smiles[config.model_config.smiles_to_extract]), "\n"
    )

    df_smiles.to_pickle("SMILES_used_for_training.pkl")

    Xtrain = df_smiles[config.model_config.embedding_list].values
    ytrain = df_smiles[config.model_config.target].values

    print("~~ DATA info \n")
    n_samples = df_smiles[config.model_config.embedding_list].values.shape[0]

    if n_samples <= 1000:
        Xtrain = Xtrain
        ytrain = ytrain
        Xtest = 0
        ytest = 0

        print(
            "Xtrain: ",
            Xtrain.shape[0],
            "ytrain: ",
            ytrain.shape[0],
            "Xtest: ",
            Xtest,
            "ytest: ",
            ytest,
        )
    else:
        Xtrain, ytrain, Xtest, ytest = train_test_split(
            Xtrain,
            ytrain,
            test_size=config.model_config.test_size,
            random_state=config.model_config.test_size,
        )

        print("Xtrain: ", Xtrain.shape[0], "ytrain: ", ytrain.shape[0])

    Xtrain = np.array(list(Xtrain))

    print("*** REGRESSION step\n")
    regressor_pipe.fit(Xtrain, ytrain)

    print("~ _ ~ ^ ~ _ ~ PIPELINE completed: trained model")

    # persist trained model
    save_pipeline(pipeline_to_persist=trans_pipe, specifics="transformer")
    save_pipeline(pipeline_to_persist=regressor_pipe, specifics="regressor")


if __name__ == "__main__":
    run_training()
