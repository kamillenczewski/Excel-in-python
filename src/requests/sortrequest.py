from src.requests.request import Request
from src.datamanager import DataManager


class SortRequest(Request):
    def __init__(self, source_names, key_source_name, destination_names, key=None):
        self.source_names = source_names
        self.key_source_name = key_source_name
        self.destination_names = destination_names
        self.key = key

    def execute(self, data_manager: DataManager): 
        values_sets = [data_manager.get_values(source_name) for source_name in self.source_names]
    
        key_source_index = self.source_names.index(self.key_source_name)

        key_set = values_sets[key_source_index]
        indices = range(0, len(key_set))
        key_set_and_indices = zip(key_set, indices)

        key_set_and_indices = sorted(key_set_and_indices, key=self.key)

        indices = [index for _, index in key_set_and_indices]

        for values_set in values_sets:
            for i in range(len(values_set)):
                values_set[i] = values_set[indices[i]]

        for values_set, destination_name in zip(values_sets, self.destination_names):
            data_manager.set_values(values_set, destination_name)