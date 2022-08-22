##import pickle
## 
##data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
##data_string = pickle.dumps(data)
##print ('PICKLE:', data_string ,end=" ")



import json
  
# python object(dictionary) to be dumped
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
  
# the json file where the output must be stored
out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()
