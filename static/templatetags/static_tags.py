from django import template
from pages.models import Page, Preferences

register = template.Library()


@register.inclusion_tag('static/navbar.html', takes_context=True)
def top_menu(context):
    request = context['request']
    pages = Page.objects.filter(visible_in_menu=True)
    return { 'pages': pages, 'current_slug': request.path }

@register.simple_tag
def site_name():
    return Preferences.objects.first().site_name

@register.inclusion_tag('static/footer.html')
def footer():
    pages = Page.objects.filter(visible_in_menu=True)
    return { 'pages': pages }

