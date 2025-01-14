"""Factory which produces datasets from a configuration."""

from typing import Optional, Type, Union

from .benchmark_dataset import BenchmarkDataset
from .config import BenchmarkConfig, DatasetConfig
from .dataset_configs import get_dataset_config
from .utils import get_class_by_name


class DatasetFactory:
    """Factory which produces datasets from a configuration.

    Args:
        benchmark_config (BenchmarkConfig):
            The benchmark configuration to be used in all datasets constructed.

    Attributes:
        benchmark_config (BenchmarkConfig):
            The benchmark configuration to be used in all datasets constructed.
    """

    def __init__(self, benchmark_config: BenchmarkConfig) -> None:
        self.benchmark_config = benchmark_config

    def build_dataset(self, dataset: Union[str, DatasetConfig]) -> BenchmarkDataset:
        """Build a dataset from a configuration or a name.

        Args:
            dataset (str or DatasetConfig):
                The name of the dataset, or the dataset configuration.

        Returns:
            BenchmarkDataset:
                The benchmark dataset.
        """
        # Get the dataset configuration
        if isinstance(dataset, str):
            dataset_config = get_dataset_config(dataset)
        else:
            dataset_config = dataset

        # Get the benchmark class based on the task
        benchmark_cls: Optional[Type[BenchmarkDataset]] = get_class_by_name(
            [
                dataset_config.name,
                dataset_config.task.name,
                dataset_config.task.supertask,
            ]
        )
        if not benchmark_cls:
            raise ValueError(f"Unknown dataset task: {dataset_config.task}")

        # Create the dataset
        dataset_obj = benchmark_cls(
            dataset_config=dataset_config, benchmark_config=self.benchmark_config
        )

        return dataset_obj
