from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from database.db import Base, session, engine


association_table = Table(
    "tag_to_notes",
    Base.metadata,
    Column("notes_id", ForeignKey("notes.id")),
    Column("tags_id", ForeignKey("tags.id")),
)


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    done = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
    tags = relationship("Tag", secondary=association_table, back_populates="notes")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag = Column(String(60), nullable=False, unique=True)
    notes = relationship("Note", secondary=association_table, back_populates="tags")


class Archive(Base):
    __tablename__ = "archives"
    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    transferred = Column(DateTime, default=datetime.now())
    tag = Column(String(60), nullable=False)


Base.metadata.create_all(engine)
Base.metadata.bind = engine, session
