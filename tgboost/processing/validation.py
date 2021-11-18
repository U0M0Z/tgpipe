from typing import List, Optional, Tuple

import pandas as pd  # type: ignore
from pydantic import BaseModel


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    validated_data.dropna(inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    relevant_data = input_data.copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    # try:
    # replace numpy nans so that pydantic can validate
    #    MultipleSmilesDataInputs(
    #        yolo=validated_data.replace({np.nan: None}).to_dict(orient="records")
    #    )
    # except ValidationError as error:
    #    errors = error.json()

    return validated_data, errors


class SmilesDataInputSchema(BaseModel):
    # SMILES: List[str]
    SMILES: Optional[str]
    # embeddings: Optional[list]
    # predictions: Optional[float]


class MultipleSmilesDataInputs(BaseModel):
    yolo: List[SmilesDataInputSchema]
