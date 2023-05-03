import requests, datetime

grabGcode = "http://drawing.local/server/files/list?root=gcodes"

x = requests.get(grabGcode)

printscall = x.json()

prints = printscall['result']

count = len(prints)

selected = prints[0]['path']

printGcode = "http://drawing.local/printer/print/start?filename={}".format(selected)

#requests.post(printGcode)

print(count)