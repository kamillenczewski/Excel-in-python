class DataSets:
    def __init__(self, source_names, datasets):
        self.names_and_data_sets = {
            name: dataset 
            for name, dataset 
            in zip(source_names, datasets)
        }
        
        self.validate_and_set_dataset_size()

    def get(self, name):
        if name not in self.names_and_data_sets:
            raise ValueError(f'There is no data set called: {name}')
        
        return self.names_and_data_sets[name]
    
    def get_element(self, name, index):
        data_set = self.get(name)

        if index >= len(data_set):
            raise ValueError(f'Index should be in interval: [0, {len(data_set) - 1}]')

        return data_set[index] 
    
    def get_dataset_size(self):
        return self.size
    
    def validate_and_set_dataset_size(self):
        data_sets = list(self.names_and_data_sets.values())

        self.size = len(data_sets[0])

        for data_set in data_sets:
            if len(data_set) != self.size:
                return False
        
        return True