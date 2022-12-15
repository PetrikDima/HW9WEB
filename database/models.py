from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from database.db import Base, engine, session

association_table = Table(
    "tag_to_notes",
    Base.metadata,
    Column("notes_id", ForeignKey("notes.id")),
    Column("tags_id", ForeignKey("tags.id")),
)


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    phone = Column('Telephone', String(100), nullable=False)
    email = Column('Email', String(100), nullable=True)
    address = Column('Address', String(100), nullable=True)
    birthday = Column('Birthday', Date, nullable=True)


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    text = Column('Text', String(255), nullable=False)
    tags = relationship("Tag", secondary=association_table, back_populates="notes")


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag = Column('Tag', String(255), nullable=False)
    notes = relationship("Note", secondary=association_table, back_populates="tags")


Base.metadata.create_all(engine)
Base.metadata.bind = engine, session
