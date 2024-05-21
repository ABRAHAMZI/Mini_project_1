## if i want to save my code to cloud 
# i use this space
# call utils inside components to use 
# i can get data from mangodb from here

import os
import sys
import numpy as np
import pandas as pd 
from exception1 import CustomException
import dill

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
