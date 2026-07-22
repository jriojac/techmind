"""
==========================================================
TechMind
Data Science Component

Module:
    validation_runner.py

Description:
    Coordinates the complete validation workflow.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

from dataclasses import dataclass

from validation.dataset_validator import DatasetValidator
from validation.preprocessing_validator import PreprocessingValidator
from validation.benchmark import Benchmark


@dataclass
class ValidationResult:
    """
    Result of the validation workflow.
    """

    dataframe: object

    document: object

    processed_document: object

    benchmark: object


class ValidationRunner:
    """
    Executes the complete validation workflow.
    """

    def __init__(self):

        self._dataset = DatasetValidator()
        self._preprocessing = PreprocessingValidator()
        self._benchmark = Benchmark()

    def run(
        self,
        dataset_path: str,
    ) -> ValidationResult:

        dataframe = self._dataset.load(dataset_path)

        self._dataset.validate_columns(dataframe)

        document = self._dataset.build_document(dataframe)

        processed = self._preprocessing.process(document)

        benchmark = self._benchmark.measure(
            self._preprocessing.process,
            [document],
        )

        return ValidationResult(
            dataframe=dataframe,
            document=document,
            processed_document=processed,
            benchmark=benchmark,
        )
    