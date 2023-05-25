from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    d1=datetime.datetime.now()
    d={'data':'How Are you','d1':d1,'c':4}
    return render(request,'filters.html',d)