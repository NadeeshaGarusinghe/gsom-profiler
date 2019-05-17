"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM
"""


class Configuration:

    """This configuration file contains parameters for the gsom profile generator"""

    """
    Visualize previously generated latent space profiles.
    In order to visualize, you should have already constructed a latent representation.
    """
    only_visualize = False

    """
    If only visualizing you MUST provide the results location
    output folder pickle is located in app/output/Exp-datestamp/ 
    """
    results_location = 'output/Exp-2019-05-09-21-02-50/ZooAnimals_data_0.4_T_1_mage_100itr'

    """
    Location of the dataset (must be excel file format)
    """
    dataset_location = 'data/zoo_data.xlsx'

    """
    Excel sheet names that include datasets
    """
    excel_sheet_names = ['ZooAnimals']

    """
    ID/Identification column name
    """
    ID_column_name = 'animal_name'

    """
    Whether you need to normalize the dataset
    """
    normalize_dataset = True

    """
    Spread factor values- you may use multiple to plot hierarchical analysis
    """
    SF_values = [0.4]

    """
    Transience/Forgetting percentage threshold - lower the percentage value, lower the forgetting rate
    """
    transience_percentages = [0]

    """
    Training and smoothing iterations
    """
    learning_itr = 100
    smoothing_irt = 50
