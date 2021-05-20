"""Module de visualisation.

Usage:
======
    interne
"""

__authors__ = "Romeo NOUDOFININ"
__contact__ = ("email@gmail.com", "email@company.com")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2021/01"



import plotly.express as px
import plotly.graph_objects as go


def var_distribution(df, var_name='rating'):

	distribution_ = px.histogram(df, x=var_name,  marginal="rug", title='{} distribution'.format(var_name))
	#distribution_.show()
	return distribution_



def scatter(df, var_name1='sugars', var_name2='rating', var_hover='name'):

	scatter_ = px.scatter(df, x=var_name1, y=var_name2, trendline="lowess", hover_name=var_hover,
                                   title='{} vs. {}'.format(var_name1, var_name2))
	#scatter_.show()
	return scatter_



def scatter_plus(df, var_name1="sugars", var_name2="rating", var_color="shelf"):

	scatter_plus_ = px.scatter(df, x=var_name1, y=var_name2, color=var_color, marginal_x="box", marginal_y="violin",
	                                    title='{} vs. {}'.format(var_name1, var_name2))
	#scatter_plus_.show()
	return scatter_plus_



def box_plot(df, var_name="rating", var_color="mfr"):
	box_rating = px.box(df, y=var_name, points="all", color=var_color, title="Box plot for {}, by {}".format(var_name, var_color))
	#box_rating.show()
	return box_rating



def treemap(df, hierarchy=['shelf', 'mfr'], var_value='cereal', the_title = 'Cereals by shelf location'):
	treemap_ = px.treemap(df, path=hierarchy, values=var_value, title=the_title)
	#treemap_.show()
	return treemap_



def sunburst(df, hierarchy=['shelf', 'mfr'], var_value='cereal', the_title = 'Cereals by shelf location'):
	sunburst_ = px.sunburst(df, path=hierarchy, values=var_value, title=the_title)
	#sunburst_.show()
	return sunburst_



def bubble(df, var_name1='sugars', var_name2='rating', var_color='mfr', var_size='calories', 
			var_facet='shelf', var_hover='name', orders={'shelf': ['Top', 'Middle', 'Bottom']}):

	Bubble_rating_sugars = px.scatter(df,
	                x=var_name1,
	                y=var_name2,
	                color=var_color,
	                size=var_size,
	                facet_row=var_facet,
	                #facet_col='type',
	                hover_name=var_hover,
	                category_orders=orders)
	#Bubble_rating_sugars.show()
	return Bubble_rating_sugars

