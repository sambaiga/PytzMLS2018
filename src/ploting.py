
import matplotlib
import matplotlib.dates as dates
import matplotlib as mpl
from matplotlib import rcParams
import pandas as pd
import numpy as np
from datetime import datetime, timezone
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler


# Format python plot with Latex
SPINE_COLOR = 'gray'
dark_colors = ["#ba1a31", "#2d6dce",             
								(0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
								(0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
								(0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
								(0.4, 0.6509803921568628, 0.11764705882352941),
								(0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
								(0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
								(0.4, 0.4, 0.4)]

def beatify(fig_width=None, fig_height=None, columns=1):
		"""Set up matplotlib's RC params for LaTeX plotting.
		Call this before plotting a figure.
		Parameters
		----------
		fig_width : float, optional, inches
		fig_height : float,  optional, inches
		columns : {1, 2}
		"""

		# code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

		# Width and max height in inches for IEEE journals taken from
		# computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

		assert(columns in [1,2])

		if fig_width is None:
				fig_width = 3.39 if columns==1 else 6.9 # width in inches

		if fig_height is None:
				golden_mean = (np.sqrt(5)-1.0)/2.0    # Aesthetic ratio
				fig_height = fig_width*golden_mean # height in inches

		MAX_HEIGHT_INCHES = 8.0
		if fig_height > MAX_HEIGHT_INCHES:
				print("WARNING: fig_height too large:" + fig_height + 
							"so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
				fig_height = MAX_HEIGHT_INCHES

				
			 


		params = {#'backend': 'ps',
							#'text.latex.preamble': ['\\usepackage{gensymb}'],
							'axes.labelsize': 6, # fontsize for x and y labels (was 10)
							'axes.titlesize': 6,
							'font.size': 8, # was 10
							'font.family': "sans serif",
#							'font.serif': ['Times', 'Palatino', 'New Century Schoolbook', 'Bookman', 'Computer Modern Roman'],
#							'font.sans-serif' : ['Helvetica', 'Avant Garde', 'Computer Modern Sans serif'],
							'legend.fontsize': 8, # was 10
							'xtick.labelsize': 6,
							'ytick.labelsize': 6,           
							'grid.linestyle':"-",
							'patch.edgecolor': 'none',
							'grid.linewidth': 0.1,
							'grid.color':"gray" ,
							 'axes.facecolor': "white",
							'figure.dpi': 600,
							'lines.linewidth':0.75,
							'axes.prop_cycle':cycler('color', dark_colors),            
							'figure.figsize': [fig_width,fig_height],
		}

		matplotlib.rcParams.update(params)


def format_axes(ax):
		# Format axes plot
		for spine in ['top', 'right']:
				ax.spines[spine].set_visible(False)

		for spine in ['left', 'bottom']:
				ax.spines[spine].set_color(SPINE_COLOR)
				ax.spines[spine].set_linewidth(.75)
				ax.spines[spine].set_smart_bounds(False)

		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		
		ax.get_xaxis().tick_bottom()    
		ax.get_yaxis().tick_left()

		for axis in [ax.xaxis, ax.yaxis]:
				axis.set_tick_params(direction='out', color=SPINE_COLOR)

#    matplotlib.pyplot.tight_layout()

		return ax    



def get_datesstring(timestamps):
		"""
		Transform a date string into unix timestam
		"""
		time = [datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M') 
						for x in timestamps]
		return time
