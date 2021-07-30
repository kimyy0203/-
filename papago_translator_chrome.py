from tkinter import *
from tkinter.ttk import *
import requests

client_id = "USL_GhRZTP2fe4Iez2Pu"
client_secret = "HVyxp9t9TD"


def get_translate(text, lan1, lan2): #파파고 번역기 사용 함수
    data = {'text' : text,
            'source' : lan1,
            'target': lan2}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        t_data = response.json()
        result = t_data['message']['result']['translatedText']
        #result는 중첩형 딕서녀리의 구조를 가지고 있다
        return result
    else: #오류 발생시 오류 코드 반환
        return "Error Code:" + str(rescode)


def process(): #"번역" 버튼 클릭시 번역 실행 함수
    before = (e1.get("1.0","end")) #첫 번째 Text에서 번역 전 문장 입력받기
    e2.delete("1.0","end") #결과 반환 전에 두 번째 Text 비우기
    #e3.delete("1.0","end") #결과 반환 전에 세 번째 Text 비우기
    lan1 = select(combo1) #첫 번째 콤보박스에서 번역 전 언어값 입력받기
    lan2 = select(combo2) #두 번째 콤보박스에서 번역 후 언어값 입력받기
    #lan3 = select(combo3) #세 번째 콤보박스에서 번역 후 언어값 입력받기
    after2 = get_translate(before, lan1, lan2)
    #after3 = get_translate(before, lan1, lan3)
    #번역 전 문장, 번역할 언어, 변역될 언어를 변수로 설정하여 변역 함수 호출하기
    e2.insert("1.0", after2) #결과를 두 번째 Text에 삽입
    #e3.insert("1.0", after3) #결과를 세 번째 Text에 삽입

  
def select(combo): #콤보박스의 해당 인덱스를 받아서 언어 설정하기
    lan = combo.current()
    if lan == 0: #한국어
        return "ko"
    elif lan == 1: #영어
        return "en"
    elif lan == 2: #일본어
        return "ja"
    elif lan == 3: #중국어 간체
        return "zh-CN"
    elif lan == 4: #중국어 번체
        return "zh-TW"
    elif lan == 5: #베트남어
        return "vi"
    elif lan == 6: #인도네시아어
        return "id"
    elif lan == 7: #태국어
        return "th"
    elif lan == 8: #독일어
        return "de"
    elif lan == 9: #러시아어
        return "ru"
    elif lan == 10: #스페인어
        return "es"
    elif lan == 11: #이탈리아어
        return "it"
    elif lan == 12: #프랑스어
        return "fr"

    
window = Tk()
window.title("파파고 번역기")
#window.geometry("600x100")

Label(window, text = "   번역 전   ").grid(row=0, column=0)
Label(window, text = "   번역 후   ").grid(row=2, column=0)
#Label(window, text = "   번역 후   ").grid(row=4, column=0)

e1 = Text(window, fg="black", bg="white", width=50, height=5) #번역 전 Text
e2 = Text(window, fg="black", bg="white", width=50, height=5) #번역 후 Text
#e3 = Text(window, fg="black", bg="white", width=50, height=5) #번역 후 Text
e1.grid(row=0, column=1)#, padx=20, pady=20, ipadx=20, ipady=20)
e2.grid(row=2, column=1)#, padx=20, pady=20, ipadx=20, ipady=20)
#e3.grid(row=4, column=1)#, padx=20, pady=20, ipadx=20, ipady=20)

combo1 = Combobox(window, width=12) #번역 전 언어 선택
combo1['values']=("한국어","영어","일본어","중국어 간체","중국어 번체","베트남어","인도네시아어","태국어","독일어","러시아어","스페인어","이탈리아어","프랑스어")
combo1.current(0)
combo1.grid(row=1, column=0)

combo2 = Combobox(window, width=12) #번역 후 언어 선택
combo2['values']=("한국어","영어","일본어","중국어 간체","중국어 번체","베트남어","인도네시아어","태국어","독일어","러시아어","스페인어","이탈리아어","프랑스어")
combo2.current(1)
combo2.grid(row=3, column=0)

#combo3 = Combobox(window, width=12) #번역 후 언어 선택
#combo3['values']=("한국어","영어","일본어","중국어 간체","중국어 번체","베트남어","인도네시아어","태국어","독일어","러시아어","스페인어","이탈리아어","프랑스어")
#combo3.current(1)
#combo3.grid(row=5, column=0)

Button(window, text="번역", command=process).grid(row=6, column=1) #번역하는 버튼

window.mainloop()