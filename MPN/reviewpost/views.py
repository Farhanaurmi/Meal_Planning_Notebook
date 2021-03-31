from django.shortcuts import render, redirect, get_object_or_404
from .models import Reviewpost,ReviewComment
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

# Create your views here.
@login_required
def review_post(request):
    form = Reviewpost.objects.order_by('-date_created')
    return render(request,'reviewpost/reviewpost.html',  {'form':form})


@login_required
def creviewpost(request):
    if request.method == 'GET':
        
        return render(request, 'reviewpost/creviewpost.html', {'form': Reviewpostform()})
    else:
        try:
            dr = Reviewpostform(data=request.POST,files=request.FILES)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('review_post')
        except ValueError:
            return render(request, 'reviewpost/creviewpost.html', {'form': Reviewpostform(), 'error':'Error! Try again!'})


@login_required
def dreviewpost(request,m_id):

    dd2 = get_object_or_404(Reviewpost, pk=m_id)
    post=Reviewpost.objects.filter(sno=m_id).first()
    stuff= get_object_or_404(Reviewpost, sno=m_id)
    total_likes=stuff.total_likes()
    liked=False
    if stuff.likes.filter(id=request.user.id).exists():
        liked=True
    comment = ReviewComment.objects.filter(post=post)
    return render(request,'reviewpost/dreviewpost.html', {'dd':dd2 , 'comments':comment, 'form':Commentpostform(), 'total_likes':total_likes, 'liked':liked})


@login_required
def mypostd(request,m_id):
    dd2 = get_object_or_404(Reviewpost, pk=m_id, user=request.user)
    return render(request,'reviewpost/mypostd.html', {'dd':dd2})

@login_required
def mypost(request):
    form = Reviewpost.objects.filter(user=request.user)
    return render(request, 'reviewpost/mypost.html', {'form':form})
    
@login_required
def mypostdelete(request, m_id):
    dd2 = get_object_or_404(Reviewpost, pk=m_id, user=request.user)
    if request.method == 'POST':
        dd2.delete()
        return redirect('mypost')

@login_required
def postcomment(request, m_id):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        post=Reviewpost.objects.get(sno=m_id)
        comment=ReviewComment(comment=comment,user=user,post=post)
        comment.save()
        return redirect(f'/reviewpost/dreviewpost/{post.sno}')

@login_required
def likepost(request,pk):
    post= get_object_or_404(Reviewpost, sno=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('dreviewpost', args=[str(pk)]))
