from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import NestedCompleter

from CLIbot.command_parser import RainbowLexer
import datetime
import re
import repository.dml_note as dml

N = 3


class DateIsNotValid(Exception):
    """You cannot add an invalid date"""


class InputError:
    """Клас для виклику помилки при введенні невірного даних"""
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        # except IndexError:
        #     return 'Error! Give me name and phone or birthday please!'
        except KeyError:
            print('Error! Note not found!')
        except ValueError:
            print('Error! Incorrect argument!')
        except DateIsNotValid:
            print('Error! Date is not valid')
        except IndexError:
            print('Error! Incorrect argument!')


class Field:
    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value


class ExecDate(Field):
    def __str__(self) -> str:
        if self.value is None:
            return ' - '
        else:
            return f'{self.value:%d %b %Y}'

    @property
    def value(self) -> datetime.date:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if value is None:
            self.__value = None
        else:
            try:
                self.__value = datetime.datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                try:
                    self.__value = datetime.datetime.strptime(value, '%d.%m.%Y')
                except ValueError:
                    raise DateIsNotValid


@InputError
def add_note(*args):
    """Додає нотатку"""
    note_text = ' '.join(args)
    dml.add_note(note_text)
    print('Successful add note')


@InputError
def change_note(*args):
    id_note, new_text = int(args[0]), ' '.join(args[1:])
    dml.change_note(id_note, new_text)
    print(f'Successful change text in note {id_note}')


@InputError
def del_note(*args):
    id_note = int(args[0])
    yes_no = input(f'Are you sure you want to delete the note ID:{id_note}? (Y/n) ')
    if yes_no == 'Y':
        dml.del_note(id_note)
        print(f'Successful delete note {id_note}')
    else:
        print('Note not deleted')


@InputError
def add_date(*args):
    """Додає дату нотатки"""
    id_note, exec_date = int(args[0]), args[1]
    dml.add_date(id_note, exec_date)
    print(f'Successful add date to note {id_note}')


def show_all(*args):
    """Повертає всі нотатки"""
    sel = dml.show_all()
    for s in sel:
        print(f'Note id: {s.id}, date: {s.created}, done: {bool(s.done)}\n'
              f'Text: {s.description}\n'
              f'Tags: {[i.tag for i in s.tags]}\n'
              f'---------------------------------------------------------\n')


def show_archive(*args):
    """Повертає нотатки з архіву"""
    sel = dml.show_archived()
    for s in sel:
        print(f'Note id: {s.id}, date: {s.transferred}, tag: {s.tag}\n'
              f'Text: {s.description}\n'
              f'---------------------------------------------------------\n')


def find_note(*args):
    """Повертає нотатки за входженням в текст"""
    sel = dml.find_note()
    som_st = ' '.join(args)
    for s in sel:
        created = s.created.strftime("%Y-%m-%d %H:%M:%S")
        if som_st in s.description or som_st in created:
            print(f'Note: {s.id}, description: {s.description}, created: {s.created}')


@InputError
def show_date(*args):
    """Повертає нотатки з вказаною датою виконання"""
    date_find = ExecDate(args[0])
    if len(args) > 1:
        days = int(args[1])
    else:
        days = 0
    date1 = (date_find.value - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    date2 = (date_find.value + datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    dml.show_date(ExecDate(date1), ExecDate(date2))


@InputError
def done_note(*args):
    """Помічає нотатку як виконану"""
    id_note = int(args[0])
    dml.done_note(id_note)


@InputError
def return_note(*args):
    """Помічає нотатку як виконану"""
    id_note = int(args[0])
    dml.return_note(id_note)
    print(f'Note with id {id_note} return successful')


@InputError
def add_tag(*args):
    id_note = int(args[0])
    note_tags = re.sub(r'[;,.!?]', ' ', ' '.join(args[1:])).title().split()
    dml.add_tag(id_note, note_tags)
    print(f'Tag/s added successfully to note with id {id_note}')


@InputError
def find_tag(*args):
    """Повертає нотатки в яких є тег"""
    dml.find_tag(args)


def goodbye(*args):
    print('You have finished working with notebook0')


def unknown_command(*args):
    print('Unknown command! Enter again!')


def help_me(*args):
    """Повертає допомогу по списку команд"""
    print("""\nCommand format:
    help or ? - this help;
    add note <text> - add note;
    change note <id> <text> - change note;
    delete note <id> - delete note;
    add date <id> <date> - add/change date;
    add tag <id> <tag> - add tag;
    done <id> - mark note as done;
    return <id> - mark note as not done;
    show all - show all notes;
    show archived - show archived notes;
    show date <date> [<days>] - show notes by date +- days;
    find note <text> - find note by text;
    find tag <text> - find note by tag;
    good bye or close or exit or . - exit the program""")


COMMANDS = {help_me: ['?', 'help'], goodbye: ['good bye', 'close', 'exit', '.'], add_note: ['add note '],
            add_date: ['add date '], show_all: ['show all'], show_archive: ['show archived'],
            change_note: ['change note '], del_note: ['delete note '], find_note: ['find note '],
            show_date: ['show date '], done_note: ['done '], return_note: ['return '], add_tag: ["add tag"],
            find_tag: ["find tag"]}


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def start_nb():
    print('\n\033[033mWelcome to notebook!\033[0m')
    print(f"\033[032mType command or '?' for help \033[0m\n")
    while True:
        with open("history.txt", "wb"):
            pass
        user_command = prompt('Enter command >>> ',
                              history=FileHistory('history.txt'),
                              auto_suggest=AutoSuggestFromHistory(),
                              completer=Completer,
                              lexer=RainbowLexer()
                              )
        command, data = command_parser(user_command)
        command(*data)
        if command is goodbye:
            break


Completer = NestedCompleter.from_nested_dict({'help': None, 'good bye': None, 'exit': None,
                                              'close': None, '?': None, '.': None,
                                              'add': {'note': None, 'date': None, 'tag': None},
                                              'show': {'all': None, 'archived': None, 'date': None},
                                              'change note': None, 'delete note': None,
                                              'find': {'note': None, 'tag': None}, 'done': None,
                                              'return': None})


if __name__ == '__main__':
    start_nb()
