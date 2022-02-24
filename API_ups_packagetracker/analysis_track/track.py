import packagetracker
import pandas as pd
import numpy as np

data= pd.read_csv('tracking_number.csv', header = None)
# data = np.loadtxt('track_number.txt')
# headerList = ['tracking_id', 'service', 'weight']
# data.to_csv("tracking_number.csv", header=headerList, index=False)
#def simple_f(tracking)

def simple_f(tracking_id):
    row = data.iloc[0].to_string(index= False)
    tracker = packagetracker.PackageTracker()
    package = tracker.package(tracking_id)
    info = package.track()
    return info.weight, info.service

weight_list = []
service_list = []
for i in range(len(data)):
    row = data.iloc[i].to_string(index= False)
    weight, service = simple_f(row)
    weight_list.append(weight)
    service_list.append(service)
    
data.columns = ['tracking_id'] 
data['weight'] = weight_list
data['service'] =service_list

data.to_csv('out.csv')