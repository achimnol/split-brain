import os
import sys
from pathlib import Path
from zipfile import ZipFile

from pex.pex_bootstrapper import bootstrap_pex_env


def _bootstrap(pex_path: Path) -> None:
    pex_abspath = pex_path.resolve()
    pex_abspath_str = os.fsdecode(pex_abspath)
    bootstrap_pex_env(pex_abspath_str)
