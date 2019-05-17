"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM
"""
import pandas as pd
import numpy as np


class InputParser:

    @staticmethod
    def parse_data(data_filename, dataset, id_label, normalize=True):
        df = pd.read_excel(open(data_filename, 'rb'), sheet_name=dataset)

        label = list(df[id_label])

        del df[id_label]

        selected_vars = df.columns

        # Normalize data
        values = df.values
        if normalize:
            normalized_df = (df - df.min()) / (df.max() - df.min())
            values = normalized_df.values

        input_database = {
            0: values
        }

        return input_database, label, selected_vars

    @staticmethod
    def get_original_data(data_filename, dataset, id_label, normalize=True):
        df = pd.read_excel(open(data_filename, 'rb'), sheet_name=dataset)

        label = list(df[id_label])

        # Normalize data
        if normalize:

            copy_df = df.copy(deep=True)

            del copy_df[id_label]

            normalized_df = (copy_df - copy_df.min()) / (copy_df.max() - copy_df.min())
            normalized_df[id_label] = df[id_label]
            df = normalized_df

        min_value = min(list(df.select_dtypes(include=[np.number]).min()))
        max_value = max(list(df.select_dtypes(include=[np.number]).max()))

        return df, label, list(df.columns), (min_value, max_value)