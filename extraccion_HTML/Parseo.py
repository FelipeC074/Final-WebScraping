import EnvSolicitudes as Solc
from bs4 import BeautifulSoup

def EnvSolicts(querys) -> dict:
    """
    Hace una solicitud a cada los principales sitios de E-Commerce y devuelve su información

    Parameters:
    args: Se envia lo que se quiere buscar

    Returns:
    dict: Información 
    """
    #Mercado Libre
    RtaML = Solc.SolictML(querys)
    MLSoup = BeautifulSoup(RtaML.content, "html.parser")
    urlsML = MLSoup.select("a.poly-component__title",limit= 10)
    DataProductsML = ExtctInfoML(urlsML)
    #E-Bay
    RtaeB = Solc.SolicteBay(querys)
    eBSoup = BeautifulSoup(RtaeB.content, "html.parser")
    urlseB = eBSoup.select("a.s-item__info clearfix",limit= 10)
    DataProductseB = ExtctInfoeB(urlseB)
    #Amazon
    RtaAm = Solc.SolictAm(querys)
    AmSoup = BeautifulSoup(RtaAm.content, "html.parser")
    urlsAm = AmSoup.select("a..a-section a-spacing-small puis-padding-left-small puis-padding-right-small",limit= 10)
    DataProductsAm = ExtctInfoAm(urlsAm)
    #Aliexpress
    RtaAlx = Solc.SolictAlx(querys)
    AlxSoup = BeautifulSoup(RtaeB.content, "html.parser")
    urlsAlx = AlxSoup.select("a.s-item__info clearfix",limit= 10)
    DataProductsAlx = ExtctInfoML(urlseB)
 

    return DataProductsML
    
#Parseo de Producto por producto separado
def ExtctInfoML(URList : list):
    """
    Parameters:
    URList(list): Contiene todas las etiquetas que contienen la url al producto especifico
    """
    Productos = []
    for i in range(len(URList)):
        RtaML = Solc.SolictML(url=URList[i].get("href"))
        ProdSoup = BeautifulSoup(RtaML.content,"html.parser")
        Caracts = {}

        Caracts["url"] = URList[i].get("href")
        Caracts["nombre"] = ProdSoup.select_one("h1.ui-pdp-title").get_text().lower()
        Caracts["precio"] = ProdSoup.select_one("span.andes-money-amount__fraction").get_text()
        Caracts["cuotas"] = ProdSoup.select_one(".ui-pdp-price__subtitles")
        Caracts["color"] = ProdSoup.select("span#picker-label-COLOR_SECONDARY_COLOR")
        Caracts["InfoOpcion"] = ProdSoup.select("div.ui-pdp-variations__picker")
        NmCaracts = ProdSoup.select("div.andes-table__header__container")
        VlCaracts = ProdSoup.select("span.andes-table__column--value")
        for i in range(len(NmCaracts)):
            Caracts[NmCaracts[i]] = VlCaracts[i]

        print(Caracts)
        Productos.append(Caracts)
    return Productos


def ExtctInfoeB(URList : list):
    Productos = []
    for i in range(len(URList)):
        RtaeB = Solc.SolicteBay(url=URList[i].get("href"))
        ProdSoup = BeautifulSoup(RtaeB.content,"html.parser")
        Caracts = {}

        Caracts["url"] = URList[i].get("href")
        Caracts["nombre"] = ProdSoup.select_one(".ux-textspans ux-textspans--BOLD")
        Caracts["precio"] = ProdSoup.select_one(".x-price-approx")
        #Caracts["mediosPago"] = ProdSoup.select(".")
        NmCaracts = ProdSoup.select(".ux-labels-values__labels")
        VlCaracts = ProdSoup.select(".ux-labels-values__values")
        for i in range(len(NmCaracts)):
            Caracts[NmCaracts[i]] = VlCaracts[i]
        
        Productos.append(Caracts)
    return Productos
        
def ExtctInfoAm(URList : list):
    Productos = []
    for i in range(len(URList)):
        RtaAm = Solc.SolictAm(url=URList[i].get("href"))
        ProdSoup = BeautifulSoup(RtaAm.content,"html.parser")
        Caracts = {}

        Caracts["url"] = URList[i].get("href")
        Caracts["nombre"] = ProdSoup.select_one("span#productTitle")
        Caracts["precios"] = ProdSoup.select("span.a-price a-text-price a-size-medium apexPriceToPay")
        NmCaracts = ProdSoup.select("td.a-span3")
        VlCaracts = ProdSoup.select("td.a-span9")
        for i in range(len(NmCaracts)):
            Caracts[NmCaracts[i]] = VlCaracts[i]

        NmCaracts = ProdSoup.select("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(2) > th")
        VlCaracts = ProdSoup.select("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(2) > td")
        for i in range(len(NmCaracts)):
            Caracts[NmCaracts[i]] = VlCaracts[i]

        Productos.append(Caracts)
        
    return Productos
        

def ExtctInfoAlx(URList : list):
    Productos = []
    for i in range(len(URList)):
        RtaAlx = Solc.SolictAlx(url=URList[i].get("href"))
        ProdSoup = BeautifulSoup(RtaAlx.content,"html.parser")
        Caracts = {}

        Caracts["url"] = URList[i].get("href")
        Caracts["nombre"] = ProdSoup.select_one(".title--wrap--UUHae_g")
        Caracts["precio"] = ProdSoup.select_one("div.price--current--I3Zeidd product-price-current")
        NmCaracts = ProdSoup.select(".specification--title--SfH3sA8")
        VlCaracts = ProdSoup.select(".specification--desc--Dxx6W0W")
        for i in range(len(NmCaracts)):
            Caracts[NmCaracts[i]] = VlCaracts[i]

print(EnvSolicts("nike","hombre","zapatillas"))