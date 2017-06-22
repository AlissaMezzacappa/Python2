# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:10:07 2017

@author: Alissa
"""
 m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
 m.group(0)       # The entire match
'Isaac Newton'
 m.group(1)       # The first parenthesized subgroup.
'Isaac'
 m.group(2)       # The second parenthesized subgroup.
'Newton'
 m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.group('first_name')
'Malcolm'
m.group('last_name')
'Reynolds'