from abc import abstractmethod
from src.datamanager import DataManager

class Request:
    @abstractmethod
    def execute(self, data_manager: DataManager):
        pass