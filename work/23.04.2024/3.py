from urllib.request import urlopen
from PIL import Image

with urlopen('https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-41.jpg') as f:
    Image.open(f).show()