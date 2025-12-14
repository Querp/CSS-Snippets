from django.shortcuts import render
from .models import Snippet

def homepage(request):
    snippets = Snippet.objects.all().order_by('-created_at')  # newest first
    return render(request, 'snippets/homepage.html', {'snippets': snippets})