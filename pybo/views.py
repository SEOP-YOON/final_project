from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice_Question, Free_Question, Info_Question 
from .forms import Notice_QuestionForm, Free_QuestionForm, Info_QuestionForm, Notice_AnswerForm, Free_AnswerForm, Info_AnswerForm
from django.utils import timezone
from django.core.paginator import Paginator

def index(request):
    return render(request, 'pybo/main.html')
    #메인의 상태이므로 추가 구현이 더 필요


def Notice_main(request):
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Notice_Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/Notice_question_list.html', context)

def Notice_detail(request, question_id):
    question = get_object_or_404(Notice_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Notice_question_detail.html', context)

def Notice_answer_create(request, question_id):
    question = get_object_or_404(Notice_Question, pk=question_id)
    if request.method == "POST":
        form = Notice_AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:Notice_detail', question_id=question.id)
    else:
        form = Notice_AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/Notice_question_detail.html', context)


def Notice_question_create(request):
    if request.method == 'POST':
        form = Notice_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:Notice_main')
    else:
        form = Notice_QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context)

############################################################################################################
def Free_main(request):
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Free_Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/Free_question_list.html', context)

def Free_detail(request, question_id):
    question = get_object_or_404(Free_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Free_question_detail.html', context)

def Free_answer_create(request, question_id):
    question = get_object_or_404(Free_Question, pk= question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:Free_detail', question_id=question.id)
 

def Free_question_create(request):
    if request.method == 'POST':
        form = Free_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:Free_main')
    else:
        form = Free_QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context)

###########################################################################################################3

def Info_main(request):
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Info_Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/Info_question_list.html', context)

def Info_detail(request, question_id):
    question = get_object_or_404(Info_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Info_question_detail.html', context)

def Info_answer_create(request, question_id):
    question = get_object_or_404(Info_Question, pk= question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:Info_detail', question_id=question.id)

def Info_question_create(request):
    form = Info_QuestionForm()
    return render(request, 'pybo/question_form.html',{'form':form})

def Info_question_create(request):
    if request.method == 'POST':
        form = Info_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:Info_main')
    else:
        form = Info_QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context) 