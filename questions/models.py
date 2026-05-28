from django.db import models

class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    semester = models.IntegerField()
    def __str__(self):
        return f"{self.code}-{self.name}"
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300,blank= True)
    order = models.IntegerField()
    concepts = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.subject.code}-{self.title}"
    
class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    expression = models.CharField(max_length=500, blank=True, null=True)
    marks = models.CharField(max_length=20, blank=True)
    frequency = models.IntegerField(default=1)

    def __str__(self):
        return self.text[:80]

class Appearance(models.Model):
    EXAM_TYPES = [
        ('R','Regular'),
        ('B','Back'),
        ('M','Model'),
        ('I','Internal'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='appearances')
    year = models.IntegerField(null=True, blank=True)
    session = models.CharField(max_length=50, blank=True)
    exam_type = models.CharField(max_length=1, choices=EXAM_TYPES, blank=True)
    
    def __str__(self):
        return f"{self.year}{self.session}{self.exam_type}"
    