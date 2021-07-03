import ubelt
import requests
ServerName = "" #server name
updates = ubelt.cmd('sudo apt update')['out'].splitlines()[-1]

resp = requests.post('https://textbelt.com/text', {
    'phone': '', #Number to Send to
    'message': ServerName + ": " + updates,
    'key': '', #textbelt Api key
})
print(resp.json())

