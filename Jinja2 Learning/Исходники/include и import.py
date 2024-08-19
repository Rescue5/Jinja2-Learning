from jinja2 import Environment, FileSystemLoader


persons = [
    {"name": 'Данил', 'old': 20, "weight": 55.3},
    {"name": 'Николай', 'old': 28, "weight": 82.5},
    {"name": 'Иван', 'old': 33, "weight": 94.0},
]


main_loader = FileSystemLoader('../templates')
env = Environment(loader=main_loader)

template = env.get_template('main.j2')
print(template.render(users=persons))
