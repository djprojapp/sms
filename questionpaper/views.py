from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QuestionBank, TotalPaper, McqOption, MultipleChoiceQuestion, TrueOption, QuestionSelection
from accounts.models import User, UserProfile
import random
from .forms import QuestionBankForm, MultipleChoiceQuestionForm, McqOptionForm, TrueOptionForm, QuestionSelectionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    total=TotalPaper.objects.all()
    return render(request, 'home.html', {'total':total})

@login_required(login_url="accounts/login")
def paper(request):
    if request.method=="POST":
        grade=request.POST['grade']
        subject=request.POST['subject']
        paper_type=request.POST['paper_type']
        qbs=list(QuestionBank.objects.all().filter(grade=grade).filter(subject=subject).filter(question_selection__short=1))
        qbl=list(QuestionBank.objects.all().filter(grade=grade).filter(subject=subject).filter(question_selection__long=1))
        mcq=list(McqOption.objects.all().select_related('options'))
        sz1=20
        sz2=6
        sz3=20
        if len(qbs)<sz1:
            sz1=len(qbs)
        if len(qbl)<sz2:
            sz2=len(qbl)
        if len(mcq)<sz3:
            sz3=len(mcq)

        qbs=random.sample(qbs,sz1)
        qbl=random.sample(qbl,sz2)
        mcq=random.sample(mcq,sz3)
        tp=TotalPaper.objects.filter(id=1)
        for i in tp:
            pprgen=i.total
            pprgen +=1
        TotalPaper.objects.filter(id=1).update(total=pprgen)
        total=TotalPaper.objects.all()
        user_id=request.user.id
        user=UserProfile.objects.filter(user_id=user_id)
        if paper_type=="subjective":
            return render(request, 'paper.html', {'qbs':qbs, 'qbl':qbl, 'user':user})
        else:
            return render(request, 'objective.html', {'mcq':mcq, 'user':user, 'subject':subject, 'grade':grade})
    else:
        total=TotalPaper.objects.all()
        return render(request, 'home.html', {'total':total})


@login_required(login_url="accounts/login")
def addquestion(request):
    if request.method=="POST":
        form=QuestionBankForm(request.POST)
        s_form=QuestionSelectionForm(request.POST)
        if form.is_valid() and s_form.is_valid():
            question_selection=s_form.save()
            question=form.save(commit=False)
            question.question_selection=question_selection
            question.save()
            messages.info(request, 'Question successfully added')
            qb=QuestionBank.objects.filter(approved=0)
            q=QuestionBank.objects.all()
            s_form=QuestionSelectionForm()
            return render(request, 'addquestion.html', {'form':form, 's_form':s_form, 'qb':qb, 'q':q})
        else:
            form=QuestionBankForm()
            messages.info(request, "Question already exists in database")
            qb=QuestionBank.objects.filter(approved=0)
            q=QuestionBank.objects.all()
            s_form=QuestionSelectionForm()
            return render(request, 'addquestion.html', {'form':form, 's_form':s_form, 'qb':qb, 'q':q})
    else:
        form=QuestionBankForm()
        question_selection=QuestionSelection.objects.all()
        qb=QuestionBank.objects.filter(approved=0).select_related("question_selection")
        q=QuestionBank.objects.all()
        s_form=QuestionSelectionForm()
        return render(request, 'addquestion.html', {'form':form, 's_form':s_form, 'qb':qb, 'q':q})
    
@login_required(login_url="accounts/login")
def approve(request, id):
    question=QuestionBank.objects.get(id=id)
    QuestionBank.objects.filter(id=id).update(approved=1)
    form=QuestionBankForm()
    qb=QuestionBank.objects.filter(approved=0)
    return redirect('questionpaper:addquestion')

@login_required(login_url="accounts/login")
def approvemcq(request, id):
    TrueOption.objects.get(id=id)
    TrueOption.objects.filter(id=id).update(approved=1)
    return redirect('questionpaper:addmcq')

@login_required(login_url="accounts/login")
def addmcq(request):
    if request.method=="POST":
        mcq_form=MultipleChoiceQuestionForm(request.POST)
        o_form=McqOptionForm(request.POST)
        t_form=TrueOptionForm(request.POST)
        if mcq_form.is_valid() and o_form.is_valid() and t_form.is_valid():
            mcq=mcq_form.save()
            mcq_options=o_form.save(commit=False)
            mcq_options.options=mcq
            mcq_options.save()
            true_option=t_form.save(commit=False)
            true_option.trueoption=mcq_options
            true_option.save()
            messages.info(request, 'Question successfully added')
            mcqs=TrueOption.objects.filter(approved=0)
            return render(request, 'addmcq.html', {'mcq_form':mcq_form, 'o_form':o_form, 't_form':t_form, 'mcqs':mcqs})
        else:
            mcq_form=MultipleChoiceQuestionForm()
            o_form=McqOptionForm()
            t_form=TrueOptionForm()
            messages.info(request, 'Question already exists in database')
            mcqs=TrueOption.objects.filter(approved=0)
            return render(request, 'addmcq.html', {'mcq_form':mcq_form, 'o_form':o_form, 't_form':t_form, 'mcqs':mcqs})
    else:
        mcq_form=MultipleChoiceQuestionForm()
        o_form=McqOptionForm()
        t_form=TrueOptionForm()
        mcqs=TrueOption.objects.filter(approved=0)
        m=MultipleChoiceQuestion.objects.all()
        return render(request, 'addmcq.html', {'mcq_form':mcq_form, 'o_form':o_form, 't_form':t_form, 'mcqs':mcqs, 'm':m})

def view(request):
    qbs=QuestionBank.objects.all().select_related('question_selection').filter(question_selection__short=1)
    return render (request, 'edit.html', {'qbs':qbs})

def edit(request, id):
    QuestionBank.objects.get(id=id)
    if request.method=="POST":
        question_eng=request.POST['question_eng']
        question_urd=request.POST['question_urd']
        chapter=request.POST['chapter']
        QuestionBank.objects.filter(id=id).update(question_eng=question_eng, question_urd=question_urd, chapter=chapter)
        qbs=QuestionBank.objects.all().select_related('question_selection').filter(question_selection__short=1)
        return render(request, 'edit.html', {'qbs':qbs})
    
def manualpaper(request):
    pass