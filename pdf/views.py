from django.shortcuts import render
from .forms import PdfUploadForm
from PyPDF4 import PdfFileMerger, PdfFileReader
import os
from django.http import HttpResponse
import traceback


def home_view(request):
    return render(request, 'pdf/home.html')


def upload_pdf(request):
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            with open('media/pdf/' + pdf_file.name, 'wb') as f:
                f.write(pdf_file.read())
            return render(request, 'pdf/upload_success.html')

    else:
        form = PdfUploadForm()
    return render(request, 'pdf/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'pdf/upload_success')


# def combine_pdfs(request):
#     if request.method == 'POST':
#         pdf_folder = request.FILES['pdf_folder']
#         print(f'PD Folder: {pdf_folder}')
#         pdf_files = [os.path.join(pdf_folder.name, file) for file in os.listdir(pdf_folder.name)
#                      if file.endswith('.pdf')]
#         print(f'PDf Files: {pdf_files}')
#
#         merger = PdfFileMerger()
#         print(f'Merger: {merger}')
#         for file in pdf_files:
#             try:
#                 with open(file, 'rb') as pdf_file:
#                     merger.append(PdfFileReader(pdf_file, 'rb'))
#             except Exception as e:
#                 print(f"Error appending {file}: {e}")
#                 traceback.print_exc()
#
#         merger.write("media/output/combined_output.pdf")
#         merger.close()
#
#         with open('media/output/combined_output.pdf', 'rb') as pdf_file:
#             response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="combined_output.pdf"'

        # return response








