from django.shortcuts import render

from .forms import supportForm

def support_submit(request):
    if request.method == 'POST':
        form = supportForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'moshavere/support.html',{'form': form})
    else:
        form = supportForm()
    
    return render (request,'moshavere/support.html',{'form': form})
      

