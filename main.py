import speech_recognition as sr
import pyttsx3
from config import *
from random import choice
import re
#import sys
#import getpass

reproducao = pyttsx3.init()

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def nome():
    global user_name
    print ('Diga seu nome')
    sai_som('Diga seu nome')
    while True: 
                resposta_erro_aleatoria = choice(lista_erros)
                rec= sr.Recognizer()
                
                with sr.Microphone() as s:
                    rec.adjust_for_ambient_noise(s)

                    while True:
                            try:
                                
                                audio = rec.listen(s)
                                user_name = rec.recognize_google(audio, language="pt")
                                user_name= verifica_nome(user_name)
                                arquivo()
                                apresentacao = '{}'.format(verifica_nome_exist(user_name))
                                print(apresentacao)
                                sai_som(apresentacao)

                                break
                                
                            except sr.UnknownValueError:
                                sai_som(resposta_erro_aleatoria)
                    break




    
    print('='* len(apresentacao))
    
def encurta_nome():
    try:
        global user_name
        user_name= user_name
    except:
        user_name= 'Giovanni Scheer'
    brute_user_name = user_name
    user_name= user_name.split(" ")
    user_name = user_name[0]
    
def assistente():
    print('Pode falar...')

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec= sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt")
                    print ("{}: {}".format(user_name,entrada))
                    print(entrada)
                    if entrada in comandos: 
                        resposta = comandos[entrada]
                        print(resposta)
                    #"Quanto é" in entrada or 'quanto é' in entrada:

                      #  resposta = calcula(entrada)
                    elif entrada in conversas:
                        resposta = conversas[entrada]
                        print(resposta)
                        sai_som(resposta)
                        break
                    else:
                        print('Assistente: {}'.format(resposta))
                        sai_som('{}'.format(resposta))
                        
                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)

if __name__== '__main__':
    intro()
    sai_som('iniciando')
    #nome()
    encurta_nome()
    assistente()

