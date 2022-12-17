from sqlalchemy import Column, Integer, String, DateTime

from database.db import Base, session, engine


class AddressBook(Base):
    __tablename__ = 'contacts'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(75), nullable=False)
    phone = Column('phone', String(50), nullable=True)
    birthday = Column('birthday', DateTime, nullable=True)
    email = Column('email', String(100), nullable=True)
    address = Column('address', String(100), nullable=True)


Base.metadata.create_all(engine)
Base.metadata.bind = engine, session
