from django import template

register = template.Library()

@register.assignment_tag
def items_by_date(user, date):
    return user.items.filter(date=date).order_by('created_at')
