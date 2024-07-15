from sqlalchemy import create_engine, Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Table d'association pour les relations plusieurs-à-plusieurs entre livres et catégories
book_category = Table('book_category', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    stock = Column(Integer)
    upc = Column(String)
    price = Column(Float)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship('Author', back_populates='books')
    categories = relationship('Category', secondary=book_category, back_populates='books')

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship('Book', back_populates='author')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship('Book', secondary=book_category, back_populates='categories')

# Créer la base de données et les tables
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)

# Créer une session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()
