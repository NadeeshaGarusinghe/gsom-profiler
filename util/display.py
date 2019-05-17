"""
Python display plots:
https://python-graph-gallery.com/all-charts/
"""

import matplotlib.pyplot as plt
import numpy as np

"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM 
"""
from matplotlib import cm
from matplotlib import colors


class Display:

    def __init__(self, gsom_node_map, aggregated_node_map):
        self.gsom_node_map = gsom_node_map
        self.aggregated_node_map = aggregated_node_map

    def setup_labels_for_gsom_nodemap(self, new_node_map, labels, title, output_filename, selected_vars):

        self.gsom_node_map = new_node_map

        plt.figure()
        plt.title(title)

        max_count = max([node.get_hit_count() for _, node in self.gsom_node_map.items()])
        listed_color_map = Display._get_color_map(max_count, alpha=0.9)

        for key, value in self.gsom_node_map.items():

            key_split = key.split(':')
            x = int(key_split[0])
            y = int(key_split[1])

            if value.get_hit_count() > 0:
                plt.plot(x, y, 'o', color=listed_color_map.colors[value.get_hit_count()], markersize=2)
                label_str = ','.join([str(labels[lbl_id]).split('_')[0] for lbl_id in value.get_mapped_labels()])
                plt.text(x, y + 0.3, label_str, fontsize=4)
            else:
                plt.plot(x, y, 'o', color=listed_color_map.colors[value.get_hit_count()], markersize=2)

        comment2_txt = 'Selected variables are ' + ', '.join(selected_vars) + '.'
        plt.xlabel(comment2_txt, fontsize=4)
        plt.savefig(output_filename + '.jpeg', dpi=1200)
        plt.clf()
        plt.close('all')

    @staticmethod
    def get_color_map(max_count, alpha=0.5):

        np.random.seed(1)

        cmap = cm.get_cmap('Reds', max_count + 1)  # set how many colors you want in color map
        # https://matplotlib.org/examples/color/colormaps_reference.html

        color_list = []
        for ind in range(cmap.N):
            c = []
            for x in cmap(ind)[:3]: c.append(x * alpha)
            color_list.append(tuple(c))

        return colors.ListedColormap(color_list, name='gsom_color_list')

    @staticmethod
    def _get_color_map(max_count, alpha=0.5):

        np.random.seed(1)

        cmap = cm.get_cmap('Reds', max_count + 1)  # set how many colors you want in color map
        # https://matplotlib.org/examples/color/colormaps_reference.html

        color_list = []
        for ind in range(cmap.N):
            c = []
            for x in cmap(ind)[:3]: c.append(x * alpha)
            color_list.append(tuple(c))

        return colors.ListedColormap(color_list, name='gsom_color_list')
