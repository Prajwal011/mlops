from ml_complete_proj.constants import *
from ml_complete_proj.utils.common import read_yaml, create_directories
from ml_complete_proj.entity.config_entity import DataIngestionConfig
from ml_complete_proj.entity.config_entity import DataValidationConfig
from ml_complete_proj.entity.config_entity import DataTransformationConfig
from ml_complete_proj.entity.config_entity import ModelTrainerConfig
from ml_complete_proj.entity.config_entity import ModelEvaluationConfig
import os


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema,
        )
        return data_validation_config

    def get_data_transformation(self) -> DataTransformationConfig:
        
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )

        return data_transformation_config


    def get_model_trainer(self)-> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
                root_dir = config.root_dir,
                train_data_path = config.train_data_path,
                test_data_path = config.test_data_path,
                model_name = config.model_name,
                alpha = params.alpha,
                l1_ratio = params.l1_ratio,
                target_column = schema.name)

        return model_trainer_config


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config1 = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        config2 = self.config.mlflow_info

        os.environ['MLFLOW_TRACKING_URI'] = config2.tracking_uri
        os.environ['MLFLOW_TRACKING_USERNAME'] = config2.tracking_username
        os.environ['MLFLOW_TRACKING_PASSWORD'] = config2.tracking_password

        create_directories([config1.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config1.root_dir,
            test_data_path=config1.test_data_path,
            model_path = config1.model_path,
            all_params=params,
            metric_file_name = config1.metric_file_name,
            target_column = schema.name,
            mlflow_uri= config2.tracking_uri,

        )

        return model_evaluation_config