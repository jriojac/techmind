"""
==========================================================
TechMind
Data Science Component

Module:
    preprocessing_validator.py

Description:
    Validates the preprocessing pipeline.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from data_science.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)


# ==========================================================
# Preprocessing Validator
# ==========================================================

class PreprocessingValidator:
    """
    Executes and validates the preprocessing pipeline.
    """

    def __init__(self):

        self._pipeline = PreprocessingPipeline()

    # ======================================================
    # Public API
    # ======================================================

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Executes the preprocessing pipeline.
        """

        return self._pipeline.process(document)

    def process_many(
        self,
        documents: list[DocumentRecord],
    ) -> list[ProcessedDocument]:
        """
        Executes preprocessing for multiple documents.
        """

        return [
            self.process(document)
            for document in documents
        ]