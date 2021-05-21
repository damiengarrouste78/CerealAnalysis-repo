

"""Module de chargement et vérification des données d'entrée.

Usage:
======
    interne
"""

__authors__ = "Romeo NOUDOFININ"
__contact__ = ("email@gmail.com", "email@company.com")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2021/01"


import pandas as pd

def load_data(data_path):
	
	df = pd.read_csv(data_path, delimiter=';', decimal=".", encoding = 'utf-8')
	return df



def check_data(df, relevant_col_path):
	# List of data columns
	data_columns = list(df.columns)
	print("Data columns: {}".format(data_columns))
	#print("\n")

	# Load list of relevant columns
	f = open(relevant_col_path, "r")
	loaded_relevant_col = f.read().split('\n')
	f.close()
	print("Mandatory columns: {}".format(loaded_relevant_col))
	#print("\n")

	# Check if our list of columns contains all relevant columns
	list_columns = list(df.columns)
	included =  all(elem in data_columns  for elem in loaded_relevant_col)
	if included:
	    print("data_columns contains all mandatory columns")
	    variable_ok = True
	else :
	    print("data_columns does not contains all elements in loaded_relevant_col")
	    variable_ok = False

	return variable_ok


