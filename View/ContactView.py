from os import system
from Controllers.ContactController import ContactController
from Model.DTO.ContactForDelete import ContactForDelete
from Model.DTO.ContactForUpdate import ContactForUpdate
from Model.DTO.UserForView import UserForView


class ContactView:
    def __init__(self, user):
        self.user_logged = user

    def Menu(self):
        while True:
            system("clear")
            print(" Menu de contactos ".center(50, "#"))
            print("1 - Lista de contactos")
            print("2 - Lista de todos los contactos que poseen una cuenta de Instagram")
            print("3 - Agregar contacto")
            print("4 - Editar contacto")
            print("5 - Eliminar contacto")
            print("6 - Cerrar sesion de usuario")
            print("-" * 50)
            option = input("Ingrese una opcion:")
            if option == "1":
                self.listContacts()
            elif option == "2":
                self.listContactsWithIg()
            elif option == "3":
                self.addContact()
            elif option == "4":
                self.editContact()
            elif option == "5":
                self.deleteContact()
            elif option == "6":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))

    def listContacts(self):
        system("clear")
        print(" Lista de contactos ".center(50, "#"))
        contactC = ContactController()
        contacts = contactC.get_contacts_by_user(self.user_logged.username)
        for contact in contacts:
            print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def listContactsWithIg(self):
        system("clear")
        print(" Lista de contactos que poseen Instagram".center(50, "#"))
        contactC = ContactController()
        contacts = contactC.get_contacts_with_ig_by_user(self.user_logged.username)
        for contact in contacts:
            print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def addContact(self):
        system("clear")
        print(" Alta de contacto ".center(50, "!"))
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        instagram_user = input("Ingrese el Instagram del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.add_contact(ContactForUpdate(0, name, surname, email, instagram_user, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))

    def editContact(self):
        system("clear")
        print(" Editar contacto ".center(50, "#"))
        print("-"*50)
        id = input("Ingrese el id del contacto a editar: ")
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        instagram_user = input("Ingrese el Instagram del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.update_contact(ContactForUpdate(id, name, surname, email, instagram_user, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))

    def deleteContact(self):
        system("clear")
        print(" Eliminar contacto ".center(50, "!"))
        print("-"*50)
        id = input("Ingrese el id del contacto a eliminar: ")
        print("-"*50)
        contactC = ContactController()
        contactC.delete_contact(ContactForDelete(id, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))
