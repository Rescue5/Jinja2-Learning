from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)

template = env.get_template('имненованные блоки.j2')

output = template.render()
print(output)
