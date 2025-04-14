from sqlalchemy import String, Integer, Column, UniqueConstraint
from app.repositories.DataBase import DBase

"""class ObjTable_Model(DBase):
    __tablename__ = "Objetos"

    name = Column(String, unique=True, prymary_key=True)
    type = Column(String)

class Mark_Model(DBase):
    __tablename__ = "Marcas"

    name = Column(String,unique=True,primary_key=True)
    type = Column(String)

class ObjtMark_Model(DBase):
    __tablename__ = "Obj-Marca"
    
    id = Column(Integrer,primary_key=True,index=True)
    markname = Column(String,foreign_key=True)
    objname = Column(String,foreign_key=True)
"""    
class Producto_Model(DBase):
    __tablename__ = "Producto"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    price = Column(Integer)
    mark = Column(String)
    typobj = Column(String)




