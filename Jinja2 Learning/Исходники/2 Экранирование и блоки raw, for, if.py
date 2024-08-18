from jinja2 import Template

# Класс escape
# from html import escape
# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# msg = escape(link)
# print(msg)

# Блок for и if
cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тольятти'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
<option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}
{% elif %}
id too small
{% endif -%}
{% endfor -%}
</select>'''

# Блок raw
# data = """{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставляет соответствующее значение{% endraw %}"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
