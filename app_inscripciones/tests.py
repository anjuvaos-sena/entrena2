from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, SimpleTestCase

from .views import _datos_inscripcion


class InscripcionUploadTests(SimpleTestCase):
	def test_accepts_non_pdf_file_types(self):
		archivo = SimpleUploadedFile(
			'imagen.jpg',
			b'\xff\xd8\xff',
			content_type='image/jpeg',
		)
		request = RequestFactory().post(
			'/inscripciones/1/inscribirse/',
			data={
				'numero_identificacion': '123',
				'nombres': 'Nombre',
				'apellidos': 'Apellido',
				'correo_electronico': 'persona@example.com',
				'telefono': '123',
				'centro_formacion': 'Centro',
				'regional': 'Regional',
				'archivo_adjunto': archivo,
			},
		)

		_, archivo_recibido, errores = _datos_inscripcion(request)

		self.assertEqual(archivo_recibido.name, 'imagen.jpg')
		self.assertEqual(archivo_recibido.content_type, 'image/jpeg')
		self.assertNotIn('archivo_adjunto', errores)

	def test_still_requires_an_attachment(self):
		request = RequestFactory().post(
			'/inscripciones/1/inscribirse/',
			data={
				'numero_identificacion': '123',
				'nombres': 'Nombre',
				'apellidos': 'Apellido',
				'correo_electronico': 'persona@example.com',
				'telefono': '123',
				'centro_formacion': 'Centro',
				'regional': 'Regional',
			},
		)

		_, archivo_recibido, errores = _datos_inscripcion(request)

		self.assertIsNone(archivo_recibido)
		self.assertEqual(errores['archivo_adjunto'], 'Debe adjuntar un archivo.')
