from django.core.management.base import BaseCommand
from quiz.models import Question, Choice

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Question.objects.all().delete()

        questions_data = [
    {
        'text': 'Who wrote the play "Romeo and Juliet"?',
        'choices': [
            {'text': 'William Shakespeare', 'is_correct': True},
            {'text': 'Charles Dickens', 'is_correct': False},
            {'text': 'Jane Austen', 'is_correct': False},
            {'text': 'Mark Twain', 'is_correct': False}
        ]
    },
    {
        'text': 'What is the largest mammal in the world?',
        'choices': [
            {'text': 'Elephant', 'is_correct': False},
            {'text': 'Blue Whale', 'is_correct': True},
            {'text': 'Giraffe', 'is_correct': False},
            {'text': 'Polar Bear', 'is_correct': False}
        ]
    },
    {
        'text': 'What is the chemical symbol for water?',
        'choices': [
            {'text': 'O2', 'is_correct': False},
            {'text': 'H2O', 'is_correct': True},
            {'text': 'CO2', 'is_correct': False},
            {'text': 'NaCl', 'is_correct': False}
        ]
    },
    {
        'text': 'Which country is home to the Great Barrier Reef?',
        'choices': [
            {'text': 'Australia', 'is_correct': True},
            {'text': 'Brazil', 'is_correct': False},
            {'text': 'South Africa', 'is_correct': False},
            {'text': 'United States', 'is_correct': False}
        ]
    },
    {
        'text': 'In which year did World War II end?',
        'choices': [
            {'text': '1940', 'is_correct': False},
            {'text': '1945', 'is_correct': True},
            {'text': '1950', 'is_correct': False},
            {'text': '1939', 'is_correct': False}
        ]
    },
    {
        'text': 'What is the tallest mountain in the world?',
        'choices': [
            {'text': 'Mount Kilimanjaro', 'is_correct': False},
            {'text': 'Mount Everest', 'is_correct': True},
            {'text': 'K2', 'is_correct': False},
            {'text': 'Mount Fuji', 'is_correct': False}
        ]
    },
    
]

        for q_data in questions_data:
            question = Question.objects.create(text=q_data['text'])
            
            for choice_data in q_data['choices']:
                Choice.objects.create(
                    question=question, 
                    text=choice_data['text'], 
                    is_correct=choice_data['is_correct']
                )
