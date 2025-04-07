import pandas as pd
import sqlite3 as sql

def AlmcData(Data: pd.DataFrame) -> None:
    """
    Comunicates with the DB to save data

    Parameters:
    Data (pd.DataFrame): The data to save

    Returns:
    None: Because it is only a procedure
    """
    DataReved = RepeatRevision(Data)
    #Puts this in DATABASE
def RepeatRevision(Frame: pd.DataFrame) -> pd.DataFrame:
   pass

def ReadReps() -> pd.DataFrame:
   Reporte: pd.DataFrame = pd.read_csv("report.csv")
   return Reporte

def WReport(Frame:  pd.DataFrame) -> None:
   """
   Writes in .csv file and stores the Dataframe in DB

   Parameters:
   Frame (pd.Dataframe): The Data to write and save

   Returns:
   None: Because it is only a procedure
   """
   Frame.to_csv("report.csv", index=False)
   NRepsFrame = RepeatRevision(Frame)
   AlmcData(NRepsFrame)

def QData(Objts: list[str],Caracs: list[str]):
   pass