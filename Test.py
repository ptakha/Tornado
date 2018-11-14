"""This is test for the RestSender like """
import json
import requests
import os
# pylint: disable = invalid-name



localcert = os.path.join("CA_test/localhost.cert.pem")
localkey = os.path.join("CA_test/localhost.key.pem")
CAcert = os.path.join("CA_test/ca.cert.pem")

msg = {
    'status': 'info',
    'phase': 'Installing',
    'timestamp': '1427121370.7',
    'messageContent': 'Uname = Linux localhost 3.10.64-85.cernvm.x86_64',
    'pilotUUID': 'eda78924-d169-11e4-bfd2-0800275d1a0a',
    'source': 'InstallDIRAC'
    }

URL = 'https://localhost:1025/json'
Json_msg = json.dumps(msg, separators=(', ', ': '))
P = requests.post(URL, json=Json_msg, cert=(localcert, localkey), verify=CAcert)
print "'Post' test of json handler"
print P.text
