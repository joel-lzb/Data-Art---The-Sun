#!/usr/bin/python

# a simple script used to automate the generation of multiple circos plots with space weather data according to year.

import sys
import csv
import os

if sys.version_info[0] > 2:
	raise Exception("this script uses Python 2")

if len(sys.argv) != 3:
	print 'USAGE: ', sys.argv[0],' <input.csv> <tree.txt>'
	sys.exit(1)

csvFile = sys.argv[1]
treeFile = sys.argv[2]


##### MODIFY #####
graphlan_annotate_script = 'graphlan_annotate.py' # point to graphlan_annotate.py script

graphlan_script = 'graphlan.py' # point to graphlan.py script


def annotHeaders(currYear): # overall plot parameters
	return '''
start_rotation	270
branch_bracket_width	1
branch_bracket_depth	0.5
branch_thickness	0.5
clade_marker_size	10
clade_marker_edge_width	0.8
annotation_background_alpha	0.4

branch_color	w

Year	clade_marker_edge_color	w
Year	clade_marker_font_size	30
Year	clade_marker_label	'''+ currYear +'''

ring_color	16	#800000
ring_color	15	#aa6e28
ring_color	14	#fffac8
ring_color	13	#ffd8b1
ring_color	12	#fabebe
ring_color	11	#e6194b
ring_color	10	#f58231
ring_color	9	#ffe119
ring_color	8	#d2f53c
ring_color	7	#3cb44b
ring_color	6	#808000
ring_color	5	#008080
ring_color	4	#0082c8
ring_color	3	#000080
ring_color	2	#911eb4
ring_color	1	#e6beff

1	annotation_background_color	m
2	annotation_background_color	b
3	annotation_background_color	g
4	annotation_background_color	r

'''

swParams = { # ring effects
	'E_06MeV': 'ring_alpha	1',
	'E_2MeV': 'ring_alpha	2',
	'P_1MeV': 'ring_alpha	3',
	'P_10MeV': 'ring_alpha	4',
	'P_100MeV': 'ring_alpha	5',
	'Radio_Flux': 'ring_alpha	6',
	'XRay_Bkgd_Flux': 'ring_alpha	7',
	'MLF_A': 'ring_alpha	8',
	'HLC_A': 'ring_alpha	9',
	'EP_A': 'ring_alpha	10',
	'Sunspot_Area': 'ring_alpha	11',
	'Sunspot_Number': 'ring_alpha	12',
	'S': 'ring_alpha	13',
	'O1': 'ring_alpha	14',
	'O2': 'ring_alpha	15',
	'O3': 'ring_alpha	16',
	'Flare_tot': 'ring_height	17',
}

leafID = 'Month-Day' # name of column containing the sample identifier

yearID = 'Year' # name of column containing the main node info

####################



# read in csv file as dictionary
with open(csvFile) as f:
	reader = csv.DictReader(f)
	swData = [r for r in reader]


# get all years available in data and sort from oldest to latest:
yearsDict = {}
for rows in range(0, len(swData)-1):
	yearsDict[swData[rows][yearID]] =  swData[rows][yearID]

yearsList = list(yearsDict.values())
yearsList.sort()


# generate the annotation file for each year:
for thisYear in yearsList:
	outFileName = 'SW_annot_' + thisYear + '.txt'
	with open(outFileName,"w+") as outFile:# open a new file
	
		outFile.write(str(annotHeaders(thisYear))) # write the common annotations
	
		for nrows in range(0, len(swData)-1):
			if swData[nrows][yearID] == thisYear:
				for k, v in swParams.items():
					outLine = swData[nrows][leafID] + '\t' + swParams[k] + '\t' + swData[nrows][k] + '\n'
					outFile.write(outLine)
	
	# run graphlan_annotate.py
	cmd1 = 'python '+ graphlan_annotate_script + ' --annot ' + outFileName + ' ' + treeFile + ' ' + outFileName + '.xml'
	os.system(cmd1)

	# run graphlan.py
	cmd2 = 'python '+ graphlan_script + ' --dpi 300 --size 8 ' + outFileName + '.xml ' + outFileName + '.png'
	os.system(cmd2)



## Created by: Joel Low Zi-Bin 20180811 ##