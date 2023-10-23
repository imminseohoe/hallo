from django.shortcuts import render

def ginlo (request):
    return render(request, 'ginlo/ginlo.html')
def choose(request):
    return render(request, 'ginlo/choose.html')