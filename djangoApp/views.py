from django.shortcuts import render
def hello(request):
    return render(request, 'Hello.html')
def main(request):
    return render(request, 'main.html')



# Create your views here.
