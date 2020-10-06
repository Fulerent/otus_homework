from json import loads, dumps
from csv import DictReader

with open("../data/users.json", "r") as file1:
    users = loads(file1.read())

with open("../data/books.csv", "r") as file2:
    reader = DictReader(file2)

    library = []

    for user in users:
        user_of_library = {'name': user["name"],
                           'gender': user["gender"],
                           'address': user["address"],
                           }
        book = next(reader)
        book_of_library = {"books": [{"title": book["Title"],
                                      "author": book["Author"],
                                      "height": book["Height"],
                                      }]
                           }

        user_of_library.update(book_of_library)
        library.append(user_of_library)
    print(library)

with open("../data/dictionary.json", "w") as fw:
    s = dumps(library, indent=4)
    fw.write(s)
