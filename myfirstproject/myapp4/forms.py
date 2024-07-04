from django import forms


class RandomGame(forms.Form):
    EVENT_CHOICES = [
        ('coin', 'монетка'),
        ('dice', 'кубики'),
        ('numbers', 'числа'),
    ]

    event_type = forms.ChoiceField(choices=EVENT_CHOICES, label='Выберите игру')
    attempts = forms.IntegerField(min_value=1, max_value=64, label='Количество попыток')
