# create table products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) UNIQUE NOT NULL,
#     level INTEGER NOT NULL,
#     published BOOLEAN NOT NULL DEFAULT false,
#     created_on TIMESTAMP NOT NULL DEFAULT NOW()
# );
# create table reviews (
#     id SERIAL PRIMARY KEY,
#     product_id INTEGER REFERENCES products(id),
#     rating INTEGER NOT NULL,
#     comment TEXT,
#     created_on TIMESTAMP NOT NULL DEFAULT NOW()
# );

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"    
      
    id = Column(Integer, primary_key=True)    
    name = Column(String, nullable=False)    
    level = Column(Integer, nullable=False)    
    published = Column(Boolean)    
    created_on = Column(TIMESTAMP)    
    reviews = relationship("Review", order_by="Review.rating", back_populates="product")
    
class Review(Base):    
    __tablename__ = "reviews"    
    id = Column(Integer, primary_key=True)    
    product_id = Column(Integer, ForeignKey("products.id"))    
    rating = Column(Integer, nullable=False)    
    comment = Column(Text)    
    created_on = Column(TIMESTAMP)    
    product = relationship("Product", back_populates="reviews")