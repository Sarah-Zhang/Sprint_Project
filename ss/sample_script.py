import sys
import json
import os

prefix = sys.argv[1]
path = '/srv/runme/'
output = []

try:
    os.remove(path + prefix)
except OSError:
    pass

file = [filename for filename in os.listdir(path) if filename.startswith(prefix)]
for filename in file:
    with open(filename) as json_data:
        for line in json_data:
            try:
                json_line = json.loads(line)
                output.append((json_line['name'], json_line['prop']['age']))
            except:
                pass

with open(path + prefix, 'w') as f:
    for i in output:
        f.write(str(i[0]) + " " + str(i[1]) + "\n")