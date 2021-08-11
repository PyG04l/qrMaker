from PIL import Image, ImageDraw
import qrcode
import os
import sys

def clean():
	operSist = sys.platform
	if operSist == 'win32':
		return os.system('cls')
	elif operSist == 'linux':
		return os.system('clear')
	else:
		return '¡No se reconoce el sistema operativo!'
		exit()

gen = lambda data: qrcode.make(data)

def saveAndShow(name, img):
	img.save(name)
	img.show()

def qrOnImage(img, url, name):
	ima = Image.open(img)
	qr = qrcode.QRCode(box_size = 10)
	qr.add_data(url)
	qr.make()
	img_qr = qr.make_image()

	pos = (ima.size[0] - img_qr.size[0], ima.size[1] - img_qr.size[1])

	img = ima.paste(img_qr, pos)
	im = ima.save(name)
	ima.show(im)

def menu():
	clean()
	print('1) QR Completo')
	print('2) QR en Imagen')
	print('3) Salir')
	op = input('\nElija opción: ')

	if op == '1':
		data = input('Inserte url: ')
		name = input('Inserte nombre para el QR: ')
		img = gen(data)
		saveAndShow(name, img)

	elif op == '2':
		ima = input('Inserte la ruta absoluta o relativa de la imagen: ')
		url = input('Inserte url: ')
		name = input('Inserte nombre para el QR: ')
		qrOnImage(ima, url, name)

	elif op == '3':		
		clean()
		exit()

	else:
		print('Por favor, elija una opción correcta!')
		menu()


menu()
