# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


pyautogui.PAUSE=1
#botao windows
pyautogui.press("win")
#buscar e entrar no chrome
pyautogui.write('chrome')

pyautogui.press('enter')
#esperar chrome carregar e colocar o link
time.sleep(3)
link='https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

#clicar para entrar no link e clicar na regiao do email
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=796, y=368)#x=796, y=368       x=744, y=422
#EMAIL
pyautogui.write('minuscloth96@gmail.com')
time.sleep(2)
pyautogui.press('tab')

#SENHA
pyautogui.write('1234')
pyautogui.press('enter')

#clicar para cadastrar produtos
pyautogui.click(x=806, y=259)



#Agora devemos importar a tabela para poder add os itens
import pandas


#agr tem que criar uma variavel da tabela
tabela=pandas.read_csv('produtos.csv')
#se a tabela nao estiver na mesma pasta,tem que usar o caminho da pasta,caso contrario,apenas o nome



for linha in tabela.index:
    #clicar para cadastrar produtos
    pyautogui.click(x=806, y=259)
    #do pandas como se fosse x e y
    codigo=tabela.loc[linha,'codigo']
    #codigo
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    pyautogui.write(tabela.loc[linha,'marca'])
    pyautogui.press('tab')
    #tipo
    pyautogui.write(tabela.loc[linha,'tipo'])
    pyautogui.press('tab')
    #categoria
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')
    #preco
    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    #custo
    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')
    #obs
    obs=tabela.loc[linha,'obs']
    #agr tem que fazer o tratamento
    if not pandas.isna(obs):

        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)










