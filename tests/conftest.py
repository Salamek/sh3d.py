import pytest
from importlib.resources import files


from pathlib import Path

@pytest.fixture(scope="module")  # type: ignore
def sh3d_path() -> Path:
    self_dir = Path(__file__).resolve().parent
    return self_dir.joinpath('assets/myHome.sh3d')


@pytest.fixture(scope="module")  # type: ignore
def resources_path() -> Path:
    return Path(str(files("sh3d").joinpath("resources")))
