
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_post, name='review_post'),
    path('postcomment/<int:m_id>/',views.postcomment, name='postcomment'),
    path('likepost/<int:pk>/', views.likepost, name='likepost'),
    path('creviewpost', views.creviewpost, name='creviewpost'),
    path('dreviewpost/<int:m_id>/', views.dreviewpost, name='dreviewpost'),
    path('mypostd/<int:m_id>/', views.mypostd, name='mypostd'),
    path('mypost/', views.mypost, name='mypost'),
    path('mypostd/<int:m_id>/delete', views.mypostdelete, name='mypostdelete'),
    
]