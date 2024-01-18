from django import forms

from .models import QuestionBank, McqOption, MultipleChoiceQuestion, TrueOption

class QuestionBankForm(forms.ModelForm):

    class Meta:
        model=QuestionBank
        fields='__all__'
        labels={
            'question_eng':'Question in English',
            'question_urd':'Question in Urdu',
            'grade':'Class',

        }
        exclude=('approved',)

    def __init__(self, *args, **kwargs):
        super(QuestionBankForm, self).__init__(*args, **kwargs)
        
        #self.fields['question_urd'].required=False

class MultipleChoiceQuestionForm(forms.ModelForm):

    class Meta:
        model=MultipleChoiceQuestion
        fields='__all__'
        labels={
            'mcq':'Multiple Choice Question(MCQ)',
        }

class McqOptionForm(forms.ModelForm):

    class Meta:
        model=McqOption
        fields=['op_a', 'op_b', 'op_c', 'op_d']
        labels = {
        'op_a': 'Option A',
        'op_b': 'Option B',
        'op_c': 'Option C',
        'op_d': 'Option D',
    }

class TrueOptionForm(forms.ModelForm):

    class Meta:
        model=TrueOption
        fields=['true_option']