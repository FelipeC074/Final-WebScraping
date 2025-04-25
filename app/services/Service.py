import pandas as pd
from app.repositories.Products_Repository import Product_Repository
from app.repositories.Table_Models import Prdct_Key_Model,Prdct_Value_Model
from app.services.Parseo import EnvSolicts
from sqlalchemy.orm import Session

class Services:
   def __init__(self):
     self.Data:  pd.DataFrame = {None:None}
     self.repository: Product_Repository = Product_Repository
   
   def Write(self, NewData: pd.DataFrame):
     self.Data = NewData
   def Read(self):
     return self.Data
   
   def SaveData(self, db:  Session):
     self.repository.SaveData(self.Data,db,Prdct_Key_Model,Prdct_Value_Model)
     
   def LocalQuery(self, db, objli: list[str],crcli: list[str]):
      return self.repository.QData(db,objli,crcli)
   
   def WbScrapp(self,query: list[str]):
      WebProds: list[list[dict[str:str,int]]] = EnvSolicts(query)
      print(type(WebProds))
      DFProds: pd.DataFrame= self.EstructureData(WebProds)
      return DFProds

   """def EstructureData(self, Productos:  list[list[dict[str:str,int]]]) -> pd.DataFrame:
     DFPrdcts = pd.DataFrame({})
     carset: set = set({}) 
     valdic = {}

     for i in range(len(Productos)):
      for j in range(len(Productos[i])):
         #if str(type(i)) != "<class int>":
         for nmcar,vlcar in Productos[i][j].items():
            carset.add(nmcar) #Para que no haya columnas repetidas
            valdic[nmcar] = vlcar  #Todos los valores pero aun relacionados a sus nombre de caracteristica
            
     carset: list = list(carset)
     for i in range(len(carset)):
      DFPrdcts[carset[i]] = [v for k,v in valdic.items() if k == carset[i]] #en cada ciclo se crea una columna en el dataframe
      #esta columna recibe el valor de todos los valores de las caracteristicas guardadas que corresponden al nombre de la columna
     return DFPrdcts #Un Dataframe con {nombre:["nam1","nam2"],precio:[1888,2977]}
    """
   def EstructureData(self, Productos: list[list[dict[str, str | int]]]) -> pd.DataFrame:
    lista_filas = []

    for producto_lista in Productos:
        fila = {}
        for item in producto_lista:
            fila.update(item)
        lista_filas.append(fila)

    df = pd.DataFrame(lista_filas)
    df = df.where(pd.notnull(df), None)

    return df
   
   def Compare(Data: pd.DataFrame):
     BaseParams = []
     ComparatFrame = pd.DataFrame()
     counter = 0
     for key,val in Data.items():
       BaseParams.append(val[0])
   
     for key,val in Data.items():#Solo funciona con valores numericos
       counter += 1 
       ComparatFrame[key] = [BaseParams[counter] - value for value in Data.values()]
     return ComparatFrame
   

   