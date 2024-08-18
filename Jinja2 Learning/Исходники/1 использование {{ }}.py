from jinja2 import Template


per = {'name': 'Данил', 'age': 20}

tm = Template("Привет, я {{ n['name'] }} и мне {{ n['age'] }} лет!")
msg = tm.render(n=per)

print(msg)
