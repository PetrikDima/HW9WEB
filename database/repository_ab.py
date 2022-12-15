from datetime import date
from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_

from database.models import Contact
from database.db import session


class Decorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except NoResultFound:
            print('Not found this command')


@Decorator
def add_record(name: str, phone: str, email: str, address: str, birthday: date):
    ab = Contact(
        name=name,
        phone=phone,
        email=email,
        address=address,
        birthday=birthday
    )
    session.add(ab)
    session.commit()


@Decorator
def remove_record(name):
    session.query(Contact).filter(Contact.name == name).delete()
    print(f'Contact: {name} successful deleted!')
    session.commit()


@Decorator
def clean_records():
    session.query(Contact).all().delete()
    print(f'Contacts successful cleaned')
    session.commit()


@Decorator
def add_email(name, email):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.email = email
    print(f"Successful add email to {name}")


@Decorator
def remove_email(name):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.email = ''
    session.commit()
    print(f"Successful delete email to {name}")


@Decorator
def show_all():
    contacts = session.query(Contact).all()
    for c in contacts:
        print(f'Name: {c.name}\nPhone: {c.phone}\nEmail: {c.email}\nAddress: {c.address}\nBirthday: {c.birthday}\n')


@Decorator
def change_contact(name, old_phone, new_phone):
    contact = session.query(Contact).filter(and_(Contact.name == name, Contact.phone == old_phone))
    contact.phone = new_phone
    session.commit()


@Decorator
def show_all():
    contacts = session.query(Contact).all()
    for c in contacts:
        print(f'Name: {c.name}\nPhone: {c.phone}\nEmail: {c.email}\nAddress: {c.address}\nBirthday: {c.birthday}\n')


@Decorator
def add_address(name, address):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.address = address
    print(f"Successful add address to {name}")


@Decorator
def remove_address(name):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.address = ''
    session.commit()
    print(f"Successful delete address to {name}")


@Decorator
def add_birthday(name, birthday):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.birthday = birthday
    print(f"Successful add email to {name}")


@Decorator
def remove_email(name):
    cnt = session.query(Contact).filter(Contact.name == name).first()
    cnt.email = ''
    session.commit()
    print(f"Successful delete email to {name}")
