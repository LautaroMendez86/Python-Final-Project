class Contact:
    id = 0
    name = ""
    surname = ""
    email = ""
    username = ""
    instagram_user = ""
    state = True

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, username={self.username}, instagram_user={self.instagram_user}, state={self.state})"
