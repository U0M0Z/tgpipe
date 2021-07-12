import pytest

from tg_regression_model.config.core import DATASET_DIR, config
from tg_regression_model.processing.smiles_manager import DatabaseExtractor


@pytest.fixture()
def sample_input_data():
    return DatabaseExtractor().extract(
        file=str(DATASET_DIR) + "/" + config.app_config.test_data_file
    )
