from fastapi import FastAPI
import services.FiltrComponentes as FlComp
import services.Parseo as Pars
import pandas as pd
import app.DBComunicator as DBC
import controllers.routes as rts

app = FastAPI(router=rts.router)

def Busq(*args) -> pd.DataFrame:
   Productos:  list[list[dict[str:str,int]]] = Pars.EnvSolicts(args)
   DFPrdcts = FlComp.EstructureData(Productos)
   return DFPrdcts

def VerResults():
   Reporte: pd.Dataframe = pd.read_csv("report.csv")
   return Reporte
   
def WReport(Frame:  pd.Dataframe) -> None:
   Frame.to_csv("report.csv", index=False)

def SavDatos():
   Reporte: pd.Dataframe = pd.read_csv("report.csv")
   DBC.AlmcData(Reporte)
