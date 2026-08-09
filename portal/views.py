from django.shortcuts import render
from portal.models import Software

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def datos(request):
    # return render(request, 'datos.html')
    try:
        result = Software.objects.all()
        return render(request, 'datos.html',{'sw':result})
    except:
        return render(request, 'datos.html',{'sw':{}})