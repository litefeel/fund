#!/usr/bin/env python3
#
import sys
from datetime import datetime
from gzip import decompress
from urllib.request import Request, urlopen

from .function import costtime, die, writefile

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    # "Cache-Control":"no-cache",
    # "Connection":"keep-alive",
    # "Host":"fund.eastmoney.com",
    # "Pragma":"no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    # "Cookie":"gsScrollPos-971=7100; gsScrollPos-67=; st_pvi=50797093597275; st_si=29235781560810; ASP.NET_SessionId=jeegm255jlzzwjewthvx3445; gsScrollPos-947=0; EMFUND0=null; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; _adsame_fullscreen_12706=1; EMFUND9=09-29 10:43:58@#$%u524D%u6D77%u5F00%u6E90%u9F0E%u88D5%u503A%u5238C@%23%24003255; _adsame_fullscreen_14694=1; EMFUND7=09-29 11:01:55@#$%u534E%u5B9D%u6807%u666E%u77F3%u6CB9%u6307%u6570@%23%24162411; EMFUND8=09-29 11:07:08@#$%u62DB%u5546%u4E2D%u8BC1%u767D%u9152%u6307%u6570%u5206%u7EA7@%23%24161725",
}


def download(url, filename=None):
    request = Request(url, headers=HEADERS)
    request.set_proxy('127.0.0.1:1080', 'http')
    with urlopen(request, timeout=20) as response:
        # print(response.geturl())
        info = response.info()
        data = response.read()
        if info['Content-Encoding'] == 'gzip':
            data = decompress(data)
        if filename:
            writefile(filename, data)
        return data
    return None



# --------------- main -----------------
if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else None
    name = sys.argv[2] if len(sys.argv) > 2 else None
    if not url:
        die('must has url')
    if '?v=' not in url:
        url = '{0:s}?v={1:%Y%m%d%H%M%S}'.format(url, datetime.now())
    costtime(lambda: download(url, name))
