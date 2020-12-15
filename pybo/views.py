from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice_Question, Free_Question, Info_Question , Notice_Answer, Free_Answer, Info_Answer
from .forms import Notice_QuestionForm, Free_QuestionForm, Info_QuestionForm, Notice_AnswerForm, Free_AnswerForm, Info_AnswerForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    return render(request, 'pybo/main.html')
    #메인의 상태이므로 추가 구현이 더 필요


def Notice_main(request):
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Notice_Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    # ---------------------------------------------------------------------------------------- #

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # ---------------------------------------- [edit] ---------------------------------------- #
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    # ---------------------------------------------------------------------------------------- #
    return render(request, 'pybo/Notice_question_list.html', context)


def Notice_detail(request, question_id):
    question = get_object_or_404(Notice_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Notice_question_detail.html', context)

@login_required(login_url='common:login')
def Notice_answer_create(request, question_id):
    question = get_object_or_404(Notice_Question, pk=question_id)
    if request.method == "POST":
        form = Notice_AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:Notice_detail', question_id=question.id)
    else:
        form = Notice_AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/Notice_question_detail.html', context)

@login_required(login_url='common:login')
def Notice_question_create(request):
    if request.method == 'POST':
        form = Notice_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:Notice_main')
    else:
        form = Notice_QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context)

@login_required(login_url='common:login')
def Notice_question_modify(request, question_id):
  
    question = get_object_or_404(Notice_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Notice_detail', question_id=question.id)

    if request.method == "POST":
        form = Notice_QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:Notice_detail', question_id=question.id)
    else:
        form = Notice_QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def Notice_question_delete(request, question_id):
    question = get_object_or_404(Notice_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:Notice_detail', question_id=question.id)
    question.delete()
    return redirect('pybo:Notice_main')

@login_required(login_url='common:login')
def Notice_answer_modify(request, answer_id):
    
    answer = get_object_or_404(Notice_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Notice_detail', question_id=answer.question.id)

    if request.method == "POST":
        form = Notice_AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:Notice_detail', question_id=answer.question.id)
    else:
        form = Notice_AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/Notice_answer_form.html', context)

@login_required(login_url='common:login')
def Notice_answer_delete(request, answer_id):
    answer = get_object_or_404(Notice_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:Notice_detail', question_id=answer.question.id)

############################################################################################################
def Free_main(request):
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Free_Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    # ---------------------------------------------------------------------------------------- #

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # ---------------------------------------- [edit] ---------------------------------------- #
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    # ---------------------------------------------------------------------------------------- #
    return render(request, 'pybo/Free_question_list.html', context)

def Free_detail(request, question_id):
    question = get_object_or_404(Free_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Free_question_detail.html', context)

@login_required(login_url='common:login')
def Free_answer_create(request, question_id):
    question = get_object_or_404(Free_Question, pk= question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:Free_detail', question_id=question.id)
 
@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
def Free_question_modify(request, question_id):
  
    question = get_object_or_404(Free_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Free_detail', question_id=question.id)

    if request.method == "POST":
        form = Free_QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:Free_detail', question_id=question.id)
    else:
        form = Free_QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def Free_question_delete(request, question_id):
    question = get_object_or_404(Free_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:Free_detail', question_id=question.id)
    question.delete()
    return redirect('pybo:Free_main')

@login_required(login_url='common:login')
def Free_answer_modify(request, answer_id):
    
    answer = get_object_or_404(Free_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Notice_detail', question_id=answer.question.id)

    if request.method == "POST":
        form = Free_AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:Free_detail', question_id=answer.question.id)
    else:
        form = Free_AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/Free_answer_form.html', context)

@login_required(login_url='common:login')
def Free_answer_delete(request, answer_id):
    answer = get_object_or_404(Free_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:Free_detail', question_id=answer.question.id)
###########################################################################################################3

def Info_main(request):
      # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Info_Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    # ---------------------------------------------------------------------------------------- #

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # ---------------------------------------- [edit] ---------------------------------------- #
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    # ---------------------------------------------------------------------------------------- #
    return render(request, 'pybo/Info_question_list.html', context)

def Info_detail(request, question_id):
    question = get_object_or_404(Info_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/Info_question_detail.html', context)

@login_required(login_url='common:login')
def Info_answer_create(request, question_id):
    question = get_object_or_404(Info_Question, pk= question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:Info_detail', question_id=question.id)


@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
def Info_question_modify(request, question_id):
  
    question = get_object_or_404(Info_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Info_detail', question_id=question.id)

    if request.method == "POST":
        form = Info_QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:Info_detail', question_id=question.id)
    else:
        form = Info_QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def Info_question_delete(request, question_id):
    question = get_object_or_404(Info_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:Info_detail', question_id=question.id)
    question.delete()
    return redirect('pybo:Info_main')

@login_required(login_url='common:login')
def Info_answer_modify(request, answer_id):
    
    answer = get_object_or_404(Info_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:Info_detail', question_id=answer.question.id)

    if request.method == "POST":
        form = Info_AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:Info_detail', question_id=answer.question.id)
    else:
        form = Info_AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/Info_answer_form.html', context)

@login_required(login_url='common:login')
def Info_answer_delete(request, answer_id):
    answer = get_object_or_404(Info_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:Info_detail', question_id=answer.question.id)