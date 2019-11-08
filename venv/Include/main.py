import requests
import time
import hashlib

url_catalogo = "catalogo/"
url_hash = "catalogo/hash/"


def interpret_page(url):
    path = "http://3.80.244.15:8080/"
    r = requests.get(url=path + url)
    s = ""
    list = []

    if url == "catalogo/":
        for chunk in r.iter_content(chunk_size=1):
            if chunk == b'.' or chunk == b'0' or chunk == b'1' or chunk == b'2' or chunk == b'3' or chunk == b'4' or chunk == b'5' or chunk == b'6' or chunk == b'7' or chunk == b'8' or chunk == b'9':
                s += chunk.decode("utf-8")
        i = 1
        for x in range(len(s)):
            inicial = 4 * i + x
            if s[inicial:inicial + 4].isdigit():
                list.append(s[inicial:inicial + 4])
            i += 1
    else:
        f = r.text.split("<body>")[1].split("</body>")[0]
        list = [x for x in f if x.isalnum()]
    return list


def probar():
    hash_paginaWeb = str(hashlib.md5(str.encode("".join(interpret_page(url_catalogo)))).hexdigest())
    hash_back = "".join(interpret_page(url_hash))

    return True if hash_back == hash_paginaWeb else False

v = True
aux = "w"
while(v):
    hora = time.strftime("%H:%M:%S")
    dia = time.strftime("%d/%m/%y")
    f = open('log.txt',aux)
    if(probar()):
        print(dia + " " + hora + " Prueba de Integridad: no hay adulteración en los precios del catálogo :) ")
        f.write(dia + " " + hora + " Prueba de Integridad: no hay adulteración en los precios del catálogo :)"+'\n')
    else:
        f.write(dia + " " + hora + " Prueba de Integridad: ERROR hay adulteración en los precios del catálogo" + '\n')
        print(dia + " " + hora + " Prueba de Integridad: ERROR hay adulteración en los precios del catálogo")
        v = False
    f.close()
    aux = 'a'
    time.sleep(5)
