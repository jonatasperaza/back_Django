from django.db import models

# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao
    
class Pais(models.Model):
    nome = models.CharField(max_length=60)
        
    def __str__(self):
        return self.nome
    
class tipoAtuacao(models.Model):
    descricao = models.CharField(max_length=100)
        
    def __str__(self):
        return self.descricao
    
class Produtora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.pais)
    
class Membros(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    dataNasc = models.DateField()

    def __str__(self):
        return "{} ({}) ({})".format(sefl.some, self.pai, self.dataNasc)
    
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField()
    duracao = models.TimeField()
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    ano = models.IntegerField()
    classificacao = models.IntegerField()
    produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)
    
    def __str__(self):
        return "Nome:{titulo} Categorias:{categorias} Pais:{pais} Sinopse:{sinopse} Duracao:{duracao} Ano:{ano} Classificacao:{classificacao}".format(
        titulo=self.titulo, categorias=self.categorias, pais=self.pais,
        sinopse=self.sinopse, duracao=self.duracao, ano=self.ano, classificacao=self.classificacao
    )
    
class atuacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)
    membro = models.ForeignKey(Membros, on_delete=models.PROTECT)
    tipoAtuar = models.ForeignKey(tipoAtuacao, on_delete=models.PROTECT)
    personagem = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
    	return "Filme:{} Membro:{} Tipo:{} Personagem:{}".format(self.filme, self.membro, self.tipoAtuar, self.personagem)

    
