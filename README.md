## Project Documentation for 'Personal Assistant' developed by ‘Dreamteam’.

### The 'Free Personal Assistant' works in three modes:
1. Creating of ‘CONTACT BOOK’ that stores names, addresses, phones, emails and birthdates and implements 
   some useful search commands such as ‘show’, ‘find’ and ‘change’.
2. ‘NOTEBOOK’. You can create simple text notes with tags and search-ability and safe for your future plans.
3. ‘CLEANER FOLDER’ that sorts files out by their types.

In the ‘CONTACT BOOK’ mode, user of the 'Personal Assistant' can do the following.

•	Bot will help you to find command by proposing you command starting with letter you will type.

•	Add contact by command ‘add cnt’ – assistant will ask you to fill following field step by step.

•	You can find contact with command ‘find cnt’ and Name of contact you want to find and see information with name, 
    phone and birthday.
•	You can edit contact with command ‘edit cnt’ and Name of contact you want to edit step by step at following fields.

•	You can delete contact with command ‘del cnt’ and Name of contact you want to delete.

•	For showing all contact information use command ‘show all’.

•	View contacts whose birthday is within specified period starting from today.

You can overwrite contact without using edit command, just with adding contact which already exist 
with same name but different other information. Bot will ask you about overwriting before changing.

All the phones, emails and dates are verifying for conditional formatting:

•	You can write your phone number starting from ‘0’.

•	Code +38 or 380 adding to your phone automatically.

•	Your contact will be saved in format:

        | Ex. +380XXXXXXXXX for phones,
        | aaa@bbb.cc for emails,
        | DD.MM.YYYY for dates.

In the NOTEBOOK mode, user of the ‘CONTACT BOOK’ can do the following.

•	You can create note by command ‘add note’ – assistant will write all notes you want parsing strings by tapping Enter. 
    When you want to finish use [Meta+Enter] or [Ecs+Enter] combinations.
    
•	Then bot propose you to create some tags for quick search.

•	After saving you will see your note ID which you can also use for quick search.

•	You can edit note with command ‘edit note’ and ID of note you want to edit.

•	You can delete note with command ‘del note’ and ID of note you want to delete.

•	You can find note with command ‘find cnt’ and Tag you use for them, you will see information with note, 
    its ID and following tags.
    
•	For showing all notes with tags and IDs use command ‘show all’.

All date you generate with ‘Personal Assistant' be stored in the files address_book and notes in the folder 
Data in main folder with all script items.
In the ‘CLEANER FOLDER’ mode, user can use the only command 'parse (folder)'.
There will be automatically created folders for images, audio files, videos, documents and archives into the specified folder.
Files of corresponding types will be moved into these folders. 
Current folders structure will be retained. All Cyrillic symbols in the names of the files and folders 
will be transliterated into Latin ones. Files of unknown types are being retained untouched. 
To use this bot, you need simply download setup package with all necessary files from github. 
Package can be installed into system with a console command "python setup.py install". 
After that, you can run the bot using 'start-assistant' command in any place in the command line mode.

### INSTALLATION:
'Personal Assistant' is being distributed in the form of Python package.

You can also do this using our archive from the Dist folder:

        pip install free_assist-1.0.3-py3-none-any.whl

