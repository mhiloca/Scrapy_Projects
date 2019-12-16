# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class CraiglistSpider(scrapy.Spider):
    name = 'craiglist'
    start_urls = ['https://accounts.craigslist.org/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response=response,
            formxpath="//form[@class='loginform']",
            formdata={"browserinfo": "%7B%0A%09%22plugins%22%3A%20%22Plugin%200%3A%20Chrome%20PDF%20Plugin%3B%20"
                                     "Portable%20Document%20Format%3B%20internal-pdf-viewer%3B%20%28Portable%20D"
                                     "ocument%20Format%3B%20application/x-google-chrome-pdf%3B%20pdf%29.%20Plugin"
                                     "%201%3A%20Chrome%20PDF%20Viewer%3B%20%3B%20mhjfbmdgcfjbbpaeojofohoefgiehjai"
                                     "%3B%20%28%3B%20application/pdf%3B%20pdf%29.%20Plugin%202%3A%20Native%20Client"
                                     "%3B%20%3B%20internal-nacl-plugin%3B%20%28Native%20Client%20Executable%3B%"
                                     "20application/x-nacl%3B%20%29%20%28Portable%20Native%20Client%20Executable%3"
                                     "B%20application/x-pnacl%3B%20%29.%20%22%2C%0A%09%22timezone%22%3A%20180%2C%0"
                                     "A%09%22video%22%3A%20%221920x1080x24%22%2C%0A%09%22supercookies%22%3A%20%"
                                     "22DOM%20localStorage%3A%20Yes%2C%20DOM%20sessionStorage%3A%20Yes%2C%20IE%2"
                                     "0userData%3A%20No%22%0A%7D",
                      "step": "confirmation",
                      "rt": "",
                      "rp": "",
                      "t": "1576500988",
                      "p": "0",
                      "inputEmailHandle": "mhiloca@hotmail.com",
                      "inputPassword": "Malpino9173"},
            callback=self.after_login
         )

    def after_login(self, response):
        yield {
            "resp": response.xpath("//header[@class='account-header']/span/a[2]/text()").extract_first()
        }