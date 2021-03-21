from params import *
import shutil
import pathlib


if __name__=='__main__':

    os.chdir(pathlib.Path(__file__).parent.absolute())
    shutil.copy(PROJECT_RAW_DATA_PATH,EXPERIMENT_RAW_DATA_PATH)
