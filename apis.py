import requests
import json

URL_PATH = "https://frappe.io/api/method/frappe-library"
x = requests.get(URL_PATH).json()
x = x["message"]

# print(x["message"])
# print(len(x))


class Imports:
    def __init__(self, URL_PATH) -> None:
        self.data = requests.get(URL_PATH).json()

    def list_author(self, author):
        res = []
        for i in self.data:
            v = i["authors"].split("/")
            if author in v:
                res.append(i)
        return res

    def list_average_ratings(self, average_rating):
        res = []
        for i in self.data:
            if average_rating >= float(i["average_rating"]):
                res.append(i)
        return res

    def search_isbn(self, isbn=None, isbn13=None):
        res = []
        if isbn is not None:
            if len(isbn) != 10:
                return "False Entry"
        if isbn13 is not None:
            if len(isbn13) != 13:
                return "False Entry"
        for i in self.data:
            if isbn is not None:
                if i["isbn"] == isbn:
                    res.append(i)
            elif isbn13 is not None:
                if i["isbn13"] == isbn13:
                    res.append(i)
            else:
                continue
        return res

    def search_book_id(self, book_id):
        for i in self.data:
            if i["bookID"] == book_id:
                return i

    def search_publication(self, publisher):
        res = []
        for i in self.data:
            v = i["publisher"].split("/")
            for c in v:
                if c == publisher:
                    res.append(i)
        return res

    def search_languageCode(self, language_code):
        res = []
        for i in self.data:
            if i["language_code"] == language_code:
                res.append(i)
        return res

    def search_title(self, title):
        res = []
        for i in self.data:
            if i["title"].find(title) >= 0:
                res.append(i)
        return res


if __name__ == "__main__":
    # print(Imports.author_import("Lynne Truss"))
    # print(Imports.average_ratings(float("4.15")))
    # print(float("4.15"))
    # print(Imports.search_isbn(isbn13="9789587043648"))
    # print(Imports.search_book_id("39763"))
    # print(Imports.search_publication("Grand Central Life & Style"))
    # print(Imports.search_languageCode("spa"))
    # print(Imports.search_title("Outlander"))
    pass
