from django.db import migrations


class Migration(migrations.Migration):

	dependencies = [
		('app_inscripciones', '0001_initial'),
	]

	operations = [
		migrations.RenameField(
			model_name='inscripcion',
			old_name='archivo_pdf',
			new_name='archivo_adjunto',
		),
	]
