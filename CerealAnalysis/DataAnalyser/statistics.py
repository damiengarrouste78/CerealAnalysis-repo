"""Module de statistiques descriptives.

Usage:
======
    interne
"""

__authors__ = "Romeo NOUDOFININ"
__contact__ = ("email@gmail.com", "email@company.com")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2021/01"



# var_num stats
def desc_num(df, var_num=['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'rating']):

	df_desc_num =  df[var_num].describe()
	df_desc_num["KPI"] =  df_desc_num.index
	return df_desc_num

# var_cat stats
def desc_cat(df, var_cat=['mfr', 'type', 'shelf']):

	df_desc_cat =  df[var_cat].describe()
	df_desc_cat["KPI"] =  df_desc_cat.index
	return df_desc_cat


# aggregation stats
def aggregation(df, var_by):

	agg_var = df.groupby([var_by], as_index=False) \
	.agg({'rating': ['mean', 'max'] \
	      ,'sugars':'mean' \
	      ,'carbo' :'mean' \
	      ,'protein' :'mean'})

	return agg_var