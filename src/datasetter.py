from src.setblock import SetBlock
from src.datamanager import DataManager

class DataSetter:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
    
    def single_set(self, setblock: SetBlock):
        values = [value for value in setblock.data_generator]
        self.data_manager.set_values(values, setblock.destination_name)
