import subprocess as sp
from rich import print
import pyfiglet as pg
import time
import os

limpar = 'cls'
os.system(limpar)

banner = pg.figlet_format('Wifi Senha')
print(banner)

while True:
	try:
		info_rede = sp.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp860')
		for x in info_rede.split('\n'):
			if "Todos os Perfis de Usuários:" in x:
				posicao = x.find(':')
				rede = x[posicao+2:]
				print(f"Nome da Rede: [green]{rede}[/]")

		nome_rede = input('\nDigite o nome da Rede Disponível: ')

		info = sp.check_output(["netsh", "wlan", "show", "profiles", nome_rede, "key", "=", "clear" ], encoding='cp860')
		for i in info.split('\n'):
			if "Conteúdo da Chave" in i:
				pos = i.find(':')
				senha = i[pos+2:]
				print(f"\nSenha de {nome_rede}: [green]{senha}[/]\n")
		break

	except:
		os.system(limpar)
		time.sleep(1)
		print('[red]Tente uma rede wifi válida![/]')
		time.sleep(4)
		os.system(limpar)
