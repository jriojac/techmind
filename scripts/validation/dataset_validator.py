"""
==========================================================
TechMind
Data Science Component

Module:
    dataset_validator.py

Description:
    Validates dataset compatibility with the Data Science
    component.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pandas as pd

from data_science.adapters.dataframe_adapter import (
    DataFrameAdapter,
)

from data_science.readers.csv_reader import (
    CsvReader,
)


# ==========================================================
# Dataset Validator
# ==========================================================

class DatasetValidator:
    """
    Validates datasets before entering the preprocessing
    pipeline.
    """

    REQUIRED_COLUMNS = {
        "document_id",
        "title",
        "content",
        "category",
        "language",
    }

    def __init__(self):

        self._reader = CsvReader()

        self._adapter = DataFrameAdapter()

    # ======================================================
    # Public API
    # ======================================================

    def load(
        self,
        dataset_path: Path,
    ) -> pd.DataFrame:
        """
        Loads the dataset.
        """

        if not dataset_path.exists():

            raise FileNotFoundError(dataset_path)

        return self._reader.read(dataset_path)

    def validate_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Validates required columns.
        """

        missing = (
            self.REQUIRED_COLUMNS.difference(
                dataframe.columns
            )
        )

        if missing:

            raise ValueError(
                f"Missing required columns: {missing}"
            )

    def build_document(
        self,
        dataframe: pd.DataFrame,
        row: int = 0,
        source: str = "fake_dataset",
    ):

        return self._adapter.to_document(
            row=dataframe.iloc[row],
            source=source,
        )

    def build_documents(
        self,
        dataframe: pd.DataFrame,
        limit: int | None = None,
        source: str = "fake_dataset",
    ):
        """
        Converts multiple DataFrame rows into DocumentRecord objects.
        """

        if limit is None:
            limit = len(dataframe)

        limit = min(limit, len(dataframe))

        return [
            self.build_document(
                dataframe=dataframe,
                row=index,
                source=source,
            )
            for index in range(limit)
        ]