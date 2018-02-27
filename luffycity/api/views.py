from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        return redirect('api/index')
def index(request):
    return render(request,'index.html')