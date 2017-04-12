from django.shortcuts import render

# Create your views here.



def sale_index(request):
    return render(request, "sale/index.html")