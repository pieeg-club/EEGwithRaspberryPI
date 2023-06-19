import pandas as pd
import numpy as np
import sys
import time

data_lenght_for_Filter = 3     # how much we read data for filter, all lenght  [_____] + [_____] + [_____]
read_data_lenght_one_time = 2   # for one time how much read  [_____]

lenght_data_for_filter = data_lenght_for_Filter*read_data_lenght_one_time-read_data_lenght_one_time
print ()
name_columns =  []
final_dataset = []
just_one_time = 0

data_before = []
data_after =  []
data_read = [1,2,3]

while 1:
    if just_one_time == 0:
        for b in range (0,data_lenght_for_Filter,1):
            for a in range (0,read_data_lenght_one_time,1):
                #data_read = data_read + 1
                data_read = [x + 3 for x in data_read]
                data_before.append(data_read)                

        just_one_time = 1
        data_before = data_before[read_data_lenght_one_time:]
            
    for c in range (0,read_data_lenght_one_time,1):
        #data_read = data_read + 1
        data_read = [x + 3 for x in data_read]
        data_after.append(data_read)
        
    data_after_flip = data_after
    data_after_flip = data_after[::-1]#.reverse()

    data_before_for_sum = data_before
    data_after_for_sum = data_after
    
    data_before_for_sum = [item for sublist in data_before for item in sublist]
    data_after_for_sum = [item for sublist in data_after for item in sublist]
    
    dataset =  data_before_for_sum + data_after_for_sum #+ data_after_flip
    print ("dataset", dataset)

    dataset_before = data_before + data_after
    data_before = dataset_before[read_data_lenght_one_time:]
   #data_before = data_before[:read_data_lenght_one_time]

    data_after = []
    dataset = []
    time.sleep(1.5)
