from db import db
from sqlalchemy import Column, ForeignKey, Integer, String, relationship

class ItemModel(db):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship(StoreModel)