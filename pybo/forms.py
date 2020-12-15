from django import forms
from pybo.models import Notice_Question, Free_Question, Info_Question, Notice_Answer, Free_Answer, Info_Answer


class Notice_QuestionForm(forms.ModelForm):
    class Meta:
        model= Notice_Question
        fields = ['subject', 'content']

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10})
        }

class Notice_AnswerForm(forms.ModelForm):
    class Meta:
        model = Notice_Answer
        fields = ['content']
        labels ={
            'content' :'답변내용',
        }

class Free_QuestionForm(forms.ModelForm):
    class Meta:
        model= Free_Question
        fields = ['subject', 'content']

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10})
        }

class Free_AnswerForm(forms.ModelForm):
    class Meta:
        model = Free_Answer
        fields = ['content']
        labels ={
            'content' :'답변내용',
        }


class Info_QuestionForm(forms.ModelForm):
    class Meta:
        model= Info_Question
        fields = ['subject', 'content']

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10})
        }

class Info_AnswerForm(forms.ModelForm):
    class Meta:
        model = Info_Answer
        fields = ['content']
        labels ={
            'content' :'답변내용',
        }