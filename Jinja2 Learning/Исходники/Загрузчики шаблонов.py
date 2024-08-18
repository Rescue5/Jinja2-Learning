from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": 'Данил', 'old': 20, "weight": 55.3},
    {"name": 'Николай', 'old': 28, "weight": 82.5},
    {"name": 'Иван', 'old': 33, "weight": 94.0},
]

file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.htm')
msg = tm.render(users=persons)

print(msg)
