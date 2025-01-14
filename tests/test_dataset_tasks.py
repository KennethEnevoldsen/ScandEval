"""Unit tests for the `dataset_tasks` module."""

import pytest

from scandeval.config import DatasetTask
from scandeval.dataset_tasks import get_all_dataset_tasks


class TestGetAllDatasetTasks:
    @pytest.fixture(scope="class")
    def dataset_tasks(self):
        yield get_all_dataset_tasks()

    def test_dataset_tasks_is_dict(self, dataset_tasks):
        assert isinstance(dataset_tasks, dict)

    def test_dataset_tasks_are_objects(self, dataset_tasks):
        for dataset_task in dataset_tasks.values():
            assert isinstance(dataset_task, DatasetTask)

    def test_get_ner_dataset_task(self, dataset_tasks):
        assert "named-entity-recognition" in dataset_tasks
