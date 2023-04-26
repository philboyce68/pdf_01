from pdf import views
from django.urls import path
from .views import home_view, upload_pdf, upload_success

urlpatterns = [
    path('', home_view, name='pdf_home'),
    path('upload/', upload_pdf, name='upload_pdf'),
    path('upload_success', upload_success, name='upload-success'),
    # path('combine_pdfs/', combine_pdfs, name='combine_pdfs'),
]
