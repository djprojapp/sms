from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QuestionBank, TotalPaper, McqOption, MultipleChoiceQuestion, TrueOption, Kuestion, KuestionType
from accounts.models import User, UserProfile
import random
from .forms import QuestionBankForm, MultipleChoiceQuestionForm, McqOptionForm, TrueOptionForm, KuestionForm, KuestionTypeForm
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
        qbs=list(QuestionBank.objects.all().filter(grade=grade).filter(subject=subject).filter(question_type='short'))
        qbl=list(QuestionBank.objects.all().filter(grade=grade).filter(subject=subject).filter(question_type='long'))
        sz=100
        if len(qbs)<sz:
            sz=len(qbs)
        qbs=random.sample(qbs,sz)
        qbl=random.sample(qbl,2)
        tp=TotalPaper.objects.filter(id=1)
        for i in tp:
            pprgen=i.total
            pprgen +=1
        TotalPaper.objects.filter(id=1).update(total=pprgen)
        total=TotalPaper.objects.all()
        user_id=request.user.id
        user=UserProfile.objects.filter(user_id=user_id)
        return render(request, 'paperdm.html', {'qbs':qbs, 'qbl':qbl, 'user':user})
    else:
        total=TotalPaper.objects.all()
        return render(request, 'home.html', {'total':total})


@login_required(login_url="accounts/login")
def addquestion(request):
    if request.method=="POST":
        form=QuestionBankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Question successfully added')
            qb=QuestionBank.objects.filter(approved=0)
            q=QuestionBank.objects.all()
            return render(request, 'addquestion.html', {'form':form, 'qb':qb, 'q':q})
        else:
            form=QuestionBankForm()
            messages.info(request, "Question already exists in database")
            qb=QuestionBank.objects.filter(approved=0)
            q=QuestionBank.objects.all()
            return render(request, 'addquestion.html', {'form':form, 'qb':qb, 'q':q})
    else:
        form=QuestionBankForm()
        qb=QuestionBank.objects.filter(approved=0)
        q=QuestionBank.objects.all()
        return render(request, 'addquestion.html', {'form':form, 'qb':qb, 'q':q})
    
@login_required(login_url="accounts/login")
def approve(request, id):
    question=QuestionBank.objects.get(id=id)
    mcqs=MultipleChoiceQuestion.objects.get(id=id)
    QuestionBank.objects.filter(id=id).update(approved=1)
    MultipleChoiceQuestion.objects.filter(id=id).update(approved=1)
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

@login_required(login_url="accounts/login")
def addkuestion(request):
    if request.method=="POST":
        k_form=KuestionForm(request.POST)
        kt_form=KuestionTypeForm(request.POST)
        if k_form.is_valid() and kt_form.is_valid():
            kuestion=k_form.save()
            kuestiontypes=kt_form.save(commit=False)
            kuestiontypes.kuestion=kuestion
            kuestiontypes.save()
            messages.info(request, 'Question successfully added')
            qb=KuestionType.objects.all()
            return render(request, 'kuestion.html', {'k_form':k_form, 'kt_form':kt_form, 'qb':qb})
        else:
            k_form=KuestionForm()
            kt_form=KuestionTypeForm()
            messages.info(request, 'Question already exists in database')
            qb=KuestionType.objects.all()
            return render(request, 'kuestion.html', {'k_form':k_form, 'kt_form':kt_form, 'qb':qb})
    else:
        k_form=KuestionForm()
        kt_form=KuestionTypeForm()
        qb=KuestionType.objects.all()
        return render(request, 'kuestion.html', {'k_form':k_form, 'kt_form':kt_form, 'qb':qb})



        
         