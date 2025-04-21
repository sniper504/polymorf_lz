import pandas as pd
from abc import ABC, abstractmethod

class Cleaner(ABC):
    def __init__(self, df_path):
        self.data = pd.read_csv(df_path)

    @abstractmethod
    def clean(self):
        pass

class DeleteDuplicates(Cleaner):
    def clean(self):
        return self.data.drop_duplicates()

    def __invert__(self):  # ~ для удаления дубликатов
        initial_rows = len(self.data)  # До удаления
        self.data = self.data.drop_duplicates()
        self.removed_rows = initial_rows - len(self.data)  # Сколько строк удалено
        return self

class SplitByOperation(Cleaner):
    def clean(self):
        operation_types = self.data["Тип операции"].unique()  
        separated_files = {}

        for operation in operation_types:
            filtered_data = self.data[self.data["Тип операции"] == operation]
            filename = f"{operation.lower().replace(' ', '_')}_data.csv"
            filtered_data.to_csv(filename, index=False)
            separated_files[operation] = filename

        return separated_files

    def __invert__(self):  # ~ для разделение датасета
        return self.clean()
