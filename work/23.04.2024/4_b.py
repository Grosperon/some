
from base64 import b64decode
from PIL import Image

by_data = b'/proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-41.jpg'
Image.frombytes('RGB', (183,172), b64decode(by_data), decode_name = 'jpeg').show()

