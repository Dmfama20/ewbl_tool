#import csv
#import collections

#grades = collections.Counter()
#with open('ebwl.csv') as input_file:
    #for row in csv.reader(input_file, delimiter=','):
        #grades[row[3]] += 1

#print('Anzahl Abgeschlossen: %s' % grades['Abgeschlossen'])
##print(grades.most_common())


import csv
my_reader = csv.reader(open('progress.e-bwl.csv'),delimiter=',')
#ncol = len(next(my_reader)) # Read first line and count columns
#get fieldnames from DictReader object and store in list
header = next(my_reader)
indices = [i for i, s in enumerate(header) if 'test' in s]
#print(indices)
for j in indices:
    my_reader = csv.reader(open('progress.e-bwl.csv'),delimiter=',')
    ctr=0;
    #print(header[j])
    for record in my_reader:
        if record[j][0:13] == "Abgeschlossen":
            ctr += 1
    print(header[j],":",ctr )


    
