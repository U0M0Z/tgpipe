import pytest

from tgApp.config.core import DATASET_DIR, config
from tgApp.processing.smiles_manager import DatabaseExtractor


@pytest.fixture()
def sample_input_data():
    return DatabaseExtractor().extract(
        file=str(DATASET_DIR) + "/" + config.app_config.test_data_file
    )
