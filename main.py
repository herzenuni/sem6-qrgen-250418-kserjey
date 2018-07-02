import pyqrcode

url = pyqrcode.create('https://github.com/kserjey')
url.png('url.png', scale=6, module_color="#7D007D")
