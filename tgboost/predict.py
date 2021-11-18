import typing as t

import numpy as np
import pandas as pd  # type: ignore

from tgboost import __version__ as _version
from tgboost.config.core import config
from tgboost.processing.data_manager import load_pipeline
from tgboost.processing.smiles_manager import SmilesEmbedder, SmilesWrapper
from tgboost.processing.validation import validate_inputs

trans_file_name = f"{config.app_config.transformer_pipeline_save_file}{_version}.pkl"
reg_file_name = f"{config.app_config.regressor_pipeline_save_file}{_version}.pkl"
_xgbRegression_pipe = load_pipeline(file_name=reg_file_name)

print(reg_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model pipeline."""

    transformer = SmilesWrapper(
        variables=[config.model_config.smiles_to_extract],
        param_scaler=config.model_config.scaler,
    )

    embedder = SmilesEmbedder(variables=[config.model_config.smiles_to_embed])

    df_input = pd.DataFrame(input_data)

    transformation = transformer.fit_transform(df_input)
    df_embedded = embedder.fit_transform(transformation)

    # df_embedded = embedder.fit_transform(transformer.fit_transform(df_input))

    validated_data, errors = validate_inputs(input_data=df_embedded)
    results = {"predictions": None, "version": _version, "errors": errors}

    tt_pred = validated_data[config.model_config.embedding_list].values.flatten()
    tt_pred = np.array(list(tt_pred))

    if not errors:
        predictions = _xgbRegression_pipe.predict(X=tt_pred)
        print(predictions)

        results = {
            "predictions": list(predictions),  # type: ignore
            "version": _version,
            "errors": errors,
        }

    return results
