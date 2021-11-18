from sklearn.pipeline import Pipeline  # type: ignore

import tgboost.processing.smiles_manager as sm
from tgboost.config.core import config

trans_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "Database processing",
            sm.SmilesWrapper(
                variables=[
                    config.model_config.smiles_to_extract,
                    config.model_config.target,
                ],
                param_scaler=config.model_config.scaler,
            ),
        ),
        (
            "Embedding step",
            sm.SmilesEmbedder(
                variables=[
                    config.model_config.smiles_to_embed,
                    config.model_config.target,
                ]
            ),
        ),
    ]
)
