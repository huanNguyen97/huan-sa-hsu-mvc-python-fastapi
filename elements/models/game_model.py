# Import from orms
from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.orm import relationship

# Import from owner
from database.dbConfig import Base


class GameModel(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    brand = Column(String, index=True)
    year_released = Column(String, index=True)
    price = Column(Float, index=True)

    def __init__(self, id, name, category, brand, year_released, price):
        self.id = id
        self.name = name
        self.category = category
        self.brand = brand
        self.year_released = year_released
        self.price = price