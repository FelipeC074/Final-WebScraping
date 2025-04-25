from app.repositories.Table_Models import Prdct_Key_Model,Prdct_Value_Model
import pandas as pd
from sqlalchemy.orm import Session


class Product_Repository:
   #db:  Session,Producto_Model:Product_Keys
  def SaveData(self,db:  Session, Data: pd.DataFrame,Prdct_Key_Model:Prdct_Key_Model, Prdct_Val_Model:Prdct_Value_Model) -> None:
    """
    Comunicates with the DB to save data

    Parameters:
    Data (pd.DataFrame): The data to save

    Returns:
    None: 
    """
    keyli = []
    valuli = []
    for i in range(len(Data["price"])):
      for k,v in Data.items():
         keyli.append(k)
         valuli.append(v[i])
    while len(keyli) != 60:
      keyli.append(None)
    while len(valuli) != 60:
      valuli.append(None)
    NewProdK = Prdct_Key_Model(
      key1 = keyli[0],
      key2 = keyli[1],
       key3 = keyli[2],
        key4 = keyli[3],
       key5 = keyli[4],
       key6 = keyli[5],
      key7 = keyli[6],
       key8 = keyli[7],
       key9 = keyli[8],
       key10 = keyli[9],
      key11 = keyli[10],
      key12 = keyli[11],
      key13 = keyli[12],
      key14 = keyli[13],
      key15 = keyli[14],
      key16 = keyli[15],
      key17 = keyli[16],
      key18 = keyli[17],
      key19 = keyli[18],
      key20 = keyli[19],
      key21 = keyli[20],
      key22 = keyli[21],
      key23 = keyli[22],
      key24 = keyli[23],
      key25 = keyli[24],
      key26 = keyli[25],
      key27 = keyli[26],
      key28 = keyli[27],
      key29 = keyli[28],
      key30 = keyli[29],
      key31 = keyli[30],
      key32 = keyli[31],
      key33 = keyli[32],
      key34 = keyli[33],
      key35 = keyli[34],
      key36 = keyli[35],
      key37 = keyli[36],
      key38 = keyli[37],
      key39 = keyli[38],
      key40 = keyli[39],
      key41 = keyli[40],
      key42 = keyli[41],
       key43 = keyli[42],
       key44 = keyli[43],
      key45 = keyli[44],
      key46 = keyli[45],
      key47 = keyli[46],
       key48 = keyli[47],
      key49 = keyli[48],
      key50 = keyli[49],
      key51 = keyli[50],
       key52 = keyli[51],
      key53 = keyli[52],
      key54 = keyli[53],
      key55 = keyli[54],
      key56 = keyli[55],
      key57 = keyli[56],
      key58 = keyli[57],
      key59 = keyli[58],
      key60 = keyli[59]
      )
    db.add(NewProdK)
    db.commit()
    db.refresh(NewProdK)
    NewProdV = Prdct_Val_Model(
     val1 = valuli[0],
     val2 = valuli[1],
     val3 = valuli[2],
     val4 = valuli[3],
     val5 = valuli[4],
     val6 = valuli[5],
     val7 = valuli[6],
     val8 = valuli[7],
     val9 = valuli[8],
     val10 = valuli[9],
     val11 = valuli[10],
     val12 = valuli[11],
     val13 = valuli[12],
     val14 = valuli[13],
     val15 = valuli[14],
     val16 = valuli[15],
     val17 = valuli[16],
     val18 = valuli[17],
     val19 = valuli[18],
     val20 = valuli[19],
     val21 = valuli[20],
     val22 = valuli[21],
     val23 = valuli[22],
     val24 = valuli[23],
     val25 = valuli[24],
     val26 = valuli[25],
     val27 = valuli[26],
     val28 = valuli[27],
     val29 = valuli[28],
     val30 = valuli[29],
     val31 = valuli[30],
     val32 = valuli[31],
     val33 = valuli[32],
     val34 = valuli[33],
     val35 = valuli[34],
     val36 = valuli[35],
     val37 = valuli[36],
     val38 = valuli[37],
     val39 = valuli[38],
     val40 = valuli[39],
     val41 = valuli[40],
     val42 = valuli[41],
     val43 = valuli[42],
      val44 = valuli[43],
     val45 = valuli[44],
     val46 = valuli[45],
     val47 = valuli[46],
     val48 = valuli[47],
     val49 = valuli[48],
     val50 = valuli[49],
     val51 = valuli[50],
     val52 = valuli[51],
     val53 = valuli[52],
     val54 = valuli[53],
     val55 = valuli[54],
      val56 = valuli[55],
      val57 = valuli[56],
      val58 = valuli[57],
      val59 = valuli[58],
      val60 = valuli[59]
    )
    db.add(NewProdV)
    db.commit()
    db.refresh(NewProdV)
    #Puts this in DATABASE

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

  def QData(self,db:  Session, Objts: list[str],Caracs: list[str]):
   KeyCrcs = []
   ValCrcs = []
   for crc in Caracs:
     if " " in crc:
       pospace = crc.find(" ")
       KeyCrcs.append(crc[pospace:])
       ValCrcs.append(crc[:pospace])
     else:
       KeyCrcs.append(crc)
       ValCrcs.append(crc)
  
   Product_Kys = db.query(Prdct_Key_Model).filter(
Prdct_Key_Model.key0.in_(KeyCrcs),
Prdct_Key_Model.key1.in_(KeyCrcs),
Prdct_Key_Model.key2.in_(KeyCrcs),
Prdct_Key_Model.key3.in_(KeyCrcs),
Prdct_Key_Model.key4.in_(KeyCrcs),
Prdct_Key_Model.key5.in_(KeyCrcs),
Prdct_Key_Model.key6.in_(KeyCrcs),
Prdct_Key_Model.key7.in_(KeyCrcs),
Prdct_Key_Model.key8.in_(KeyCrcs),
Prdct_Key_Model.key9.in_(KeyCrcs),
Prdct_Key_Model.key10.in_(KeyCrcs),
Prdct_Key_Model.key11.in_(KeyCrcs),
Prdct_Key_Model.key12.in_(KeyCrcs),
Prdct_Key_Model.key13.in_(KeyCrcs),
Prdct_Key_Model.key14.in_(KeyCrcs),
Prdct_Key_Model.key15.in_(KeyCrcs),
Prdct_Key_Model.key16.in_(KeyCrcs),
Prdct_Key_Model.key17.in_(KeyCrcs),
Prdct_Key_Model.key18.in_(KeyCrcs),
Prdct_Key_Model.key19.in_(KeyCrcs),
Prdct_Key_Model.key20.in_(KeyCrcs),
Prdct_Key_Model.key21.in_(KeyCrcs),
Prdct_Key_Model.key22.in_(KeyCrcs),
Prdct_Key_Model.key23.in_(KeyCrcs),
Prdct_Key_Model.key24.in_(KeyCrcs),
Prdct_Key_Model.key25.in_(KeyCrcs),
Prdct_Key_Model.key26.in_(KeyCrcs),
Prdct_Key_Model.key27.in_(KeyCrcs),
Prdct_Key_Model.key28.in_(KeyCrcs),
Prdct_Key_Model.key29.in_(KeyCrcs),
Prdct_Key_Model.key30.in_(KeyCrcs),
Prdct_Key_Model.key31.in_(KeyCrcs),
Prdct_Key_Model.key32.in_(KeyCrcs),
Prdct_Key_Model.key33.in_(KeyCrcs),
Prdct_Key_Model.key34.in_(KeyCrcs),
Prdct_Key_Model.key35.in_(KeyCrcs),
Prdct_Key_Model.key36.in_(KeyCrcs),
Prdct_Key_Model.key37.in_(KeyCrcs),
Prdct_Key_Model.key38.in_(KeyCrcs),
Prdct_Key_Model.key39.in_(KeyCrcs),
Prdct_Key_Model.key40.in_(KeyCrcs),
Prdct_Key_Model.key41.in_(KeyCrcs),
Prdct_Key_Model.key42.in_(KeyCrcs),
Prdct_Key_Model.key43.in_(KeyCrcs),
Prdct_Key_Model.key44.in_(KeyCrcs),
Prdct_Key_Model.key45.in_(KeyCrcs),
Prdct_Key_Model.key46.in_(KeyCrcs),
Prdct_Key_Model.key47.in_(KeyCrcs),
Prdct_Key_Model.key48.in_(KeyCrcs),
Prdct_Key_Model.key49.in_(KeyCrcs),
Prdct_Key_Model.key50.in_(KeyCrcs),
Prdct_Key_Model.key51.in_(KeyCrcs),
Prdct_Key_Model.key52.in_(KeyCrcs),
Prdct_Key_Model.key53.in_(KeyCrcs),
Prdct_Key_Model.key54.in_(KeyCrcs),
Prdct_Key_Model.key55.in_(KeyCrcs),
Prdct_Key_Model.key56.in_(KeyCrcs),
Prdct_Key_Model.key57.in_(KeyCrcs),
Prdct_Key_Model.key58.in_(KeyCrcs),
Prdct_Key_Model.key59.in_(KeyCrcs)
   )
   Product_Vals = db.query(Prdct_Value_Model).filter(
    Prdct_Value_Model.val0.in_(ValCrcs),
Prdct_Value_Model.val1.in_(ValCrcs),
Prdct_Value_Model.val2.in_(ValCrcs),
Prdct_Value_Model.val3.in_(ValCrcs),
Prdct_Value_Model.val4.in_(ValCrcs),
Prdct_Value_Model.val5.in_(ValCrcs),
Prdct_Value_Model.val6.in_(ValCrcs),
Prdct_Value_Model.val7.in_(ValCrcs),
Prdct_Value_Model.val8.in_(ValCrcs),
Prdct_Value_Model.val9.in_(ValCrcs),
Prdct_Value_Model.val10.in_(ValCrcs),
Prdct_Value_Model.val11.in_(ValCrcs),
Prdct_Value_Model.val12.in_(ValCrcs),
Prdct_Value_Model.val13.in_(ValCrcs),
Prdct_Value_Model.val14.in_(ValCrcs),
Prdct_Value_Model.val15.in_(ValCrcs),
Prdct_Value_Model.val16.in_(ValCrcs),
Prdct_Value_Model.val17.in_(ValCrcs),
Prdct_Value_Model.val18.in_(ValCrcs),
Prdct_Value_Model.val19.in_(ValCrcs),
Prdct_Value_Model.val20.in_(ValCrcs),
Prdct_Value_Model.val21.in_(ValCrcs),
Prdct_Value_Model.val22.in_(ValCrcs),
Prdct_Value_Model.val23.in_(ValCrcs),
Prdct_Value_Model.val24.in_(ValCrcs),
Prdct_Value_Model.val25.in_(ValCrcs),
Prdct_Value_Model.val26.in_(ValCrcs),
Prdct_Value_Model.val27.in_(ValCrcs),
Prdct_Value_Model.val28.in_(ValCrcs),
Prdct_Value_Model.val29.in_(ValCrcs),
Prdct_Value_Model.val30.in_(ValCrcs),
Prdct_Value_Model.val31.in_(ValCrcs),
Prdct_Value_Model.val32.in_(ValCrcs),
Prdct_Value_Model.val33.in_(ValCrcs),
Prdct_Value_Model.val34.in_(ValCrcs),
Prdct_Value_Model.val35.in_(ValCrcs),
Prdct_Value_Model.val36.in_(ValCrcs),
Prdct_Value_Model.val37.in_(ValCrcs),
Prdct_Value_Model.val38.in_(ValCrcs),
Prdct_Value_Model.val39.in_(ValCrcs),
Prdct_Value_Model.val40.in_(ValCrcs),
Prdct_Value_Model.val41.in_(ValCrcs),
Prdct_Value_Model.val42.in_(ValCrcs),
Prdct_Value_Model.val43.in_(ValCrcs),
Prdct_Value_Model.val44.in_(ValCrcs),
Prdct_Value_Model.val45.in_(ValCrcs),
Prdct_Value_Model.val46.in_(ValCrcs),
Prdct_Value_Model.val47.in_(ValCrcs),
Prdct_Value_Model.val48.in_(ValCrcs),
Prdct_Value_Model.val49.in_(ValCrcs),
Prdct_Value_Model.val50.in_(ValCrcs),
Prdct_Value_Model.val51.in_(ValCrcs),
Prdct_Value_Model.val52.in_(ValCrcs),
Prdct_Value_Model.val53.in_(ValCrcs),
Prdct_Value_Model.val54.in_(ValCrcs),
Prdct_Value_Model.val55.in_(ValCrcs),
Prdct_Value_Model.val56.in_(ValCrcs),
Prdct_Value_Model.val57.in_(ValCrcs),
Prdct_Value_Model.val58.in_(ValCrcs),
Prdct_Value_Model.val59.in_(ValCrcs)
   )
   
   