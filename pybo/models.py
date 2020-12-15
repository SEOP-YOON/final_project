#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User



class Notice_Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Notice_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Notice_Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


class Free_Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.subject


class Free_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Free_Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)



class Info_Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.subject


class Info_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Info_Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
