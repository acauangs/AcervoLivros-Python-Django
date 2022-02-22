from django.db import models

# My models.

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Formato(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    numero_paginas = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
