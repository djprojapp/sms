from django.db import models


# Create your models here.
class QuestionBank(models.Model):
    question_eng=models.CharField(max_length=200,  unique=True)
    question_urd=models.CharField(max_length=200)
    question_type=models.CharField(max_length=20, choices=(
        ('', '--select--'),
        ('short','short'),
        ('long','long'),
        ))
    subject=models.CharField(max_length=20, choices=(
        ('', '--select--'),
        ('islamiyat','Islamiyat'),
        ('urdu','Urdu'),
        ('physics','Physics'),
        ('chemistry','Chemsitry'),
        ('bioloby','Biology'),
        ('math','Mathematics'),
        ('english','English'),
        ('pakstudy','Pakistan Study'),
        ))
    grade=models.CharField(max_length=20, choices=(
        ('', '--select--'),
        ('10','10'),
        ('9','9'),
        ('8','8'),
        ('7','7'),
        ('6','6'),
        ('5','5'),
        ))
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.question_eng+"  "+self.question_type
    
    
        
class TotalPaper(models.Model):
    total=models.IntegerField(default=0)

class MultipleChoiceQuestion(models.Model):
    subject=models.CharField(max_length=20, choices=(
        ('', '--select--'),
        ('islamiyat','Islamiyat'),
        ('urdu','Urdu'),
        ('physics','Physics'),
        ('chemistry','Chemsitry'),
        ('bioloby','Biology'),
        ('math','Mathematics'),
        ('english','English'),
        ('pakstudy','Pakistan Study'),
        ), default='--select--', unique=True)
    grade=models.CharField(max_length=20, choices=(
        ('', '--select--'),
        ('10','10'),
        ('9','9'),
        ('8','8'),
        ('7','7'),
        ('6','6'),
        ('5','5'),
        ), default='--select--')
    mcq=models.CharField(max_length=200)
     
    def __str__(self):
        return self.mcq
    

class McqOption(models.Model):
    options=models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
    op_a=models.CharField(max_length=100)
    op_b=models.CharField(max_length=100)
    op_c=models.CharField(max_length=100)
    op_d=models.CharField(max_length=100)
    

    def __str__(self):
        return self.op_a
    
class TrueOption(models.Model):
    trueoption=models.ForeignKey(McqOption, on_delete=models.CASCADE)
    true_option=models.CharField(max_length=100)
    approved=models.BooleanField(default=False)
    def __str__(self):
        return self.true_option

