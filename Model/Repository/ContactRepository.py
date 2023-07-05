from ..Entities.Contact import Contact
from ..Context import Context

class ContactRepository:

    def get_contacts_by_user(self, username):
        with Context() as context1:
            query = "SELECT * FROM contact WHERE state = 1 && username = %s "
            values = (username,)
            context1.mycursor.execute(query,values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            contact.instagram_user = contactDB[6]
            contacts.append(contact)
        return contacts
    
    def get_contact(self, contact):
        with Context() as context1:
            query = "SELECT * FROM contact WHERE idcontact = %s"
            values = (contact.id,)
            context1.mycursor.execute(query, values)
            contactDB = context1.mycursor.fetchone()
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            contact.instagram_user = contactDB[6]
        return contact
    
    def add_contact(self, contact):
        with Context() as context1:
            query = "INSERT INTO contact (name, surname, email, username, instagram_user, state) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (contact.name, contact.surname, contact.email, contact.username, contact.instagram_user, contact.state)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            contact.id = context1.mycursor.lastrowid
        return contact

    def update_contact(self, contact):
        print(contact.name, contact.surname, contact.email, contact.id, contact.instagram_user, contact.username)
        with Context() as context1:
            query = "UPDATE contact SET name = %s, surname = %s, email = %s, instagram_user = %s WHERE idcontact = %s AND username = %s"
            values = (contact.name, contact.surname, contact.email, contact.instagram_user, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET state = %s WHERE idcontact = %s AND username = %s"
            values = (0, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
        
