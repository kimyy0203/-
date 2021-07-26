import os
import sys
import urllib.request
#from pprint import pprint

client_id = "USL_GhRZTP2fe4Iez2Pu"
client_secret = "HVyxp9t9TD"

def get_translate(text, lan):
    encText = urllib.parse.quote(text)
    data = f"source=ko&target={lan}&text=" + encText
    
    '''
    data = {'text' : text,
            'source' : 'ko',
            'target': lan}
    '''

    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    '''
    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}
    '''

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


while True:
    text = input("한국말 : ")
    lan = input("번역할 언어 (영어 : en, 일어 : ja) :")
    print(get_translate(text, lan))
    select = input("번역기를 계속해서 사용하실 건가요?(Y/N) : ")
    if select == "N" or select == "n":
        break
