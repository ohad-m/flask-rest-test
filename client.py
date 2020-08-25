import requests, json

# curl -X POST -d '{"a":"b"}' -H "Content-Type: application/json" http://localhost:5000/add

headers = {'Content-Type': 'application/json'}

r = requests.post('http://localhost:5000/add',
                headers=headers, 
                data=json.dumps({"a":"b"}))