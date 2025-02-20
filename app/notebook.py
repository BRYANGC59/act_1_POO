from datetime import datetime
from random import randint

class Note:

    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __int__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if self.tags.count(tag) < 1:
            self.tags.append(tag)

        else:
            return "La etiqueta ya existe"

    def __str__(self,) -> str:
        return f"Date: {self.creation_date} - Title: {self.title} \n {self.text}"


class Notebook:

    def __int__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, important: str):
       code: int = len(self.notes) + 1













