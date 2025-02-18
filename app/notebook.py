from datetime import datetime

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










