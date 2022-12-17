from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import joinedload

from database.db import session
from models.note_models import Note, Archive, Tag


def add_note(text):
    note = Note(description=text)
    session.add(note)
    session.commit()


def change_note(id_, text):
    sel = session.query(Note).filter(Note.id == id_).one()
    sel.description = text
    session.commit()


def del_note(id_):
    session.query(Note).filter(Note.id == id_).delete()
    session.commit()


def add_date(id_, date):
    sel = session.query(Note).filter(Note.id == id_).one()
    sel.date = date
    session.commit()


def show_all():
    sel = session.query(Note).all()
    return sel


def done_note(id_):
    try:
        session.query(Archive).filter(Archive.id == id_).one()
        print(f'Note with id: {id_} in archives')
    except NoResultFound:
        print('Note not in archives')
    try:
        sel_note = session.query(Note).options(joinedload('tags')).filter(Note.id == id_).one()
        arc = Archive(id=sel_note.id,
                      description=sel_note.description,
                      tag=sel_note.tags)
        print(f'Note with id: {id_} added to archives')
        session.query(Note).filter(Note.id == id_).delete()
        session.add(arc)
        session.commit()
    except NoResultFound:
        print('Note not in notes')


def show_archived():
    sel = session.query(Archive).all()
    return sel


def find_note():
    sel = session.query(Note).all()
    return sel


def return_note(id_):
    sel_arc = session.query(Archive).filter(Archive.id == id_).one()
    print(type(sel_arc.tag))
    note = Note(id=sel_arc.id,
                description=sel_arc.description)
    session.add(note)
    session.query(Archive).filter(Archive.id == id_).delete()
    session.commit()


def add_tag(id_, tags):
    list_tags = []
    for i in tags:
        sel_tag = Tag(id=id_, tag=i)
        list_tags.append(sel_tag)
    note_ = session.query(Note).options(joinedload('tags')).filter(Note.id == id_).one()
    note_.tags = list_tags
    session.add(note_)
    session.commit()


def find_tag(tag):
    notes_ = session.query(Note).options(joinedload('tags')).all()
    for n in notes_:
        for i in n.tags:
            if tag.title() in i.tag:
                print(f'---------------------------------------------------------\n'
                      f'Note id: {n.id}, date: {n.created}, done: {bool(n.done)}\n'
                      f'Text: {n.description}\n'
                      f'Tags: {i.tag}\n'
                      f'---------------------------------------------------------\n')
    session.commit()


def show_date(date1, date2):
    notes_ = session.query(Note).all()
    for n in notes_:
        if date1.value <= n.created <= date2.value:
            print(f'Id: {n.id}, date: {n.created}')
        else:
            print(f'Not find notes with this date')
