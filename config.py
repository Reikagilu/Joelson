import re
from main import *
version = '1.0.5'

def intro():
    msg= 'Assistente Joelson - version {} / by G.Scheer'.format(version)
    print('-' * len (msg) +'\n{}\n'.format(msg) + '-' * len (msg))

lista_erros= [
    'Não entendi o que você disse',
    'Desculpe, pode repetir?',
    'Você disse alguma coisa?'
]


conversas = {
    'Olá': 'oi, tudo bem?',
    'sim e você': 'Estou bem, obrigado por perguntar'
    }

comandos = {
    'Quanto é' : 'Vai se fuder'
    #re.search('^Quanto é|quanto é',entrada) : print('é isso')
        #calcula(entrada)

    #'reiniciar': 'reiniciando'
    }

def verifica_nome(user_name):
    if user_name.startswith('Meu nome é'):
        user_name= user_name.replace ('Meu nome é','')
    if user_name.startswith('Eu sou o'):
        user_name= user_name.replace ('Eu sou o','')
    if user_name.startswith('Eu sou a'):
        user_name= user_name.replace ('Eu sou a','')
    if user_name.startswith('Me chamo'):
        user_name= user_name.replace ('Me chamo','')

    return user_name

def verifica_nome_exist(nome):
    dados = open('dados/nomes.txt', "r")
    nome_list = dados.readlines()

    if not nome_list:
            vazio = open('dados/nomes.txt', "r")
            conteudo= vazio.readlines()
            conteudo.append('{}'.format(nome))
            vazio = open ('dados/nomes.txt', 'w')
            vazio.writelines(conteudo)
            vazio.close()
            return 'Olá {}, prazer em te conhecer!'.format(nome)

    for linha in nome_list:
        if linha == nome:
                 return 'Olá {}, bem vindo de volta'.format(nome)

    desconhecido = open ('dados/nomes.txt', 'r')
    conteudo= desconhecido.readlines()
    conteudo.append('\n{}'.format(nome))
    desconhecido = open ('dados/nomes.txt', 'w')
    desconhecido.writelines(conteudo)
    desconhecido.close()
    return 'Olá {}, prazer em te conhecer!'.format(nome)

def arquivo():
    try:
        arq= open ('dados/nomes.txt', 'r')
        arq.close()
    except FileNotFoundError:
        arq = open ('dados/nomes.txt', 'w')
        arq.close()
        
def calcula(entrada):
    entrada=entrada.replace( 'Quanto é','')
    if 'mais' in entrada or '+' in entrada:
        n1= re.search('[0-9].+?(?=\+|mais)',entrada)
        n2= re.search('[^+|mais]*$',entrada)
        n11=float(n1.group())
        n22=float(n2.group())
        resultado=round((n11)+(n22),2)
    elif 'menos' in entrada or '-' in entrada:
        n1= re.search('[0-9].+?(?=\-|menos)',entrada)
        n2= re.search('[^-|menos]*$',entrada)
        n11=float(n1.group())
        n22=float(n2.group())
        resultado=round((n11)-(n22),2)
    elif 'vezes' in entrada or 'x' in entrada:
        n1= re.search('[0-9].+?(?=x|vezes)',entrada)
        n2= re.search('[^xvezs]*$',entrada)
        n11=float(n1.group())
        n22=float(n2.group())
        resultado=round((n11)*(n22),2)
    elif 'dividido' in entrada or '/' in entrada:
        n1= re.search('[0-9].+?(?=\/|dividido)',entrada)
        n2= re.search('[^/|divor]*$',entrada)
        n11=float(n1.group())
        n22=float(n2.group())
        resultado=round((n11)/(n22),2)
    else:
        resultado = 'Não sei fazer essa conta'
    resultado=str(resultado)
    if resultado.endswith('.0'):
        resultado= resultado.replace ('.0','')
                          
    return resultado
