from textSummarizer.pipeline.step_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.step_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.step_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.step_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.logger import logging


STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logging.exception(e)
   raise e


STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logging.exception(e)
   raise e


STAGE_NAME = "Data Transformation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logging.exception(e)
   raise e


STAGE_NAME = "Model Trainer stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logging.exception(e)
   raise e