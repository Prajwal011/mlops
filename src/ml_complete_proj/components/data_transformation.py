import os
from ml_complete_proj import logger
from ml_complete_proj.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config

    def split(self):
        
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, )

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info(f"Splited data into training and testing sets")
        logger.info(f"{train.shape}")
        logger.info(f"{test.shape}")

        print(train.shape)
        print(test.shape)