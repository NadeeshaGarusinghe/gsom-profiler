"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM
"""
import time
import sys
import os
import itertools
from os import listdir
from os.path import join
from datetime import datetime
sys.path.append('../../')

import config as config
from util import input_parser as Parser
from util import display as Display_Utils
from util import profiles as profiler
from util import interactive_display as int_display
from util import utilities as Utils
from params import params as Params
from core4 import core_controller as Core


def generate_output_config(dataset, SF, forget_threshold, temporal_contexts, output_save_location):

    # Output data config
    output_save_filename = '{}_data_'.format(dataset)
    filename = output_save_filename + str(SF) + '_T_' + str(temporal_contexts) + '_mage_' + str(forget_threshold) + 'itr'
    plot_output_name = join(output_save_location, filename)

    # Generate output plot location
    output_loc = plot_output_name
    output_loc_images = join(output_loc, 'images/')
    if not os.path.exists(output_loc):
        os.makedirs(output_loc)
    if not os.path.exists(output_loc_images):
        os.makedirs(output_loc_images)

    return output_loc, output_loc_images


def plot_only_visualization():

    # Sample 'output/Exp-2019-05-09-18-35-48/Survey_data_0.5_T_1_mage_80itr'
    result_location = config.Configuration.results_location

    parameters = result_location.split('/')[-1].split('_')
    dataset = parameters[0]
    SF = parameters[2]
    forget_threshold_label = [f for f in listdir(result_location) if '.pickle' in f][0].split('_F-')[1].split('_')[0]
    interactive_plot_title = dataset + ' Analysis'

    print('Plot interactive visualization for {} with SF={} with {} forget threshold.'.format(dataset, SF, forget_threshold_label))

    int_display.InteractiveDisplay.plot_interactive(dataset, result_location, SF, forget_threshold_label,
                                                    interactive_plot_title)


def generate_latent_map(visualize=False):
    # File config
    dataset_location = config.Configuration.dataset_location
    experiment_id = 'Exp-' + datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    output_save_location = join('output/', experiment_id)
    ID_column_name = config.Configuration.ID_column_name
    is_normalized = config.Configuration.normalize_dataset

    # Grid search config
    sheet_names = config.Configuration.excel_sheet_names

    # GSOM Config
    SF_values = config.Configuration.SF_values
    learning_itr = config.Configuration.learning_itr
    smoothing_irt = config.Configuration.smoothing_irt
    forget_threshold_values = [int(learning_itr * (1 - tp)) for tp in config.Configuration.transience_percentages]
    temporal_contexts = 1
    plot_for_itr = 4

    for dataset in sheet_names:

        # Process the input files
        input_vector_database, labels, selected_vars = Parser.InputParser.parse_data(dataset_location, dataset,
                                                                                     ID_column_name, is_normalized)
        print('Latent Spaces for {}, using: \n{}'.format(dataset, list(selected_vars)))

        for SF, forget_threshold in itertools.product(SF_values, forget_threshold_values):
            print('\nProcessing with SF={} with Forgetting={}'.format(SF, forget_threshold))

            forget_threshold_label = Utils.Utilities.forget_thresh_label(learning_itr, forget_threshold)

            output_loc, output_loc_images = generate_output_config(dataset, SF, forget_threshold, temporal_contexts, output_save_location)

            # Init GSOM Parameters
            gsom_params = Params.GSOMParameters(SF, learning_itr, smoothing_irt,
                                                distance=Params.DistanceFunction.EUCLIDEAN,
                                                temporal_context_count=temporal_contexts,
                                                forget_itr_count=forget_threshold)
            generalise_params = Params.GeneraliseParameters(gsom_params)

            # Setup the age threshold based on the input vector length
            generalise_params.setup_age_threshold(input_vector_database[0].shape[0])

            # Process the clustering algorithm algorithm
            controller = Core.Controller(generalise_params)
            result_dict = controller.run(input_vector_database, plot_for_itr, labels, output_loc_images)
            Utils.Utilities.save_object(result_dict, join(output_loc, 'gsom_nodemap_SF-{}_F-{}'.format(SF, forget_threshold_label)))

            gsom_nodemap = result_dict[0]['gsom']

            print('Latent Space generated with {} neurons.'.format(len(gsom_nodemap)))

            # Visualizations
            display = Display_Utils.Display(gsom_nodemap, None)

            display.setup_labels_for_gsom_nodemap(gsom_nodemap, labels,
                                                  'Latent Space of {} : SF={} with Forget={}'.format(dataset, SF,
                                                                                                     forget_threshold_label),
                                                  join(output_loc, '{}_latent_space_SF-{}_F-{}_hit_count'.format(
                                                      dataset, SF, forget_threshold_label)),
                                                  selected_vars=selected_vars)

            # Plot profile images
            profiler.Profiler.plot_profile_images(dataset_location, dataset, ID_column_name, output_loc,
                                                  SF, forget_threshold_label, is_normalized)

            # Plot interactive profile visualization
            if visualize:
                int_display.InteractiveDisplay.plot_interactive(dataset, output_loc, SF, forget_threshold_label)


if __name__ == '__main__':

    # Decide based on whether only visualize or not
    if config.Configuration.only_visualize:
        plot_only_visualization()
    else:
        generate_latent_map(visualize=True)

    print('\nCompleted.')
