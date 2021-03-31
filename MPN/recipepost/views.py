from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required



@login_required
def recipepost(request):
    form = Recipepost.objects.order_by('-date_created')
    return render(request,'recipepost/recipepost.html', {'form':form})


@login_required
def cpost(request):
    if request.method == 'GET':
        return render(request, 'recipepost/cpost.html', {'form':Recipepostform()})
    else:
        try:
            dr = Recipepostform(data=request.POST,files=request.FILES)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('recipepost')
        except ValueError:
            return render(request, 'recipepost/cpost.html', {'form':Recipepostform(), 'error':'Error! Try again!'})

@login_required
def dpost(request,d_id):
    dd2 = get_object_or_404(Recipepost, pk=d_id)
    return render(request,'recipepost/dpost.html', {'dd':dd2})
@login_required
def search(request):
    query=request.GET['query']
    allpost=Recipepost.objects.filter(title__icontains=query)
    return render(request,'recipepost/search.html', {'allpost': allpost})

@login_required
def rate(request, m_id):
    if request.method == 'POST':
        score = request.POST.get('score')
        title = Recipepost.objects.get(sno=m_id)
        obj = Rating(title=title, score=score)
        obj.save()
        return redirect(f'/recipepost/dpost/{m_id}')