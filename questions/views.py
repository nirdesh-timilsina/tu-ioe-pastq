from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Subject,Chapter,Question

def home(request):
    subjects = Subject.objects.all().order_by('semester', 'code')

    semesters = {}
    for subject in subjects:
        sem = subject.semester
        if sem not in semesters:
            semesters[sem]= []
        semesters[sem].append(subject)
    return render(request, 'questions/home.html', {'semesters': semesters})
def subject_detail(request, subject_code):
    subject = get_object_or_404(Subject, code=subject_code)
    chapters = subject.chapters.prefetch_related(
        'questions__appearances'
    ).order_by('order')
    return render(request, 'questions/subject.html', {
        
        'subject': subject,
        'chapters': chapters,
    })

def semester_detail(request, semester):
    subjects = Subject.objects.filter(semester=semester).order_by('code')
    return render(request, 'questions/semester.html', {
        'semester': semester,
        'subjects': subjects,
    })
