import pandas as pd
import Comparador

def EstructureData(Productos:  list[list[dict[str:str,int]]]) -> pd.DataFrame:
   DFPrdcts = pd.DataFrame({})
   carset = set({}) 
   valdic = []

   for i in range(len(Productos)):
      for j in range(len(Productos[i])):
         for nmcar,vlcar in Productos[i[j]].items():
            carset.add(nmcar) #Para que no haya columnas repetidas
            valdic[nmcar] = vlcar  #Todos los valores pero aun relacionados a sus nombre de caracteristica
   
   for i in range(len(carset)):
      DFPrdcts[carset[i]] = [v for k,v in valdic.items() if k == carset[i]] #en cada ciclo se crea una columna en el dataframe
      #esta columna recibe el valor de todos los valores de las caracteristicas guardadas que corresponden al nombre de la columna
   return DFPrdcts #Un Dataframe con {nombre:["nam1","nam2"],precio:[1888,2977]}
    
def Compare(Data: pd.DataFrame):
   BaseParams = []
   ComparatFrame = pd.DataFrame()
   counter = 0
   for key,val in Data.items():
       BaseParams.append(val[0])
   
   for key,val in Data.items():
     counter += 1 
     ComparatFrame[key] = [BaseParams[counter] - value for value in Data.values()]

   