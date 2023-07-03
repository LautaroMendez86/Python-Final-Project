from Model.DTO.ContactForView import ContactForView
from Model.Repository.ContactRepository import ContactRepository


class ContactController:
    def get_contacts_by_user(self, username):
        contact_repository = ContactRepository()
        contacts = contact_repository.get_contacts_by_user(username)
        contactsForView = []
        for contact in contacts:
            contactForView = ContactForView(contact)
            contactsForView.append(contactForView)
        return contactsForView
    
    def get_contact(self, contact):
        contact_repository = ContactRepository()
        contact = contact_repository.get_contact(contact)
        contactForView = ContactForView(contact)
        return contactForView
    
    def add_contact(self, contact):
        contact_repository = ContactRepository()
        contact.instagram_user = self.format_instagram_user(contact.instagram_user)
        contact_repository.add_contact(contact)

    def update_contact(self, contact):
        contact_repository = ContactRepository()
        contact.instagram_user = self.format_instagram_user(contact.instagram_user)
        contact_repository.update_contact(contact)

    def delete_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.delete_contact(contact)
    
    @staticmethod
    def format_instagram_user(account):
        if account and account.startswith("@"):
            return account[1:]
        return account