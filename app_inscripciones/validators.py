from django.core.exceptions import ValidationError


MAX_PDF_FILE_SIZE = 50 * 1024 * 1024
MAX_PDF_FILE_SIZE_MB = MAX_PDF_FILE_SIZE // (1024 * 1024)
PDF_HEADER = b'%PDF-'


def validate_pdf_file(uploaded_file):
	"""Valida extensión, tamaño y firma del PDF sin confiar en el MIME declarado."""
	if not uploaded_file.name.lower().endswith('.pdf'):
		raise ValidationError('El archivo debe tener extensión .pdf.')

	if uploaded_file.size > MAX_PDF_FILE_SIZE:
		raise ValidationError(
			f'El archivo no puede superar {MAX_PDF_FILE_SIZE_MB} MB.',
		)

	position = uploaded_file.tell()
	try:
		header = uploaded_file.read(1024)
	finally:
		uploaded_file.seek(position)

	if PDF_HEADER not in header:
		raise ValidationError('El contenido del archivo no corresponde a un PDF.')
