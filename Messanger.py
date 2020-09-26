#!/usr/bin/env python
# coding: utf-8

# In[9]:


from twilio.rest import Client
from googletrans import Translator,LANGUAGES
import sqlite3
trans=Translator()
account_sid="AC23b3b6813aa1cad9c2d62803ab2edbcf"
account_token="66aa3c9bc8a6df5b9331adc9e974c542"
client = Client(account_sid,account_token)
def send_message(number,message):
        client.messages.create(
            to =number,
            from_ ="+16318134581",
            body =message

        )
def get_number_and_lang(region):
    conn = sqlite3.connect('data.db')
    c=conn.cursor()
    numbers=[]
    lang_pref=[]
    l=c.execute("SELECT Num,Lang from profile WHERE State='{}'".format(region))
    l=list(l)
    print(l)
    for i in range(len(l)):
            numbers.append(l[i][0])
            lang_pref.append(l[i][1])
    c.close()
    conn.close()
    return numbers,lang_pref
def getcode(x):
    for lang in LANGUAGES:
        if LANGUAGES[lang]==x:
            return (lang)
def translate(message,destination_lang):
    translator=Translator()
    t=trans.translate(message,src='en',dest=destination_lang)
    return t.text
def main(incoming_param):
    x=incoming_param.split('*')
    region=x[0]
    pest=x[1]
    if pest=='':
        message = "Unknown Pest are attacking the farms of {}.".format(region)
    else:
        #solution=getsolution(pest)
        message = "{} are attacking the farms of {}.".format(pest,region) 
    numbers,language_pref=get_number_and_lang(region)
    print(numbers,language_pref,message)
    for i in range(len(language_pref)):
        code=getcode(language_pref[i].lower())
        x=translate(message,code)
        try:
            send_message(numbers[i],x)
        except:
            pass


# In[ ]:




