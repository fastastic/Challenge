# Using curl or similarr provide a script that monitors the stub_status endpoint created in the Nginx section. Can you parse the "Active connections" and get the value?
import requests

response = requests.get('http://localhost/basic_status')

# [0] to get the first line [1] to get the second part of the string after the ":" character and [1:] to remove the space before the number
active_connections = response.text.splitlines()[0].split(":")[1][1:]

print(active_connections)
