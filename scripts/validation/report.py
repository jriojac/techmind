"""
==========================================================
TechMind
Data Science Component

Module:
    report.py

Description:
    Displays validation results in the console.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

# ==========================================================
# Report
# ==========================================================

class Report:

    LINE = "=" * 60
    SEPARATOR = "-" * 60

    def _title(self, title: str):

        print()
        print(self.LINE)
        print(title)
        print(self.LINE)

    def show_dataset(
        self,
        dataset_path: str,
        dataframe,
    ):

        self._title("DATASET")

        print(f"Ruta      : {dataset_path}")
        print(f"Registros : {len(dataframe)}")
        print(f"Columnas  : {len(dataframe.columns)}")

    def show_document(
        self,
        document,
    ):

        self._title("DOCUMENT RECORD")

        print(f"ID        : {document.document_id}")
        print(f"Título    : {document.title}")
        print(f"Categoría : {document.category}")
        print(f"Idioma    : {document.language}")

    def show_preprocessing(
        self,
        document,
        processed,
    ):

        self._title("PREPROCESSING")

        # --------------------------------------------------
        # Original Text
        # --------------------------------------------------

        print("Texto original")
        print(self.SEPARATOR)
        print(document.text[:300])

        print(f"\nCaracteres: {len(document.text)}")

        # --------------------------------------------------
        # Processed Text
        # --------------------------------------------------

        print()
        print(self.SEPARATOR)

        print("\nTexto procesado")
        print(self.SEPARATOR)
        print(processed.processed_text[:300])

        print(f"\nCaracteres: {len(processed.processed_text)}")

        # --------------------------------------------------
        # Tokens
        # --------------------------------------------------

        print()
        print(self.SEPARATOR)

        print("\nTokens")
        print(self.SEPARATOR)

        print(processed.tokens)

        print(
            f"\nCantidad de tokens: "
            f"{len(processed.tokens)}"
        )

        # --------------------------------------------------
        # Lemmas
        # --------------------------------------------------

        print()
        print(self.SEPARATOR)

        print("\nLemmas")
        print(self.SEPARATOR)

        print(processed.lemmas)

        print(
            f"\nCantidad de lemmas: "
            f"{len(processed.lemmas)}"
        )

    def show_benchmark(
        self,
        benchmark,
    ):

        self._title("BENCHMARK")

        print(f"Documentos procesados : {benchmark.documents}")
        print(f"Tiempo total          : {benchmark.total_time:.6f} s")
        print(f"Tiempo promedio       : {benchmark.average_time:.6f} s")
        print(
            f"Documentos/segundo    : "
            f"{benchmark.documents_per_second:.2f}"
        )

    def show_success(self):

        self._title("RESULTADO")

        print("✓ Pipeline ejecutado correctamente")