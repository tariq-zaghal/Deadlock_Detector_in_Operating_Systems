import pandas as pd
import deadlock_detector_helper as ddh

allocation_file = pd.read_csv('Allocation.csv')
request_file = pd.read_csv('Request.csv')
available_file = pd.read_csv('Available.csv')

status_list = []

for i in range(len(allocation_file)):
    status_list.append(False)

if ddh.check_dimensions(allocation_file, request_file, available_file):
    print("files dimensions are inconsistent")
else:
    result = ddh.detect_deadlock(allocation_file, request_file, available_file, status_list)
    if result[0]:
        print("No deadlock detected")
        print("The Execution series could be")
        print(result[1])
    else:
        print("deadlock detected")
        print("The processes in deadlock are")
        print(result[1])
