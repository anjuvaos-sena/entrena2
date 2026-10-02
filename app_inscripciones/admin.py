from django.contrib import admin
from django.utils.html import format_html

from .models import Inscripcion


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'apellidos',
        'numero_identificacion',
        'convocatoria',
        'fecha_inscripcion',
        'enlace_archivo_pdf',
    )
    search_fields = (
        'nombres',
        'apellidos',
        'numero_identificacion',
        'correo_electronico',
    )
    readonly_fields = ('enlace_archivo_pdf',)
    fields = (
        'convocatoria',
        'numero_identificacion',
        'nombres',
        'apellidos',
        'correo_electronico',
        'telefono',
        'centro_formacion',
        'regional',
        'fecha_inscripcion',
        'enlace_archivo_pdf',
    )

    @admin.display(description='PDF adjunto')
    def enlace_archivo_pdf(self, obj):
        if not obj or not obj.archivo_pdf:
            return 'Sin archivo'
        return format_html(
            '<a href="{}" target="_blank" rel="noopener">Abrir PDF</a>',
            obj.archivo_pdf.url,
        )
