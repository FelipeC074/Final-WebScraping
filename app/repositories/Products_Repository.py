from app.repositories.Table_Models import Producto_Model
import pandas as pd
from sqlalchemy.orm import Session


class Product_Repository:
   
  def SaveData(self, Data: pd.DataFrame,db:  Session,Producto_Model:Producto_Model) -> None:
    """
    Comunicates with the DB to save data

    Parameters:
    Data (pd.DataFrame): The data to save

    Returns:
    None: 
    """
    for i in range(len(Data)):
      New_Prod =  Producto_Model(
       name = Data["nombre"][i],
       precio = Data["precio"][i],
       mark = Data["marca"][i]
      )
      db.add(New_Prod)
      db.commit()
      db.refresh(New_Prod)
    #Puts this in DATABASE
  def RepeatRevision(self, Frame: pd.DataFrame) -> pd.DataFrame:
   SavedData: pd.DataFrame= self.QData()

  def ReadReps(self) -> pd.DataFrame:
   Reporte: pd.DataFrame = pd.read_csv("report.csv")
   return Reporte

  def WReport(self, Frame:  pd.DataFrame) -> None:
   """
   Writes in .csv file and stores the Dataframe in DB

   Parameters:
   Frame (pd.Dataframe): The Data to write and save

   Returns:
   None: Because it is only a procedure
   """
   Frame.to_csv("report.csv", index=False)
   NRepsFrame = self.RepeatRevision(Frame)
   self.SaveData(NRepsFrame)

  def QData(self,db:Session, Objts: list[str],Caracs: list[str]):
   #Products = db.query(Producto_Model).filter(typobj in Objts)
   #msdvo = 
   pass
   