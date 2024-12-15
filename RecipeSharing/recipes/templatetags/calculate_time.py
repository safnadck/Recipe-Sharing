from django import template

register = template.Library()

@register.filter
def calculate_time(value):
    hours = value // 60
    minutes = value % 60
    return f'{hours} hours {minutes} minutes' if hours else f'{minutes} minutes'
