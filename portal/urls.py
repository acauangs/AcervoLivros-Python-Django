from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView, name ='home'),
    
    path('autor/', views.AutorView, name ='autor'),
    path('autor/add/', views.autor_add, name='autor_add'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),
    
    path('editora', views.EditoraView, name ='editora'),
    path('editora/add/', views.editora_add, name ='editora_add'),
    path('editora/adit/<int:editora_pk>', views.editora_edit, name ='editora_edit'),
    path('editora/delete/<int:editora_pk>', views.editora_delete, name ='editora_delete'),
    
    path('livro/', views.LivroView, name ='livro'),
    path('livro/add/', views.livro_add, name ='livro_add'),
    path('livro/adit/<int:livro_pk>', views.livro_edit, name ='livro_edit'),
    path('livro/delete/<int:livro_pk>', views.livro_delete, name ='livro_delete'),
    
    
    path('dashboard/', views.DashboardView, name ='dashboard'),
    path('formato/', views.FormatoView, name ='formato'),


    
]
