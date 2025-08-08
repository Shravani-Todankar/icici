from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import PDF, QuizQuestion, QuizResult


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'core/login.html')


@login_required
def dashboard_view(request):
    # Static list ko hatao, real PDF objects lo
    pdfs = PDF.objects.all()
    return render(request, 'core/dashboard.html', {'pdfs': pdfs})


@login_required
def quiz_view(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    questions = QuizQuestion.objects.filter(pdf=pdf)

    if request.method == "POST":
        score = 0
        total = questions.count()

        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_answer:
                score += 1

        # Result save with PDF
        QuizResult.objects.create(user=request.user, pdf=pdf, score=score, total=total)

        return render(request, 'core/result.html', {
            'score': score,
            'total': total,
            'pdf': pdf,
        })

    return render(request, 'core/quiz.html', {
        'questions': questions,
        'pdf': pdf,
    })
