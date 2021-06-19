from django.http import HttpResponse
from django.shortcuts import render
from .models import Documents

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_documents_to_expire(request):
    obj = Documents.objects.get(id=1)
    context = {
        'doc_name': obj.doc_name,
        'doc_expiry_date': obj.doc_expiry_date
    }
    return render(request, "document/detail.html", {})