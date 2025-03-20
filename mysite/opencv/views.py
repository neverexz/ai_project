from django.shortcuts import render

# Create your views here.
def filter(request):
    return render(request, template_name='opencv/filter.html')