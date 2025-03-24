import requests

def SolictML(query=[],url="https://listado.mercadolibre.com.ar/"):
   
   for i in range(len(query)):
      url = url + str(query[i]) + "/"
   headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   
   Rta = requests.get(url,headers=headers)
   if Rta.status_code == 200:
       return Rta
   else:
      return "Error Peticion" + {Rta.status_code}

def SolicteBay(query=[] ,url="https://www.ebay.com/sch/i.html?"):
   #urlmodel = "https://www.ebay.com/sch/i.html?_nkw=zapatillas+nike+hombre"
   for i in range(len(query)):
      kparam = query[i] + "+"
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   params = {"_nkw": kparam.rstrip("+")}

   Rta = requests.get(url,headers=headers, params= params)
   if Rta.status_code == 200:
       return Rta
   else:
      return "Error Peticion"+ {Rta.status_code}


def SolictAm(query=[],url="https://www.amazon.com/s?"):
   #urlmodel = "https://www.amazon.com/s?k=zapatillas+nike+hombre&ref=nav_bb_sb"
   for i in range(len(query)):
      kparam = query[i] + "+"
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"}
   params = {"k": kparam.rstrip("+"),"ref":"nav_bb_sb"}

   Rta = requests.get(url,headers=headers, params= params)
   if Rta.status_code == 200:
       return Rta
   else:
      return "Error Peticion"+ {Rta.status_code}

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
      return "Error Peticion"+ {Rta.status_code}