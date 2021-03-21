import pathlib
import os

# calculations

RANDOM_SEED = 123

# paths

os.chdir(pathlib.Path(__file__).parent.absolute())

PROJECT_RAW_DATA_PATH = os.path.join("..","..","..","data","reviews_full.xlsx")
EXPERIMENT_RAW_DATA_PATH = os.path.join("data","raw","reviews_full.xlsx")
EXPERIMENT_PROCESSED_DATA_FOLDER = os.path.join("data","processed","reviews_full.xlsx")

TEST_SET_FILENAME = "test.xlsx"
TRAIN_SET_FILENAME = "train.xlsx"

