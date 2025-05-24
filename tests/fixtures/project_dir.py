"""Project directory fixture for testing purposes."""
import shutil
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import generate_project


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "test-repo",
    }
    generated_report_dir: Path = generate_project(template_values=template_values)
    yield generated_report_dir
    shutil.rmtree(path=generated_report_dir)
