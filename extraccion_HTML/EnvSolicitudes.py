import requests

def SolictML(query=[],url="https://listado.mercadolibre.com.ar/"):
   
   for i in range(len(query)):
      url = url + str(query[i]) + "/"
   headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   Rta = requests.get(url,headers=headers)
   return Rta

def SolicteBay(query[],url="https://www.ebay.com/itm/"):
   urlmodel = ""
   pass


def SolictAm(query=[],url="https://www.amazon.com/"):
   urlmodel = "https://www.amazon.com/s?k=zapatillas+nike+hombre&ref=nav_bb_sb"
   pass

def SolictAlx(query=[],url="https://es.aliexpress.com/item/"):
   urlModel = "https://es.aliexpress.com/w/wholesale-zapatillas-hombre-nike.html?"
   pass