from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
import random

from .models import Question, Choice, QuizSession, UserAnswer

@login_required
def start_quiz(request):
    QuizSession.objects.filter(user=request.user).delete()
    
    quiz_session = QuizSession.objects.create(user=request.user)
    
    return redirect('get_question')

@login_required
def get_question(request):

    quiz_session = QuizSession.objects.get(user=request.user)
    
    answered_question_ids = UserAnswer.objects.filter(
        quiz_session=quiz_session
    ).values_list('question_id', flat=True)
    
    available_questions = Question.objects.exclude(id__in=answered_question_ids)
    
    if not available_questions.exists():
        return redirect('quiz_summary')
    

    question = random.choice(available_questions)
    
    question_data = {
        'id': question.id,
        'text': question.text,
        'choices': [
            {'id': choice.id, 'text': choice.text} 
            for choice in question.choices.all()
        ]
    }
    
    return render(request, 'question.html', {'question': question_data})

@login_required
def submit_answer(request):

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        choice_id = request.POST.get('choice_id')
        
        quiz_session = QuizSession.objects.get(user=request.user)
        
        question = Question.objects.get(id=question_id)
        chosen_choice = Choice.objects.get(id=choice_id)
        
        is_correct = chosen_choice.is_correct
        
        UserAnswer.objects.create(
            quiz_session=quiz_session,
            question=question,
            chosen_choice=chosen_choice,
            is_correct=is_correct
        )
        
        quiz_session.total_questions += 1
        if is_correct:
            quiz_session.correct_answers += 1
            print(quiz_session.correct_answers)
        else:
            quiz_session.incorrect_answers += 1
        quiz_session.save()
        
        return redirect('get_question')

@login_required
def quiz_summary(request):

    quiz_session = QuizSession.objects.get(user=request.user)
    
    context = {
        'total_questions': quiz_session.total_questions,
        'correct_answers': quiz_session.correct_answers,
        'incorrect_answers': quiz_session.incorrect_answers
    }
    print(context)
    return render(request, 'summary.html', context)