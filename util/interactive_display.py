"""
Author: Rashmika Nawaratne
Date: 17-May-19 at 11:27 AM
"""
from os.path import join
from os import listdir
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from util import utilities as Utils
from util import display as Display_Utils


class InteractiveDisplay:

    @staticmethod
    def plot_interactive(map_name, output_folder, sf, forget_level_text):

        # Construct configs
        title = '{} Analysis - SF:{} Forget:{}'.format(map_name, sf, forget_level_text)

        # Load pickle files
        filename = [join(output_folder, fname) for fname in listdir(output_folder) if '.pickle' in fname][0]
        gsom_nodemap = Utils.Utilities.load_object(filename.replace('.pickle', ''))[0]['gsom']

        # Setup image root folder
        image_root_folder = join(output_folder, 'images')
        image_filename_prefix = 'node_profile_'

        display = Display_Utils.Display(None, None)

        # Make the plot
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title(title)

        max_count = max([node.get_hit_count() for _, node in gsom_nodemap.items()])
        listed_color_map = display.get_color_map(max_count, alpha=0.9)

        for key, value in gsom_nodemap.items():

            key_split = key.split(':')
            x = int(key_split[0])
            y = int(key_split[1])

            if value.get_hit_count() > 0:
                ax.plot(x, y, 'o', color=listed_color_map.colors[value.get_hit_count()], markersize=3)
                ax.text(x, y + 0.1, str(value.get_hit_count()), fontsize=4)
            else:
                ax.plot(x, y, 'o', color=listed_color_map.colors[value.get_hit_count()], markersize=3)

        def onclick(event, args_list):

            ix, iy = event.xdata, event.ydata
            x, y = int(round(ix)), int(round(iy))
            print("Clicked at x={0:5.2f}, y={1:5.2f}".format(ix, iy), "Select to show", x, y)

            image_folder = args_list[0]
            prefix = args_list[1]

            key = '{}_{}'.format(str(x).replace('-', 'm'), str(y).replace('-', 'm'))
            fname = prefix + key + '.png'

            try:
                plt.figure()
                print('fname', join(image_folder, fname))
                plt.title('Node: {}-{}'.format(x, y))
                img = mpimg.imread(join(image_folder, fname))
                imgplot = plt.imshow(img, interpolation='none')
                imgplot.axes.set_axis_off()
                plt.show()

            except:
                print('No cluster w.r.t. selected node')

        cid = fig.canvas.mpl_connect('button_press_event',
                                     lambda event: onclick(event, [image_root_folder, image_filename_prefix]))
        plt.show()
