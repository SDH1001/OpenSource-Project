from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question, QuestionCount


def get_client_ip(request):  # Add this function
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def main(request):
    return render(request, 'pybo/mainpage.html')



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ip = get_client_ip(request)
    #cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    #if cnt == 0:
       # qc = QuestionCount(ip=ip, question=question)
        #qc.save()
        #if question.view_count:
        #    question.view_count += 1
        #else:
           # question.view_count = 1
       # question.save()
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)