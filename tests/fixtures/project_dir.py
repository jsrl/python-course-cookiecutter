"""Fixture for a reusable cookiecut template project for tests."""

import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

# pylint: disable=no-name-in-module
from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    """Create an instance of our cookiecutter template to be re-used in tests."""
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"test-repo-{test_session_id}",
        "package_import_name": f"test_package_{test_session_id}",
    }
    generated_report_dir: Path = generate_project(template_values=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(repo_dir=generated_report_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_report_dir, check=False)
        yield generated_report_dir
    finally:
        shutil.rmtree(path=generated_report_dir)


def generate_test_session_id() -> str:
    """Return a randomly generated, unique string."""
    test_session_id = str(uuid4())[:6]
    return test_session_id
