from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_
import models.ab_models as mod
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
def insert_addressbook(name, phone, birthday, emails, address):
    emails_str = ''
    for i in emails:
        emails_str += i.value + ' '
    ab_ = mod.AddressBook(
        name=name.value,
        phone=phone.value,
        birthday=birthday.value,
        email=emails_str,
        address=address.value
    )
    session.add(ab_)
    session.commit()


@Decorator
def remove_all():
    session.query(mod.AddressBook).filter(mod.AddressBook.id != 0).delete()
    session.commit()


@Decorator
def remove_user(name):
    session.query(mod.AddressBook).filter(mod.AddressBook.name == name).delete()
    session.commit()


@Decorator
def add_email(name, email):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    sel.email = email


@Decorator
def show_all():
    users = session.query(mod.AddressBook).all()
    return users


@Decorator
def change_contact(name, old, new):
    old_data = session.query(mod.AddressBook).filter(and_(mod.AddressBook.phone == old, mod.AddressBook.name == name)).one()
    old_data.phone = new
    session.commit()


@Decorator
def show_phone(name):
    user = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    return user.phone


@Decorator
def del_phone(name):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    sel.phone = None
    session.commit()


@Decorator
def add_birthday(name, birthday):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    sel.birthday = birthday
    session.commit()


@Decorator
def find_user(name):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    session.commit()
    return sel.birthday


@Decorator
def del_email(name):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    sel.email = None
    session.commit()


@Decorator
def add_address(name, address):
    sel = session.query(mod.AddressBook).filter(mod.AddressBook.name == name).one()
    sel.address = address


@Decorator
def find_something(som):
    sel = session.query(mod.AddressBook).all()
    som_st = ' '.join(som)
    for s in sel:
        birthday = s.birthday.strftime("%Y-%m-%d")
        if som_st in s.name or som_st in s.phone or som_st in birthday or som_st in s.email or som_st in s.address:
            print(f'User {s.name}, phone: {s.phone}, birthday: {s.birthday}, email: {s.email}, address: {s.address}')
