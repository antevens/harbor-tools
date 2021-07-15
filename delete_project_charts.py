#!/usr/bin/env python

import requests
import json

user = "username"
password = "SuperSecretPass123!"

r = requests.get('https://harbor.example.com/api/v2.0/projects?page=1&page_size=100', auth=(user, password))
#print(r.status_code)
#print(r.text)

for project in r.json():
    if project['name'] != 'dekn':
        print(project['name'])
        c = requests.get('https://harbor.example.com/api/chartrepo/' + project['name'] + '/charts?page=1&page_size=1', auth=(user, password)) #/api/chartrepo/library/charts/harbor
#        print(c.status_code)
        for chart in c.json():
            print(chart['name'])
            cd = requests.delete('https://harbor.example.com/api/chartrepo/' + project['name'] + '/charts/' + chart['name'], auth=(user, password)) #/api/chartrepo/library/charts/harbor
            print(cd.status_code)
            #print(cd.text)
        pd = requests.delete('https://harbor.example.com/api/v2.0/projects/' + str(project['project_id']), auth=(user, password))
        print(pd.status_code)



#print(json.dumps(r, sort_keys=True, indent=4))
