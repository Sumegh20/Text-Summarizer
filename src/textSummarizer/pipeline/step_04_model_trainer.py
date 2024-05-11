from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logger import logging


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainr_config = config.get_model_trainer_config()
        model_trainr = ModelTrainer(config=model_trainr_config)
        model_trainr.train()