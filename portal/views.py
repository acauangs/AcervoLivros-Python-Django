from django.shortcuts import render, redirect
from portal.models import *
from portal.forms import *


# MY views.

def HomeView(request):
    return render(request, 'portal/home.html')


def AutorView(request):
    autores = Autor.objects.all()

    context = {
        'autores': autores,
    }

    return render(request, 'portal/autor.html', context)


def autor_add(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
    
    context = {
        'form': form
    }

    return render(request, 'portal/autor_add.html', context)

def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance = autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('autor')
    
    context = {
        
        'form': form,
    }
    
    return render(request,'portal/autor_edit.html', context)


def autor_delete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()

    return redirect('autor')

    
def EditoraView(request):
    editora = Editora.objects.all()

    context = {
        'editora': editora,
    }
    return render(request, 'portal/editora.html', context)


def editora_add(request):
    form = EditoraForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')
    
    context = {
        'form': form
    }
    return render(request, 'portal/editora_add.html', context)


def editora_edit(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    form = EditoraForm(request.POST or None, instance = editora)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')
    
    context = {
        
        'form': form
    
    }

    return render(request, 'portal/editora_edit.html', context)


def editora_delete(request, editora_pk):
    editora = Editora.objects.get(pk =editora_pk)
    editora.delete()
    
    return redirect('editora')


def FormatoView(request):
    return render(request, 'portal/formato.html')


def DashboardView(request):
    return render(request, 'portal/dashboard.html')


def LivroView(request):
    livro = Livro.objects.all()

    context = {
        'livro': livro,
    }

    return render(request, 'portal/livro.html', context)


def livro_add(request):
    form = LivroForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livro')
    
    context = {
        'form': form
    }

    return render(request, 'portal/livro_add.html', context)

def livro_edit(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    form = LivroForm(request.POST or None, instance = livro)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('livro')
    
    context = {
        
        'form': form,
    }
    
    return render(request,'portal/livro_edit.html', context)


def livro_delete(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()

    return redirect('livro')








