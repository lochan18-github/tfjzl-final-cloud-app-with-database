from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission, Course


def show_exam_result(request):
    # Dummy course (since no real DB)
    course = Course(name="Sample Course")

    questions = Question.objects.all()
    selected_ids = []

    total_score = 0
    possible_score = 0

    for question in questions:
        possible_score += 1

        # simulate selected choice (just take first correct)
        correct_choice = Choice.objects.filter(question=question, is_correct=True).first()

        if correct_choice:
            selected_ids.append(correct_choice.id)
            total_score += 1

    # Grade calculation
    if possible_score > 0:
        grade = (total_score / possible_score) * 100
    else:
        grade = 0

    return render(request, "exam_result_bootstrap.html", {
        "course": course,
        "selected_ids": selected_ids,
        "grade": grade,
        "possible": possible_score
    })
