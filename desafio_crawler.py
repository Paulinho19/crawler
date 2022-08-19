import pyautogui as p
import time as t
import json

'''comandos para chegar à página desejada'''
p.press('win')
t.sleep(3)
p.write('Google Chrome')
t.sleep(3)
p.press('enter')
t.sleep(17)
p.write('https://www.tripadvisor.com.br/')
t.sleep(3)
p.press('enter')
t.sleep(17)
p.click(x=1062, y=623)
t.sleep(3)
p.write('Congresso Nacional - Brasilia')
t.sleep(4)
p.click(x=949, y=702)
t.sleep(6)
p.click(x=507, y=516)
t.sleep(8)
p.click(x=600, y=186)
t.sleep(4)
p.click(x=408, y=341)
t.sleep(2)
p.dragTo(584,343,2.4,button='left')
t.sleep(4)
p.hotkey('alt','f4')
t.sleep(2)
'''fim do comando de automação'''

'''carrega o arquivo ".json", que possui as informações coletadas da web
   e as imprime no terminal juntamente com uma mensagem'''
with open(r'D:\Programas\Crawler\notas_e_avaliacao.json', encoding='utf-8') as meu_json: 
  dados =  json.load(meu_json)
avaliacao = dados[0]['nota']
n_avaliacao = dados[0]['n_avaliacao']
print('## Resultado da coleta de dados ##')
print('Avaliação do local:',avaliacao,'de',n_avaliacao)



