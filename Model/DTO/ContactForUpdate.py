class ContactForUpdate:
    id = 0
    name = ""
    surname = ""
    email = ""
    username = ""
    instagram_user = ""
    state = 1

    def __init__(self, id, name, surname, email, instagram_user, username) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.instagram_user = instagram_user
        self.state = 1
