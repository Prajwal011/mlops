import os
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from ml_complete_proj import logger 
from ml_complete_proj.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config = ModelTrainerConfig):
        self.config = config

    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        train_x = train_df.drop([self.config.target_column], axis = 1)
        test_x = test_df.drop([self.config.target_column], axis = 1)
        train_y = train_df[[self.config.target_column]]
        test_y = test_df[[self.config.target_column]]

        model = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state = 42)
        
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))