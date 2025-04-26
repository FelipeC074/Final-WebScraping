from fastapi import APIRouter, HTTPException,Depends
from pandas import DataFrame

from app.repositories.DataBase import Get_DB
from app.services.Service import Services
from sqlalchemy.orm import Session

router = APIRouter()
querycrc = []
queryobj = []
Serv = Services()

@router.get("/")
def Index():
    return {"Lista de Objetos que quieres ver":queryobj,"Lista de Características que quieres que los objetos tengan":querycrc }

@router.post("/addc/")
def addcarac(qc:  str):
    if qc in querycrc:
        raise HTTPException(status_code=404,detail="No puede haber 2 caracteristicas iguales")#ERROR que no puede haber dos objetos iguales
    querycrc.append(qc)
    return {"Estas son las características que quieres en tu producto":querycrc}

@router.post("/addo/")
def addobj(qo: str):
    if qo in queryobj:
        raise HTTPException(status_code=404,detail="No puede haber 2 objetos iguales")#ERROR que no puede haber dos objetos iguales
    queryobj.append(qo)
    return {"Estos son los objetos que quieres":queryobj}

@router.get("/search/{local}")
def search(local:  bool, db: Session = Depends(Get_DB)):
    if local:
        LocDat: DataFrame = Serv.LocalQuery(db,queryobj,querycrc)
        Serv.Write(LocDat)
    else:
        queryobj.append(querycrc)
        ProdsData: DataFrame = Serv.WbScrapp(queryobj)
        for i in range(len(queryobj)):#Se separa de nuevo a las listas para no ocasionar problemas
             if queryobj[i] in querycrc:
                 queryobj.remove(queryobj[i])
        Serv.Write(ProdsData)
        return Serv.Data

@router.get("/compare")
def Compare(excluir_caracs: list[str]):
    exclusionli = ["url"]
    PrdsComp: DataFrame = Serv.Read()
    if len(excluir_caracs) >= 1:
        for i in range(len(excluir_caracs)):
            exclusionli.append(excluir_caracs)
    ComparatFrame = Serv.Compare(PrdsComp,exclusionli)
    return ComparatFrame

@router.delete("/delc/{carac}")
def DCarac(carac: str):
    if carac in querycrc:
        querycrc.remove(carac)
    else:
        HTTPException(status_code=404,detail="Ese parametro no existe")

@router.delete("/delo/{obj}")
def DCarac(obj: str):
    if obj in queryobj:
        queryobj.remove(obj)
    else:
        HTTPException(status_code=404,detail="Ese parametro no existe")

