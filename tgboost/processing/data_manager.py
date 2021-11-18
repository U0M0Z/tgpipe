import typing as t

import joblib  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore

from tgboost import __version__ as _version
from tgboost.config.core import TRAINED_MODEL_DIR, config


def save_pipeline(*, pipeline_to_persist: Pipeline, specifics: str) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    embedding_model = f"{config.app_config.embedding_word2vec_model}.pkl"

    if specifics == "transformer":
        save_file_name = (
            f"{config.app_config.transformer_pipeline_save_file}{_version}.pkl"
        )
        other_model_name = (
            f"{config.app_config.regressor_pipeline_save_file}{_version}.pkl"
        )
    elif specifics == "regressor":
        save_file_name = (
            f"{config.app_config.regressor_pipeline_save_file}{_version}.pkl"
        )
        other_model_name = (
            f"{config.app_config.transformer_pipeline_save_file}{_version}.pkl"
        )

    safe_files = [other_model_name, embedding_model, save_file_name]
    # safe_files = [other_model_name, save_file_name]

    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=safe_files)
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
