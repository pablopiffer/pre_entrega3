from django.urls import path

from Tratamiento.views import (
    index,
    lista_pacientes,
    paciente_create,
    paciente_delete,
    paciente_detalles,
    paciente_update,
)

app_name = "Tratamiento"

urlpatterns = [
    path("", index, name="index"),
    path("lista_pacientes/", lista_pacientes, name="lista_pacientes"),
    path("paciente_confirm_delete/<int:pk>", paciente_delete, name="paciente_confirm_delete"),
    path("paciente_detalles/<int:pk>", paciente_detalles, name="paciente_detalles"),
    path("paciente_update/<int:pk>", paciente_update, name="paciente_update"),
    path("paciente_form/", paciente_create, name="paciente_form"),
]
