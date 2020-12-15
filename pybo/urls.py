from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns =[
    path('', views.index, name='index'),
    path('Notice/',views.Notice_main ,name = 'Notice_main'),
    path('Notice/<int:question_id>/', views.Notice_detail, name='Notice_detail'),
    path('Notice/answer/create/<int:question_id>/', views.Notice_answer_create, name='Notice_answer_create'),
    path('Notice/question/create/', views.Notice_question_create, name = 'Notice_question_create'),

    path('Free/',views.Free_main ,name = 'Free_main'),
    path('Free/<int:question_id>/', views.Free_detail, name='Free_detail'),
    path('Free/answer/create/<int:question_id>/', views.Free_answer_create, name='Free_answer_create'),
    path('Free/question/create/', views.Free_question_create, name = 'Free_question_create'),

    path('Info/',views.Info_main ,name = 'Info_main'),
    path('Info/<int:question_id>/', views.Info_detail, name='Info_detail'),
    path('Info/answer/create/<int:question_id>/', views.Info_answer_create, name='Info_answer_create'),
    path('Info/question/create/', views.Info_question_create, name = 'Info_question_create'),
]