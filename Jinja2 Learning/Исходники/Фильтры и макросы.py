from jinja2 import Template

# Блок фильтров
# persons = [
#     {"name": 'Данил', 'old': 20, "weight": 55.3},
#     {"name": 'Николай', 'old': 28, "weight": 82.5},
#     {"name": 'Иван', 'old': 33, "weight": 94.0},
# ]
#
# tpl = '''
# {%- for person in persons -%}
# {% filter upper -%}{{person.name}}{%endfilter%}
# {%endfor-%}'''

# Макросы macro
# html ='''
# {%- macro input(name, value='', type='text',size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e}}" size="{{ size }}">
# {%- endmacro -%}
#
# <p>{{ input('username', 'size', type='text', size=30) }}</p>
# <p>{{ input('email', 'mail', type='text') }}</p>
# <p>{{ input('username', 'size', type='text', size=30) }}</p>
# '''

# Вложенный макрос Call
persons = [
    {"name": 'Данил', 'old': 20, "weight": 55.3},
    {"name": 'Николай', 'old': 28, "weight": 82.5},
    {"name": 'Иван', 'old': 33, "weight": 94.0},
]

html = '''
{% macro list_users(list_of_users) %}
<ul>
{% for user in list_of_users -%}
    <li>{{user['name']}}</li> {{caller(user)}}
{% endfor %}
</ul>
{% endmacro %}

{% call(user) list_users(persons) %}
    <ul>
    <li>Age: {{user['old']}}</li>
    <li>Weight: {{user['weight']}}</li>
    </ul>
{% endcall %}
'''

msg = Template(html).render(persons=persons)
print(msg)
