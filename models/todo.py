from beanie import Document
import pymongo

class Todo(Document):
    title: str
    description: str

    class Settings():
        name = "todos"
        indexes = [
            [
                ("name", pymongo.TEXT),
                ("description", pymongo.TEXT)
            ]
        ]