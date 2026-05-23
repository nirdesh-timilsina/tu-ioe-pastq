from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Subject,Chapter,Question

def home(request):
    subjects = Subject.objects.all().order_by('semester', 'code')
    return render(request, 'questions/home.html', {'subjects': subjects})

def subject_detail(request, subject_code):
    subject = get_object_or_404(Subject, code=subject_code)
    chapters = subject.chapters.all().order_by('order')
    return render(request, 'questions/subject.html', {
        'subject': subject,
        'chapters': chapters,
    })