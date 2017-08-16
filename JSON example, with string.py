# -*- coding: utf-8 -*-
"""JSON examples and exersize
Created on Fri Jul 21 16:40:17 2017

@author: Alissa
"""
import pandas as pd
import json
from pandas.io.json import json_normalize
"""creation of normalized dataframes from nested json string
   source: http://pandas.pydata.org/pandas-docs/stable/io.html#normalization"""

# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]   
json_normalize(data,'counties')
print(type(json_normalize(data,'counties')))

print(json_normalize(data,'counties'))
# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
# load json as string
json.load((open('data/world_bank_projects_less.json')))
# load as Pandas dataframe
sample_json_df = pd.read_json('data/world_bank_projects_less.json')
sample_json_df
# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])

   