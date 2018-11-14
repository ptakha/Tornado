"""This is test for the second tornado study server"""
import requests

G = requests.get('https://localhost:1025')
print("'Get' test of MainHandler")
print G.text
P = requests.post('https://localhost:1025', data={'User':'U','Password':'R'})
print("'Post' test of user autenfication with correct data")
print P.text
P1 = requests.post('https://localhost:1025', data={'User':'U','Password':'Password'})
print("'Post' test of user autenfication with incorrect data")
print P1.text
G1 = requests.get('https://localhost:1025/random')
print("'Get' test of MathHandler")
print G1.text

