from django.contrib import admin
from .models import QuestionBank, TotalPaper, MultipleChoiceQuestion, McqOption, TrueOption, Kuestion, KuestionType

# Register your models here.
admin.site.register(QuestionBank)
admin.site.register(TotalPaper)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(McqOption)
admin.site.register(TrueOption)
admin.site.register(Kuestion)
admin.site.register(KuestionType)

