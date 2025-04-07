from fastapi import APIRouter, HTTPException
from pandas import DataFrame

from app.services import Parseo, FiltrComponentes as FLComp
from app.repositories import DBComunicator as DBC

router = APIRouter()
querycrc = []
queryobj = []

@router.get("/")
def Index():
    return {"Lista de Objetos que quieres ver":queryobj,"Lista de Características que quieres que los objetos tengan":querycrc }

@router.post("/addc/")
def addcarac(qc:  list):
    for el in querycrc:
        for ele in qc:
            if ele == el:
              raise HTTPException()#ERROR que no puede haber dos objetos iguales
    queryobj.append(qc)
    return {"Estas son las características que quieres en tu producto":querycrc}

@router.post("/addo/")
def addobj(qo: list):
    for el in queryobj:
        for ele in qo:
            if ele == el:
              raise HTTPException()#ERROR que no puede haber dos objetos iguales
    queryobj.append(qo)
    return {"Estos son los objetos que quieres":queryobj}

@router.get("/search/{local}")
def search(local:  bool):
    if local:
        LocDat: DataFrame = DBC.QData(queryobj,querycrc)
        DBC.WReport(LocDat)
    else:
        queryobj.append(querycrc)
        ParsDat: list[list[dict]] = Parseo.EnvSolicts(queryobj)
        queryobj = queryobj[:len(queryobj)-len(querycrc)]#Se separa de nuevo a las listas para no ocasionar problemas

        DFProds: DataFrame = FLComp.EstructureData(ParsDat)
        DBC.WReport(DFProds)
        return DFProds

@router.get("/compare")
def Compare():
    PrdsComp: DataFrame = DBC.ReadRep()
    ComparatFrame = FLComp.Compare(PrdsComp)
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

