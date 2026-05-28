import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from questions.models import Subject, Chapter,Question,Appearance

SUBJECTS = [
    
     {
        'file': 'computer_networks.json',
        'code': 'ENCT304',
        'name': 'Computer Networks',
        'semester': 5
    },
    {
        'file': 'computer_organization_architecture.json',
        'code': 'ENCT303',
        'name': 'Computer Organization & Architecture',
        'semester': 5
    },
    {
        'file': 'probability_statistics.json',
        'code': 'ENSH304',
        'name': 'Probability & Statistics',
        'semester': 5
    },
    {
        'file': 'database_management_system.json',
        'code': 'ENCT301',
        'name': 'Database Management System',
        'semester': 5
    },
    {
        'file': 'web_application_programming.json',
        'code': 'ENCT302',
        'name': 'Web Application Programming',
        'semester': 5
    },
    {
        'file': 'compiler_design.json',
        'code': 'ENCT326',
        'name': 'Compiler Design',
        'semester': 5
    },
    {
        'file': 'advanced_python_data_science.json',
        'code': 'ENCT325',
        'name': 'Advanced Python for Data Science',
        'semester': 5
    },
    
    {
        'file' : 'artificial_intelligence.json',
        'code' : 'ENCT351',
        'name' : 'Artificial Intelligence',
        'semester':6
    },
    {
        'file' : 'software_engineering.json',
        'code' : 'ENCT352',
        'name' : 'Software Engineering',
        'semester':6
    },
    ]

def parse_appearance(year_string):
    """Parse '2081 Bhadra R' into year, session, exam_type"""
    if year_string in ['Model Q', 'by DP Sir, Pulchowk']:
        return None, year_string, 'M'
    
    parts = year_string.strip().split()
    
    year = int(parts[0]) if parts[0].isdigit() else None
    session = parts[1] if len(parts) > 1 else ''
    exam_type = parts[2] if len(parts) > 2 else ''
    
    return year, session, exam_type


def import_subject(subject_info):
    with open(subject_info['file'], 'r', encoding='utf-8') as f:
        chapters_data = json.load(f)
    
    subject, created = Subject.objects.update_or_create(
        code=subject_info['code'],
        defaults={
            'name': subject_info['name'],
            'semester': subject_info['semester']
        }
    )
    print(f"{'Created' if created else 'Skipped'} subject: {subject.code}")
    
    for order, chapter_data in enumerate(chapters_data, start=1):
        chapter, created = Chapter.objects.update_or_create(
            subject=subject,
            order=order,
            defaults={
                'title': chapter_data.get('title', ''),
                'subtitle': chapter_data.get('sub', ''),
                'concepts':chapter_data.get('concepts',{}),
            }
        )
        
        for q_data in chapter_data.get('qs', []):
            question, created = Question.objects.get_or_create(
                chapter=chapter,
                text=q_data.get('t', ''),
                defaults={
                    'expression': q_data.get('expr'),
                    'marks': q_data.get('m', ''),
                    'frequency': q_data.get('freq', 1),
                }
            )
            
            if created:
                for year_string in q_data.get('years', []):
                    year, session, exam_type = parse_appearance(year_string)
                    Appearance.objects.create(
                        question=question,
                        year=year,
                        session=session,
                        exam_type=exam_type
                    )

def run():
    for subject_info in SUBJECTS:
        print(f"\nImporting {subject_info['code']}...")
        import_subject(subject_info)
    print("\nDone.")

run()