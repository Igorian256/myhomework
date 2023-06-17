from django import template

register = template.Library()

bad_words = ['фиг', 'дурак', 'дура', 'алкоголь', 'курить', 'бухать']

@register.filter()
def censor(value):
    if isinstance(value, str):
        for word in value.split():
            if word.capitalize() in bad_words:
                value = value.replace(word, word[0] + '*' * len(word))
    else:
        raise ValueError('custom_filters -> censor -> A string is expected, but a different data type has been entered')
    return value
