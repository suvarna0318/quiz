from django.contrib import admin
from .models import student,Category,Question,Answer

admin.site.register(student)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)