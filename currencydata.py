import requests
import json
import xml.dom.minidom
import os 

def parser():
     for root,dirs,files in os.walk('dir'):
        for file in files:
            filename,extension=os.path.splitext(file)
            if extension=='.json':
                print(filename)





api_key = "<ENTER-KEY-HERE>"
example_text = "Hollo, wrld" # the text to be spell-checked
endpoint = "https://finans.truncgil.com/today.json"
data = {'text': example_text}
params = {
    'mkt':'en-us',
    'mode':'proof'
    }
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': api_key,
    }
response = requests.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()
for key,value in json_response.items():
    if key=="USD":
        dolar = value
        
val = value
result = str(val)
print (value)


def main():
    parser()
   

if __name__=="__main__":
    main()
