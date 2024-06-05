# %% [markdown]
# # Projeto Consulta de Ações
# 
# Passo a passo do problema
# 
# - Sistema que busca informações de uma Ação da Bolsa de valores de forma automática
# - Criar as análises solicitadas
#     - Cotação Máxima
#     - Cotação Mínima
#     - Valor Médio
# - Enviar um e-mail automaticamente para o gestor

# %% [markdown]
# #### Buscar os dados da ação informada
# 
# Bibliotecas: `yfinance` e `matplotlib`
# 
# Requerido para o sistema:
# 
# `pip install yfinance`
# `pip install matplotlib`

# %%
import yfinance as _Fin

# %%
ticker = input("Digite o código da Ação: ")
dt_inicial = input("Informe a data inicial: ")
dt_final = input("Informe a data final: ")

dados = _Fin.Ticker(ticker).history(start=dt_inicial, end=dt_final)
fechamento = dados.Close
fechamento
fechamento.plot()

# %% [markdown]
# #### Criar as Análises solicitadas
# 
# - Cotação Máxima
# - Cotação Mínima
# - Valor Médio

# %%
fechamento

# %% [markdown]
# Precisamos coletar as informações listadas acima e converter para uma forma mais simples de leitura.
# 
# Usar a função `round()` para converter os valores para uma leitura mais próxima da moeda corrente.

# %%
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(media)


# %% [markdown]
# #### Enviando e-mail de forma automática
# 
# Necessário instalar a biblioteca `pyautogui`
# 
# Comando: `pip install pyautogui`
# 
# As coordenadas utilizadas no código irão variar de acordo com o monitor e a resolução de tela que está sendo utilizado. Código abaixo mapeia a informação necessária.

# %%
import time
import pyautogui

time.sleep(5)

print(pyautogui.position())


# %%
import pyperclip
import pyautogui
import webbrowser
from time import sleep

destinatario = "werdelessoares@gmail.com"
assunto = "Analise de Ações"

mensagem = f"""
Saudações

Segue abaixo as análises da ação {ticker} do periodo solicitado {dt_inicial} a {dt_final}:

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minima}
Valor médio: R$ {media}

Attr

"""
print(fechamento.plot())

# configurando a pausa de ação do bot
pyautogui.PAUSE = 5

# abrir navegador no gmail
webbrowser.open("www.gmail.com")
sleep(3)

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

# preencher assunto
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# clicar no botão enviar
pyautogui.click(x=840, y=687)

# fechar a aba
pyautogui.hotkey("ctrl","f4")

print("E-mail enviado com sucesso!!!")


