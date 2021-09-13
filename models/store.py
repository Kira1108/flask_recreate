from db import db
from sqlalchemy import Column, Integer, String, relationship
from .items import ItemModel


class StoreModel(db):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    items = relationship(ItemModel)