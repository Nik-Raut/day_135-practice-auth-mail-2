from django.shortcuts import render

# Create your views here.
def homeview(request):
    template_name = 'App1/base.html'
    context = {}
    return render(request,template_name,context)

