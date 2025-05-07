from django.shortcuts import render

def gallery(request):
    # Replace HttpResponse with render to display the template
    return render(request, 'gallery/gallery.html')
