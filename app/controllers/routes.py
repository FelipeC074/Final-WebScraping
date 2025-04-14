from fastapi import APIRouter, HTTPException
from pandas import DataFrame

from app.services import Service as Serv
from app.repositories.Products_Repository import Product_Repository

router = APIRouter()
querycrc = []
queryobj = []

@router.get("/")
def Index():
    return {"Lista de Objetos que quieres ver":queryobj,"Lista de Características que quieres que los objetos tengan":querycrc }

@router.post("/addc/")
def addcarac(qc:  str):
    for el in querycrc:
        for ele in qc:
            if ele == el:
              raise HTTPException(status_code=404,detail="No puede haber 2 iguales")#ERROR que no puede haber dos objetos iguales
    queryobj.append(qc)
    return {"Estas son las características que quieres en tu producto":querycrc}

@router.post("/addo/")
def addobj(qo: list):
    for el in queryobj:
        for ele in qo:
            if ele == el:
              raise HTTPException(status_code=404,detail="No puede haber 2 iguales")#ERROR que no puede haber dos objetos iguales
    queryobj.append(qo)
    return {"Estos son los objetos que quieres":queryobj}

@router.get("/search/{local}")
def search(local:  bool):
    if local:
        LocDat: DataFrame = Serv.QData(queryobj,querycrc)
        Serv.Write(LocDat)
    else:
        queryobj.append(querycrc)
        ProdsData: DataFrame = Serv.EnvSolicts(queryobj)
        queryobj = queryobj[:len(queryobj)-len(querycrc)]#Se separa de nuevo a las listas para no ocasionar problemas

        Serv.Write(ProdsData)
        return ProdsData

@router.get("/compare")
def Compare():
    PrdsComp: DataFrame = Serv.Read()
    ComparatFrame = Serv.Compare(PrdsComp)
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

