from datetime import datetime

from django.shortcuts import render


def index(request):
  return render(request, "DocBlog/index.html", context={"prenom": "Yoann", "date": datetime.today()})