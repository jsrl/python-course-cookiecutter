"""Project directory fixture for testing purposes."""
import shutil
import subprocess
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "test-repo",
    }
    generated_report_dir: Path = generate_project(template_values=template_values)
    initialize_git_repo(repo_dir=generated_report_dir)
    subprocess.run(["make","lint-ci"],cwd=generated_report_dir, check=False)
    yield generated_report_dir
    shutil.rmtree(path=generated_report_dir)
