from fastapi import APIRouter

router = APIRouter()
querycrc = []
queryobj = []

@router.get("/")
def ppal_page():
    return {"message":"principal_page"}

@router.post("/addc/{carac}")
def addcarac(carac: str):
    querycrc.append(carac)
    return {"correct":"yes"}

@router.post("/addo/{obj}")
def addobj(obj: str):
    queryobj.append(obj)
    return {"correct":"yes"}

@router.get("/search/{local}")
def search(local:  bool):
    if local:
        pass
    else:
        pass