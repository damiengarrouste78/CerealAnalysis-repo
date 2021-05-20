
"""Cette application réalise l'analyse des données issues de plusieurs céréals.

Usage:
======
    python CerealAnalysis
"""

__authors__ = "Romeo NOUDOFININ"
__contact__ = ("email@gmail.com", "email@company.com")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2021/01"





####################################
##   Import packages and Modules
####################################
import logging
import sys
sys.path.append(".\\")


import data_loader
import DataAnalyser.statistics as stats
import DataAnalyser.data_viz as viz


####################################
##   Log config
####################################
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')



logging.info('CerealAnalysis launched')

def run():

	####################################
	##   Data Paths
	####################################

	input_data = "CerealAnalysis\\data\\input\\"
	output_data = "CerealAnalysis\\data\\output\\"

	
	####################################
	##   Loading Data
	####################################

	# Load Data
	df = data_loader.load_data(input_data+"cereal_data.csv")
	logging.info('Input data loaded')

	# Check Data
	logging.info('Input data checking ...')
	variable_ok = data_loader.check_data(df, input_data+"relevant_col.txt")
	logging.info('Input data checked')


	####################################
	##   Stats
	####################################

	# If data is ok, then produce stats desc and visualisations
	if variable_ok == True:

		logging.info('Input data is OK')

		# var_num stats
		df_desc_num = stats.desc_num(df)

		# var_cat stats
		df_desc_cat = stats.desc_cat(df)

		# aggregation stats, by fat
		agg_fat = stats.aggregation(df, "fat")

		# aggregation stats, by mfr
		agg_mfr = stats.aggregation(df, "mfr")


		logging.info('Descriptive statistics calculated')



		####################################
		##   Viz
		####################################

		# Rating distribution
		distribution_rating = viz.var_distribution(df, var_name='rating')

		# scatter plot entre rating and sugars
		scatter_rating_sugars = viz.scatter(df, var_name1='sugars', var_name2='rating', var_hover='name')

		# scatter plot entre rating and sugars + boxplots pour sugar + violins pour rating
		scatter2_rating_sugars = viz.scatter_plus(df, var_name1="sugars", var_name2="rating", var_color="shelf")

		# Boxplots pour le rating, par mfr
		box_rating = viz.box_plot(df, var_name="rating", var_color="mfr")

		# Un treemap pour illustrer la nature hiérarchique des données
		treemap = viz.treemap(df, hierarchy=['shelf', 'mfr'], var_value='cereal', the_title = 'Cereals by shelf location')

		# Un Sunburst pour illustrer la nature hiérarchique des données
		sunburst = viz.sunburst(df, hierarchy=['shelf', 'mfr'], var_value='cereal', the_title = 'Cereals by shelf location')

		# Bubble chart pour rating et sugars
		Bubble_rating_sugars = viz.bubble(df, var_name1='sugars', var_name2='rating', var_color='mfr', var_size='calories',
										var_facet='shelf', var_hover='name', orders={'shelf': ['Top', 'Middle', 'Bottom']})


		logging.info('Data visualisation created')



		####################################
		##   Save Results
		####################################

		# Saving tables into excel files
		df_desc_num.to_csv(output_data+'cereal_desc_num.csv', sep=';', index=False, encoding='utf-8')
		df_desc_cat.to_csv(output_data+'cereal_desc_cat.csv', sep=';', index=False, encoding='utf-8')

		agg_fat.to_csv(output_data+'agg_fat.csv', sep=';', index=False, encoding='utf-8')
		agg_mfr.to_csv(output_data+'agg_mfr.csv', sep=';', index=False, encoding='utf-8')

		logging.info('Descriptive statistics results saved into excel file at {}'.format(output_data))


		# Saving visualisation into unique html file
		with open(output_data+'cereal_reporting.html', 'a') as f:
		    f.write(distribution_rating.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(scatter_rating_sugars.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(scatter2_rating_sugars.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(box_rating.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(treemap.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(sunburst.to_html(full_html=False, include_plotlyjs='cdn'))
		    f.write(Bubble_rating_sugars.to_html(full_html=False, include_plotlyjs='cdn'))

		logging.info('Data visualisation results saved into html file at {}'.format(output_data))


