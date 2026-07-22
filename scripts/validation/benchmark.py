"""
==========================================================
TechMind
Data Science Component

Module:
    benchmark.py

Description:
    Measures preprocessing pipeline performance.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from dataclasses import dataclass
from time import perf_counter


# ==========================================================
# Benchmark Result
# ==========================================================

@dataclass(slots=True)
class BenchmarkResult:
    """
    Stores benchmark metrics.
    """

    documents: int
    success: int
    failed: int

    success_rate: float

    total_time: float
    average_time: float

    min_time: float
    max_time: float

    documents_per_second: float

    errors: list[str]


# ==========================================================
# Benchmark
# ==========================================================

class Benchmark:
    """
    Measures preprocessing performance.
    """

    def measure(
        self,
        func,
        documents,
    ) -> BenchmarkResult:

        processed = 0
        success = 0
        failed = 0

        execution_times = []
        errors = []

        global_start = perf_counter()

        for document in documents:

            start = perf_counter()

            try:

                func(document)

                success += 1

            except Exception as ex:

                failed += 1
                errors.append(str(ex))

            elapsed = perf_counter() - start

            execution_times.append(elapsed)

            processed += 1

        total = perf_counter() - global_start

        average = (
            sum(execution_times) / processed
            if processed
            else 0.0
        )

        throughput = (
            processed / total
            if total > 0
            else 0.0
        )

        minimum = (
            min(execution_times)
            if execution_times
            else 0.0
        )

        maximum = (
            max(execution_times)
            if execution_times
            else 0.0
        )

        success_rate = (
            (success / processed) * 100
            if processed
            else 0.0
        )

        return BenchmarkResult(
            documents=processed,
            success=success,
            failed=failed,
            success_rate=success_rate,
            total_time=total,
            average_time=average,
            min_time=minimum,
            max_time=maximum,
            documents_per_second=throughput,
            errors=errors,
        )