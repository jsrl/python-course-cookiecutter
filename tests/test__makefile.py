import subprocess
from pathlib import Path

import pytest


def test__linting_passes(project_dir: Path):
    subprocess.run(["make","lint-ci"], cwd=project_dir, check=True)

def test__test_pass():
    ...

def test__install_succeds():
    ...

