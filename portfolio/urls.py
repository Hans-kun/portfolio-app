from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
   path('', views.index, name='index'),
   path('tag/<slug:tag_slug>/', views.index, name='post_by_tag'),
   path('details/<int:id>/', views.post_detail, name='post_detail'),
   path('about/', views.about, name='about'),
   # path('pdf/<int:id>', views.post_detail, name='pdf'),
   # path('download_pdf/', views.download_pdf, name='download_pdf'),
]
