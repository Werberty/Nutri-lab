from django.contrib import admin

from .models import Pacientes, Refeicao, Opcao

admin.site.register(Pacientes)
admin.site.register(Refeicao)
admin.site.register(Opcao)
