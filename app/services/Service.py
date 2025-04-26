import pandas as pd
from app.repositories.Products_Repository import Product_Repository
from app.repositories.Table_Models import Prdct_Key_Model,Prdct_Value_Model
from app.services.Parseo import EnvSolicts
from sqlalchemy.orm import Session
from app.services.Comparador import extraer_numero, TransBool

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
      return self.repository.QData(db=db,Caracs=crcli)
   
   def WbScrapp(self,query: list[str]):
      WebProds: list[list[dict[str:str,int]]] = EnvSolicts(query)
      DFProds: pd.DataFrame= self.EstructureData(WebProds)
      return DFProds

   def EstructureData(self, Productos: list[list[dict[str, str | int]]]) -> pd.DataFrame:
      lista_filas = []

      for sublista in Productos:
        for producto in sublista:
            if isinstance(producto, dict):
                lista_filas.append(producto)

      if not lista_filas:
        print("No se detectaron productos en la entrada.")
        raise pd.DataFrame()

      df = pd.DataFrame(lista_filas)
      df = df.where(pd.notnull(df), None)  # Para evitar errores de JSON con NaN
      return df
   
   def Compare(df: pd.DataFrame, columnas_excluir=["url"]) -> pd.DataFrame:
    # Eliminar columnas irrelevantes
    columnas_excluir = [col for col in columnas_excluir if col in df.columns]
    df_filtrado = df.drop(columns=columnas_excluir)

    datos_comparativos = {}

    for columna in df_filtrado.columns:
        col_data = df_filtrado[columna]

        valores_numericos = [extraer_numero(valor) for valor in col_data]
        tiene_numeros = any(val is not None for val in valores_numericos)

        if tiene_numeros:
            datos_comparativos[columna + " (num)"] = valores_numericos
            continue  # Ya lo procesamos


        valores_bool = [TransBool(valor) for valor in col_data]
        tiene_booleanos = any(val is not None for val in valores_bool)

        if tiene_booleanos:
            datos_comparativos[columna + " (bool)"] = valores_bool
            continue

        datos_comparativos[columna] = list(col_data)

    return pd.DataFrame(datos_comparativos)