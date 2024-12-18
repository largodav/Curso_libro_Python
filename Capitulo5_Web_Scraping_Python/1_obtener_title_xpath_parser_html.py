import re
import requests

from lxml import html

respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

elementos = html.fromstring(respuesta.text)

obtener_text_xpath = elementos.xpath("//title/text()",smart_strings= False)

texto = obtener_text_xpath[0]
print(texto)