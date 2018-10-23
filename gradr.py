import csv
import pandas
from canvasapi import Canvas
import os
import sys

csv_file = sys.argv[1] 
df = pandas.read_csv(csv_file)
df.insert(loc=0, column='Calculated grade', value = df['22.1 - Lab (135)']*135/100)
df.drop(columns=['Primary email', 'Participation total (0)', 'Total (135)', 'Challenge total (0)'])

API_URL = os.environ['API_URL']
API_KEY = os.environ['API_KEY']
COP3503_NUM = 357209

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COP3503_NUM)

sections = course.get_sections()

# section_4B37 = sections[0]
# section_04C4 = sections[1]
# section_19G8 = sections[2]
# section_35HA = sections[3]
# section_128D = sections[4]
# section_128H = sections[5]
# section_129E = sections[6]
section_141B = sections[7]
section_141D = sections[8]
# section_1278 = sections[9]
# section_1280 = sections[10]
section_1889 = sections[11]
# section_1907 = sections[12]
# section_1927 = sections[13]
# section_7255 = sections[14]
# section_8228 = sections[15]
# section_8229 = sections[16]
# section_8230 = sections[17]
# section_MISC = sections[18]

my_sections = [section_1889, section_141B, section_141D]

for each_section in my_sections:
	section_number = each_section
	print('Grades for section: ' + str(section_number))
	enrollments = []
	for student in course.get_section(section_number).get_enrollments():
		if student.user['sortable_name'] != 'Student, Test':
			enrollments.append(student.user['sortable_name'].split(','))
	gradedList = []
	for index, student in df.iterrows():
		for canvas in enrollments:
			if(student['Last name'] == canvas[0]):
				if(student['First name'][0] == canvas[1][1]):
					gradedList.append([canvas[0], canvas[1], student['Calculated grade']])
	for i in gradedList:
		print(i)



