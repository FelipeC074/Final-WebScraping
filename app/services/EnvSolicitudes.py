import requests

def SolictML(query=[],url="https://listado.mercadolibre.com.ar/"):
   
   for i in range(len(query)):
      url = url + str(query[i]) + "/"
   headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   
   Rta = requests.get(url,headers=headers)
   if Rta.status_code == 200:
       return Rta
   else:
      return f"Error Peticion{Rta.status_code}"

def SolicteBay(query=[] ,url="https://www.ebay.com/sch/i.html?_nkw="):
   #urlmodel = "https://www.ebay.com/sch/i.html?_nkw=zapatillas+nike+hombre"
   finalparam = ""
   for el in query:
      url += str(el).lower().replace(" ","%20") + "+"
     # print(finalparam)
   url = url[:-1]
   
   
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   params = {"nkw": finalparam}

   Rta = requests.get(url=url)

   if Rta.status_code == 500 or Rta.status_code == 503:
       return f"Error Peticion {Rta.status_code}"
   else:
       return Rta


"""def SolictAm(query=[],url="https://www.amazon.com/s?k="):
   #urlmodel = "https://www.amazon.com/s?k=zapatillas+nike+hombre&ref=nav_bb_sb"
   for el in query:
      url += str(el).lower().replace(" ","") + "+"
     # print(finalparam)
   url = url[:-1]
   
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   params = {"k": "","ref":"nav_bb_sb"}
   url += "&ref=nav_bb_sb"
   
   Rta = requests.get(url,headers=headers,allow_redirects=False)
   if Rta.status_code == 500 or Rta.status_code == 503:
      return f"Error de Peticion, codigo{Rta.status_code}"
   else:
      return Rta"""

def SolictAlx(query=[],url="https://es.aliexpress.com/w/wholesale"):
   #urlModel = "https://es.aliexpress.com/w/wholesale-zapatillas-hombre-nike.html?"
   for i in range(len(query)):
      url = url + str(query[i]) + "-"
   url = url.rstrip("-") 
   url = url + ".html?"

   headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   
   Rta = requests.get(url,headers=headers)
   if Rta.status_code == 200:
       return Rta
   else:
      return f"Error Peticion{Rta.status_code}"

def ConvPricesCons(unOrig: str, unDest: str):
   pass

