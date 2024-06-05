import yfinance as _Fin
import pyperclip
import pyautogui
import webbrowser
from time import sleep

# Variáveis do sistema que são informadas pelo usuário

ticker = input("Digite o código da Ação: ")
dt_inicial = input("Informe a data inicial: ")
dt_final = input("Informe a data final: ")
email_dest = input("Informe o e-mail do destinatário: ")

dados = _Fin.Ticker(ticker).history(start=dt_inicial, end=dt_final)
fechamento = dados.Close
fechamento
fechamento.plot()

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(media)

destinatario = email_dest

assunto = f"Analise de Ações {ticker}"

mensagem = f"""

Saudações

Segue abaixo as análises da ação {ticker} referente ao periodo solicitado {dt_inicial} a {dt_final}:

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minima}
Valor médio: R$ {media}

Atenciosamente,

consultaB3-bot

"""
# Ações do Bot para acessar o gmail e enviar os emails

# configurando a pausa de ação do bot
pyautogui.PAUSE = 5

# abrir navegador no gmail
webbrowser.open("www.gmail.com")
sleep(6)

# clicar no botão de "escrever"
pyautogui.click(x=76, y=203)

# preencher para

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# preencher assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# preencher corpo do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# clicar no botão enviar
pyautogui.click(x=840, y=687)

# fechar a aba
pyautogui.hotkey("ctrl","f4")

print("E-mail enviado com sucesso!!!")