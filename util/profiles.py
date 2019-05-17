"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM
"""
from os.path import join
from os import listdir
from tqdm import tqdm
import matplotlib.pyplot as plt

from util import utilities as Utils
from util import input_parser as Parser


class Profiler:

    @staticmethod
    def plot_profile_images(dataset_loc, map_name, id_label, output_folder, sf, forget_level_text, is_normalized):

        # Construct configs
        title = '{} Analysis on {} - SF:{} Forget:{}'.format(map_name, map_name, sf, forget_level_text)

        # Load dataset
        df, labels, selected_vars, minmax = Parser.InputParser.get_original_data(dataset_loc, map_name, id_label, is_normalized)

        # Load pickle files
        filename = [join(output_folder, fname) for fname in listdir(output_folder) if '.pickle' in fname][0]
        gsom_nodemap = Utils.Utilities.load_object(filename.replace('.pickle', ''))[0]['gsom']

        # Setup image root folder
        image_root_folder = join(output_folder, 'images')

        x_values = list(range(len(selected_vars) - 1))
        for key, value in tqdm(gsom_nodemap.items(), desc='Building profile'):

            sel_emp_list = [labels[i] for i in value.get_mapped_labels()]

            if value.get_hit_count() > 0:

                fig = plt.figure()
                ax = fig.add_subplot(211)
                plt.title(title)

                plt.ylim(minmax[0], minmax[1])

                cur_emp = df.loc[df[id_label].isin(sel_emp_list)]

                for idx, row in cur_emp.iterrows():
                    y_values = [row[col] for col in selected_vars if col not in [id_label]]
                    ax.plot(x_values, y_values, label=row[id_label])

                ax.set_xticks(x_values)
                ax.set_xticklabels([col for col in selected_vars if col not in [id_label]], rotation=90)
                ax.legend(prop={'size': 6})
                ax.grid(True)

                plt.tight_layout()
                output_filename = join(image_root_folder,
                                       'node_profile_{}.png'.format(key.replace('-', 'm').replace(':', '_')))
                plt.savefig(output_filename, dpi=800)

                plt.clf()
                plt.close()
