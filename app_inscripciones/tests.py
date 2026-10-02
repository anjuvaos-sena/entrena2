from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase

from .validators import MAX_PDF_FILE_SIZE, validate_pdf_file


class ValidatePdfFileTests(SimpleTestCase):
	def test_accepts_pdf_with_nonstandard_content_type(self):
		archivo = SimpleUploadedFile(
			'requisitos.PDF',
			b'%PDF-1.7\ncontenido',
			content_type='application/octet-stream',
		)

		validate_pdf_file(archivo)

	def test_rejects_file_without_pdf_signature(self):
		archivo = SimpleUploadedFile(
			'requisitos.pdf',
			b'Esto no es un PDF.',
			content_type='application/pdf',
		)

		with self.assertRaisesMessage(
			ValidationError,
			'El contenido del archivo no corresponde a un PDF.',
		):
			validate_pdf_file(archivo)

	def test_rejects_file_larger_than_supabase_limit(self):
		archivo = SimpleUploadedFile(
			'requisitos.pdf',
			b'%PDF-1.7',
			content_type='application/pdf',
		)
		archivo.size = MAX_PDF_FILE_SIZE + 1

		with self.assertRaisesMessage(
			ValidationError,
			'El archivo no puede superar 50 MB.',
		):
			validate_pdf_file(archivo)
