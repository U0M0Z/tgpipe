from pathlib import Path
from typing import List

from pydantic import BaseModel
from strictyaml import YAML, load  # type: ignore

import tgboost

# Project Directories
PACKAGE_ROOT = Path(tgboost.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    training_data_file: str
    test_data_file: str

    pipeline_name: str
    regressor_pipeline_save_file: str
    transformer_pipeline_save_file: str
    embedding_word2vec_model: str


class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    target: str
    features: List[str]
    target_param_to_extract: str
    smiles_to_extract: str
    translator_activation: bool
    scaler: bool
    smiles_to_embed: str
    embedding_list: str
    test_size: float

    random_state: int

    base_score: float
    booster: str
    colsample_bylevel: int
    colsample_bynode: int
    colsample_bytree: float
    gamma: int
    gpu_id: int
    importance_type: str
    learning_rate: float
    max_delta_step: int
    max_depth: int
    min_child_weight: float
    monotone_constraints: str
    n_estimators: int
    n_jobs: int
    num_parallel_tree: int
    objective: str
    reg_alpha: int
    reg_lambda: int
    scale_pos_weight: int
    subsample: int
    tree_method: str
    validate_parameters: int


class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    """Locate the configuration file."""
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()
