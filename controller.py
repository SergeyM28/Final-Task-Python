import model

def start():
    print('добро пожаловать в приложение "Заметки"\nЖду команду')
    help()
    model.importAll()
    makeAction(model.getData())

def makeAction(Action): 
    if Action == "help": help()
    elif Action == "printall": model.printAll()
    elif Action == "print": 
        print("введите номер заметки")
        model.printNote(model.searchId(model.getData()))
    elif Action == "add" : model.addNote()
    elif Action == "delete": 
        print("введите номер заметки для удаления")
        model.deleteNoteById(model.getData())
    elif Action == "edit": 
        print("введите номер заметки для редактирования")
        model.editNote(model.getData())
    elif Action == "exit": 
        model.exportAll()
        exit(0)
    else: print("введена неверная команда, попробуйте еще раз")
    makeAction(model.getData())

def help():
    print("help - список команд\n"+
          "printall - посмотерть все заметки\n"+
          "print - посмотреть одну заметку по номеру\n"+
          "add - добавить заметку\n"+
          "delete - удалить заметку по номеру\n"+
          "edit - отредактировать заметку по номеру\n"+
          "exit - сохранить изменения и выйти")
