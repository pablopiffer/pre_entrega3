from django.urls import path

from Tratamiento.views import (
    PacienteList,
    PacienteCreate,
    PacienteDelete,
    PacienteDetail,
    PacienteUpdate,
    InstitucionList,
    InstitucionCreate,
    InstitucionDelete,
    InstitucionDetail,
    InstitucionUpdate,
    EstadisticasView,
    NotaDeSesionCreate,
    ObjetivoDeTratamientoCreate,
    index,

)

app_name = "Tratamiento"

urlpatterns = [
    path("", index, name="index")
    # path("lista_pacientes/", lista_pacientes, name="lista_pacientes"),
    # path("paciente_confirm_delete/<int:pk>", paciente_delete, name="paciente_confirm_delete"),
    # path("paciente_detalles/<int:pk>", paciente_detalles, name="paciente_detalles"),
    # path("paciente_update/<int:pk>", paciente_update, name="paciente_update"),
    # path("paciente_form/", paciente_create, name="paciente_form"),
]

urlpatterns += [
    path("Tratamiento/lista_pacientes", PacienteList.as_view(), name="lista_pacientes"),
    path("Tratamiento/paciente_create/", PacienteCreate.as_view(), name="paciente_form"),
    path("Tratamiento/paciente_detalles/<int:pk>", PacienteDetail.as_view(), name="paciente_detalles"),
    path("Tratamiento/paciente_update/<int:pk>", PacienteUpdate.as_view(), name="paciente_update"),
    path("Tratamiento/paciente_confirm_delete/<int:pk>", PacienteDelete.as_view(), name="paciente_confirm_delete"),
    path("Tratamiento/estadisticas", EstadisticasView.as_view(), name="estadisticas"),
    path("Tratamiento/lista_institucion", InstitucionList.as_view(), name="lista_institucion"),
    path("Tratamiento/institucion_create/", InstitucionCreate.as_view(), name="institucion_form"),
    path("Tratamiento/institucion_detalles/<int:pk>", InstitucionDetail.as_view(), name="institucion_detalles"),
    path("institucion_update/<int:pk>", InstitucionUpdate.as_view(), name="institucion_update"),
    path("Tratamiento/institucion_confirm_delete/<int:pk>", InstitucionDelete.as_view(), name="institucion_confirm_delete"),
    path("Tratamiento/nota_de_sesion_form/", NotaDeSesionCreate.as_view(), name="nota_de_sesion_form"),
    path("Tratamiento/objetivo_de_tratamiento_form/", ObjetivoDeTratamientoCreate.as_view(), name="objetivo_de_tratamiento_form"),
]
