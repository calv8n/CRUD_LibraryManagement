import login
import apis
import json
import time

username = input("username: ")
password = input("password: ")
l = login.Login(username, password)
o = open("borrowed.json")
m = json.load(o)
if l:
    f = open("borrowed.json")
    data = json.load(f)
    title = input("title: ")
    author = input("author: ")
    if title != "":
        search_result = apis.Imports.search_title(title=title)
        if search_result == []:
            print("Sorry no books available")
        if search_result in data:
            print("Already Borrowed")
        else:
            option = input(
                """1. to borrow
                   2. not borrow"""
            )
            if option == 1:
                d = {}
                d[search_result["isbn"]] = [time.time(), username]
                json.dump(d, "borrowed.json")

    else:
        search_result = apis.Imports.list_author(author=author)
        if search_result == []:
            print("Sorry no books available")
        if search_result["isbn"] in data:
            print("Already Borrowed")
        else:
            option = input(
                """1. to borrow
                   2. not borrow"""
            )
            if option == 1:
                d = {}
                d[search_result["isbn"]] = [time.time(), username]
                json.dump(d, "borrowed.json")
