from pathlib import Path

# ROOT directory = project folder
ROOT_DIR = Path(__file__).resolve().parent.parent

# Useful paths
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
OUTPUTS_DIR = ROOT_DIR / "outputs"
SRC_DIR = ROOT_DIR / "src"

CONFIG_PATH = ROOT_DIR / "config.yaml"