from django import forms

from .models import QuestionBank, McqOption, MultipleChoiceQuestion, TrueOption, QuestionSelection

class QuestionBankForm(forms.ModelForm):

    class Meta:
        model=QuestionBank
        fields='__all__'
        labels={
            'question_eng':'Question in English',
            'question_urd':'Question in Urdu',
            'grade':'Class',

        }
        exclude=('approved','question_selection', 'question_type',)  


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question_eng'].widget.attrs.update({'id': 'tags'})

class MultipleChoiceQuestionForm(forms.ModelForm):

    class Meta:
        model=MultipleChoiceQuestion
        fields='__all__'
        labels={
            'mcq_eng':'Multiple Choice Question(MCQ)-English',
            'mcq_urd':'Multiple Choice Question(MCQ)-Urdu',
        }
        exclude=('approved',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mcq_eng'].widget.attrs.update({'id': 'tags'})
        
class McqOptionForm(forms.ModelForm):

    class Meta:
        model=McqOption
        fields=['op_a','op_au', 'op_b', 'op_bu', 'op_c', 'op_cu', 'op_d', 'op_du']
        labels = {
        'op_a': 'Option A-English',
        'op_b': 'Option B-English',
        'op_c': 'Option C-English',
        'op_d': 'Option D-English',
        'op_au': 'Option A-urdu',
        'op_bu': 'Option B-urdu',
        'op_cu': 'Option C-urdu',
        'op_du': 'Option D-urdu',
    }

class TrueOptionForm(forms.ModelForm):

    class Meta:
        model=TrueOption
        fields=['true_option']

class QuestionSelectionForm(forms.ModelForm):

    class Meta:
        model=QuestionSelection
        fields='__all__'
        labels = {
        'short': 'Short Question?',
        'long': 'Long Question?',
        'analytical': 'Analytical Question?',
        'i2018': 'Part I 2018',
        'ii2018': 'Part II 2018',
        'i2019': 'Part I 2019',
        'ii2019': 'Part II 2019',
        'i2020': 'Part I 2020',
        'ii2020': 'Part II 2020',
        'i2021': 'Part I 2021',
        'ii2021': 'Part II 2021',
        'i2022': 'Part I 2022',
        'ii2022': 'Part II 2022',

    }