# -*- coding: utf-8 -*-
""" xml
Created on Wed Jul 26 12:32:48 2017
@author: Alissa
"""
import os
os.cd='C:\Users\Alissa\Documents\Springboard\DataWrangling\data_wrangling_xml\data_wrangling_xml\data'
from xml.etree import ElementTree as ET
document_tree = ET.parse( 'mondial_database_less.xml' )
# print names of all countries
for child in document_tree.getroot():
    print child.find('name').text