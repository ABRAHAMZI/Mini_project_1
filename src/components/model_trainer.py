## confusion matrix, rsquare , also here
import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from exception1 import CustomException
from logger1 import logging

from utils1 import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):#,preproceesor_path
        try:
            logging.info("split training and test input data")

            X_train,Y_train,X_test,Y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Random_Forest":RandomForestRegressor(),
                "Decision_Tree": DecisionTreeRegressor(),
                "Gradient_Boosting":GradientBoostingRegressor(),
                "Linear_Regressor":LinearRegression(),
                "K_Neighbors_Regressor":KNeighborsRegressor(),
                "XGB_Regressor":XGBRegressor(),
                "CatBoosting_Regressor":CatBoostRegressor(),
                "AdaBoost_Regressor":AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(X_train=X_train,Y_train=Y_train,X_test=X_test,Y_test=Y_test,models=models)

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            if best_model_score< 0.6:
                raise CustomException("NO best model found")
            logging.info(f"Best found model on both training and testing dataset")

            # preprocessing_obj
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2_square=r2_score(Y_test,predicted)
            return r2_square

        except Exception as e:
            raise CustomException(e,sys)