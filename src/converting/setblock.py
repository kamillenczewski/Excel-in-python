from src.converting.datalocation import DataLocation

class SetBlock:
    def __init__(self, destination: DataLocation, data_generator):
        self.destination = destination
        self.data_generator = data_generator