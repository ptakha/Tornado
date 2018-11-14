#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''class RestSender and his test'''
import json
import os
import requests

#pylint: disable = invalid-name, line-too-long

class RestSender:
    """Get URL, certificates and keys and send request"""
    def __init__(self, URL, HostCertificate, HostKey, CAcertificate):
        """initiating of sender"""		
        self.url = URL
        self.HostCertificate = HostCertificate
        self.HostKey = HostKey
        self.CAcertificate = CAcertificate
    def send_message(self, message):
        """Sending of message"""
        msg = json.dumps(message, separators=(', ', ': '))
        post = requests.post(self.url, json=msg, cert=(self.HostCertificate, self.HostKey), verify=self.CAcertificate)
        return post.text
    def get_responce(self):
        """Get method of sender (just for test and pylint)"""
        get = requests.get(self.url, cert=(self.HostCertificate, self.HostKey), verify=self.CAcertificate)
        return get




if __name__ == '__main__':
    URL = 'https://localhost:1027/json'
    localcert = os.path.join("CA_test/test.cert.pem")
    localkey = os.path.join("CA_test/test.key.pem")
    CAcert = os.path.join("CA_test/ca.cert.pem")
    msg = {
        'status': 'info',
        'phase': 'Installing',
        'timestamp': '1427121370.7',
        'messageContent': 'Uname = Linux localhost 3.10.64-85.cernvm.x86_64',
        'pilotUUID': 'eda78924-d169-11e4-bfd2-0800275d1a0a',
        'source': 'InstallDIRAC'
    }
    Sender = RestSender(URL, localcert, localkey, CAcert)
    print(Sender.send_message(msg))
    
    
