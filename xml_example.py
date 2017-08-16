# -*- coding: utf-8 -*-
""" xml
Created on Wed Jul 26 12:32:48 2017
@author: Alissa
"""
import os
os.cd='C:\Users\Alissa\Documents\Springboard\DataWrangling\data_wrangling_xml\data_wrangling_xml\data'
#from xml.etree import ElementTree as ET
from lxml import etree
doc=etree.parse('mondial_database_less')
#document_tree = ET.parse('mondial_database_less.xml')
# print names of all countries
for child in document_tree.getroot():
    print child.find('name').text

# print names of all countries and their cities
for element in document_tree.iterfind('country'):
    print '* ' + element.find('name').text + ':',
    capitals_string = ''
    for subelement in element.getiterator('city'):
        capitals_string += subelement.find('name').text + ', '
    print capitals_string[:-2]

