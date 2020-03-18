# Part. 1
#=======================================
# Import module
# csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107000118.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   # 以迴圈輸出每一列
   for row in mycsv: 
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
# Deal with the data indivitually in each station

#===================C0A880====================

target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   if tmp > max:
    max = tmp

output_list = []

if tmp == -99 or tmp == -999:
   output_list.append(['C0A880','None'])
else:
   output_list.append(['C0A880',max])


#====================C0F9A0===================

target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   if tmp > max:
    max = tmp

if  tmp == -99 or tmp == -999:
   output_list.append(['C0F9A0','None'])
else:
   output_list.append(['C0F9A0',max])


#====================C0G640===================

target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   if tmp > max:
    max = tmp

if tmp == -99 or tmp == -999:
   output_list.append(['C0G640','None'])
else:
   output_list.append(['C0G640',max])


#=====================C0R190==================

target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   if tmp > max:
    max = tmp

if  tmp == -99 or tmp == -999:
   output_list.append(['C0R190','None'])
else:
   output_list.append(['C0R190',max])


#=====================C0X260==================

target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   if tmp > max:
    max = tmp

if tmp == -99 or tmp == -999:
   output_list.append(['C0X260','None'])
else:
   output_list.append(['C0X260',max])

print (output_list)