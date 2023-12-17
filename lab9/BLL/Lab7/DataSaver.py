import json
import os
import pandas as pd

class DataSaver:
    """
    The DataSaver class saves data in various formats.
    """
    @staticmethod
    def save_data(data, format):
        """
        Saves data in the specified format.
        """
        directory = os.path.join('..', 'Data', 'Lab7')

        if not os.path.exists(directory):
            os.makedirs(directory)

        if format == 'json':
            filepath = os.path.join(directory, 'data.json')
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
        elif format == 'csv':
            if isinstance(data, dict):
                data = [data]
            df = pd.DataFrame(data)
            filepath = os.path.join(directory, 'data.csv')
            df.to_csv(filepath)
        elif format == 'txt':
            filepath = os.path.join(directory, 'data.txt')
            with open(filepath, 'w') as f:
                for item in data:
                    f.write("%s\n" % item)
