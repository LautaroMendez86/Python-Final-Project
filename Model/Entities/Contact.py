class Contact:
    id = 0
    name = ""
    surname = ""
    email = ""
    username = ""
    state = True

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, username={self.username}, state={self.state})"
