from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from .models import Product
from .forms import productForm

# Create your views here.
def show(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view/')
    else:
        form = productForm()
    return render(request,'show.html',{'form': form})

def view(request):
    form = Product.objects.all()
    return render(request,'view.html',{'fm':form})

def edit(request):
    form = Product.objects.get(id=id)
    return render(request,'update.html',{'fm':form})

def update(request,id):
    if request.method == 'POST':   
        ti = Product.objects.get(id=id)
        form = productForm(request.POST, instance=ti)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view/")
    else:
        form = productForm( )
    return render(request,'update.html',{'fm': form})

def delete(request,id):
    form = Product.objects.get(id=id)
    form.delete()
    return redirect('/view/')

