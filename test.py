"""This is test for the checking DN of cert function"""
import os
import json
x = {"countryName": "PL", "organizationalUnitName": "Unit", "organizationName": "Some_organization", "localityName": "WARSAW", "stateOrProvinceName": "MAZOWIECKIE"}
def DN_check(filename, client_DN ):
    DN_file = open(filename, "r")
    cert_dictionary_list = []
    for line in DN_file:
        dictionary=json.loads(line)
        cert_dictionary_list.append(dictionary)
    list_of_equal = filter(lambda x: x == client_DN, cert_dictionary_list)
    if list_of_equal != 0:
        return True
    else: 
		return False
print(DN_check("Test_DN", x))
