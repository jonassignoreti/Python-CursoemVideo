'''Crie um código em Python
que teste se o site Pudim está acessível pelo computador usado.
>>> pudim.com.br

'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O Site Pudim.com.br NÃO está acessível')
else:
    print('O site Pudim.com.br está acessível!')
    print(site.read())
