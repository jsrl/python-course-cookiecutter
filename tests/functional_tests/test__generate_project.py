"""Test that the cookiecutter template is valid."""

from pathlib import Path


def test__can_generate_project(project_dir: Path) -> None:
    """
    execute `cookiecutter <template directory> ...`
    """
    assert project_dir.exists()
