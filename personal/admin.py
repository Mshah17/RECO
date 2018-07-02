from django.contrib import admin
from .models import Medicinereco

class MedicinerecoAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'symptoms', 'dose')
    search_fields = ('medicine', 'symptoms')

admin.site.register(Medicinereco, MedicinerecoAdmin)