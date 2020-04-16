# -*- coding: utf-8 -*-
"""
Parsing Huawei LTE CM for 
Created on Sat Sep  7 2019
@author: hesam.mo
"""

import xml.etree.ElementTree as ET
tree = ET.parse(r"LTE\CM\CMExport_MBTS_L5019_2020041505.xml")
root = tree.getroot()

class_to_extract = 'BTS3900EUTRANEXTERNALCELL'
f1 = open('Huawei CM parsed partial.csv', mode='w')

att_list =['fdn','CELLID','DLEARFCN','DLFREQOFFSET',
'ENODEBFUNCTIONNAME','ENODEBID','MCC','MNC','MOIndex',
'PHYCELLID','TAC','className','name','neID']
text = 'fdn,CELLID,DLEARFCN,DLFREQOFFSET,ENODEBFUNCTIONNAME,ENODEBID,MCC,MNC,MOIndex,PHYCELLID,TAC,className,name,neID\n'
f1.write(text)

for item in root.findall(".//MO[@className='BTS3900EUTRANEXTERNALCELL']"):  #./channel/item
	text = ''
	for child in item: 		
		for i in child.attrib.values():#range(len(child)):
			
			text = text + child.text.replace(',', ';') + ','
	text +='\n'
	f1.write(text)

f1.close()
