class Todo:
    def __init__(self, code_id: int, title: str, description: str) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: List[str] = []

    def mark_completed(self) -> None:
        self.completed = True

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self) -> None:
        self.todos: Dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        new_id = len(self.todos) + 1
        new_todo = Todo(code_id=new_id, title=title, description=description)
        self.todos[new_id] = new_todo
        return new_id