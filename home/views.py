from django.shortcuts import render

def home(request):
    # Replace HttpResponse with render to display the template
    return render(request, 'home/index.html')
