import requests
from bs4 import BeautifulSoup as bs4
from concurrent.futures import ThreadPoolExecutor, wait
from requests import get, packages
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colored import fg, bg, attr


data = requests.get('https://es.wikipedia.org/wiki/Elon_Musk')
status = data.status_code
html = data.content

soup = bs4(html, "html.parser")
infobox = soup.find('table', 'infobox biography vcard')
# print(infobox.text)

with open('elon_musk.txt', 'w', encoding='utf-8') as f:
    f.write(infobox.text)

image = soup.find('a', 'image')
print(image.img['src'])



def concurrent_download(self, url, filename, folder, threads):
    self.state_print = self.verde('run')
    self.state = 'run'

    try:
        req = get(url, stream=True, verify=False, headers=self.header, timeout=10, allow_redirects=True)
        self.pesoTotal = int(req.headers['Content-Length'])
        self.file_size_Megas = format(self.pesoTotal / (1024. * 1024.), '.1f')
        self.segmentos = int(float(self.file_size_Megas) / 2)
    except Exception as e:
        if u'Connection aborted' in unicode(e):
            self.NetError = True
            return
        else:
            self.UrlFaill = True
            return

    if not self.segmentos:
        self.segmentos = self.hilos = 1

    self.part = self.pesoTotal / (int(self.segmentos))

    ThreadPoolExecutor(1).submit(self.EstadoDownload)

    self.Lista_Pool2 = []

    executor = ThreadPoolExecutor(max_workers=self.hilos)
    for i in range(self.segmentos):
        while executor._work_queue.qsize() >= self.hilos:
            sleep(0.3)

        if self.abort:
            self.state = 'cancelado'
            self.scan = False
            for i in range(self.contador):
                remove(path.join(self.tmp, self.filename + str(i + 1)))
            break
        start = self.part * i
        end = start + self.part
        self.new_len = 0
        if i == (self.segmentos - 1):
            self.new_len = self.pesoTotal - start
            end = self.pesoTotal

        self.Intentos_Segmentos[self.filename + str(i + 1)] = 0
        pool = executor.submit(self.Handler, start, end, url, self.filename + str(i + 1))
        self.Lista_Pool.append(pool)

    wait(self.Lista_Pool)
    if self.contador == self.segmentos:
        self.finish = True
        self.state_print = self.verde('completo')
        self.state = 'completo'
        self.porcentaje = '100'

        unir = ThreadPoolExecutor(1)
        self.Lista_Pool2.append(unir.submit(self.Concat, self.filename, folder))
        wait(self.Lista_Pool2)
        self.scan = False
        self.is_great()

    else:
        self.scan = False

def is_great(self):
    self.state = 'completo'
    logging.info(self.akua('%s Descargado con Exito!' % (self.filename)))
    logging.info(self.akua('salida:  %s' % (self.pwd)))

def direct_download(self, url, filename, folder):
    self.state_print = self.verde('run')
    self.state = 'run'
    head = self.header.copy()
    if self.basic_authentication:
        head['Authorization'] = self.basic_auth(self.basic_authentication)
    req = get(url, verify=False, stream=True, headers=head, timeout=120, allow_redirects=True)
    self.pesoTotal = int(req.headers['Content-Length'])
    self.file_size_Megas = format(self.pesoTotal / (1024. * 1024.), '.1f')
    ThreadPoolExecutor(1).submit(self.EstadoDownload)
    self.stream_download(req, filename)
    src = path.join(self.tmp, filename)
    dest = path.join(folder, filename)
    move(src, dest)
    self.scan = False
    self.is_great()
