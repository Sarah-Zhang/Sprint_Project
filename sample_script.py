import sys
import json
import os

debug = []

try:
    import datetime
    debug.append(datetime.datetime.now())
except:
    pass

print 'running sample_script' 

prefix = sys.argv[1]
path = '/srv/runme/'
output = []

if not os.path.isdir(path):
        os.makedirs(path)

files = [filename for filename in os.listdir(path) if filename.startswith(prefix)]
debug.append('found ' + str(len(files)) + ' file(s)')

for file in files:
    with open(path+file) as json_data:  # give full path of the file since we are in home directory...?
        # Go over each line in json
        for line in json_data:
            # Check if each line is in proper json format
            try:
                json_line = json.loads(line)
                # filter out wrong hierarchy - if wrong, a KeyError will be returned
                try:
                    # Get rid of empty lines and filter out the target entries with empty string:
                    if (bool(json_line)) and (json_line['name'] != '') and (json_line['prop']['age'] >= 0) and (json_line['prop']['age'] != ''):
                        output.append((json_line['name'],json_line['prop']['age']))
                    else:
                       pass
                except (KeyError):
                    pass
            except (ValueError):
                pass

debug.append('processed ' + str(len(output)) + ' records')

with open(path + prefix+'.txt', 'w') as f:
     for i in range(len(output)):
            f.write(str(output[i][0]) + " " + str(output[i][1]) + "\n")

debug.append('records saved to file')
with open('debug.txt', 'a') as d:
    d.write(str(debug)+'\n')
