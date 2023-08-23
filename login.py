import json

loginID = {
    "len": 2,
    100001: ["admin", "1234"],
    100002: ["ccalvin731@gmail.com", "Chris@2105"],
}


class Login:
    def __init__(self, username, password) -> bool:
        self.username = username
        self.password = password
        return self.verify()

    def verify(self) -> bool:
        for key, value in loginID:
            if value[0] == self.username and value[1] == self.password:
                return True
        else:
            return False

    def dump(self, x) -> None:
        json.dump(loginID, "loginDetails.json")
        json.dump(x, "loginDetails.json")


class Register:
    def __init__(self, username, password1, password2) -> bool:
        self.username = username
        self.password1 = password1
        self.password2 = password2
        if password1 != password2:
            return False
        else:
            f = open("loginDetails.json")
            data = json.load(f)
            data["len"] += 1
            data[str(100000 + data["len"])] = [username, password1]
            Login.dump(data)
            return True
