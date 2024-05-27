from django.shortcuts import redirect, render
from .models import Questions

# Create( your views here.
def home(request):
    questions = Questions.objects.all()
    return render(
        request,
        'poll/home.html',
        {
            "questions":questions
        })


def vote(request, q_id):
    q = get_object_or_404(Questions, pk=q_id)
    if request.method == "POST":
        choice_id = request.POST.get('choice')
        choice = q.choice_set.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('poll:result', q_id)
    return render(request, 'poll/vote.html', {
        "question": q
    })

def result(request, q_id):
    try:
        q = Questions.objects.get(pk=q_id)
    except Questions.DoesNotExist:
        return redirect('poll:home')
    return render(request, 'poll/result.html', {
        "question": q
    })