import EnvSolicitudes as Solc
from bs4 import BeautifulSoup

def EnvSolicts(*args) -> dict:
    """
    Hace una solicitud a cada los principales sitios de E-Commerce y devuelve su información

    Parameters:
    args: Se envia lo que se quiere buscar

    Returns:
    dict: Información 
    """
    #Mercado Libre
    RtaML = Solc.SolictML(args)
    MLSoup = BeautifulSoup(RtaML.content, "html.parser")
    urlsML = MLSoup.select("a.poly-component__title",limit= 10)
    DataProductsML = ExtctInfoML(urlsML)
    #E-Bay
    RtaeB = Solc.SolicteBay(args)
    eBSoup = BeautifulSoup(RtaeB.content, "html.parser")
    urlseB = eBSoup.select("a.s-item__info clearfix",limit= 10)
    DataProductseB = ExtctInfoeB(urlseB)
    #Amazon
    RtaAm = Solc.SolictAm(args)
    AmSoup = BeautifulSoup(RtaAm.content, "html.parser")
    urlsAm = AmSoup.select("a..a-section a-spacing-small puis-padding-left-small puis-padding-right-small",limit= 10)
    DataProductsAm = ExtctInfoAm(urlsAm)
    #Aliexpress
    RtaAlx = Solc.SolictAlx(args)
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
    for i in range(len(URList)):
        RtaeB = Solc.SolicteBay(url=URList[i.get("href")])
        
def ExtctInfoAm(URList : list):
    for i in range(len(URList)):
        RtaAm = Solc.SolictAm(url=URList[i.get("href")])

def ExtctInfoAlx(URList : list):
    for i in range(len(URList)):
        RtaAlx = Solc.SolictAlx(url=URList[i.get("href")])


print(EnvSolicts("nike","hombre","zapatillas"))