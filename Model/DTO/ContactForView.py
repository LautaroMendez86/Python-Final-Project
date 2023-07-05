class ContactForView:
    id=0
    name = ""
    surname = ""
    email = ""
    username = ""
    instagram_user = ""

    def __init__(self, contact) -> None:
        self.name = contact.name
        self.surname = contact.surname
        self.email = contact.email
        self.username = contact.username
        self.instagram_user = contact.instagram_user
        self.id = contact.id

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Apellido: {self.surname} - Email: {self.email} - Instagram: {self.instagram_user and '@' + self.instagram_user or 'No tiene una cuenta'} - Id: {self.id}"

    
