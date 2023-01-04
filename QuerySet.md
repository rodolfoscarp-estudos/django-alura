### Classe Base

```python
from django.db import models

class Pessoa(models.Model):
   nome = models.CharField(max_length=200)
   email = models.CharField(max_length=200)

 def __str__(self):
       return self.nome
```

### Insert

```python
pessoa = Pessoa(nome='Rodolfo', email='rodolfo@rodolfo.com')
pessoa.save()
```

### Listar Tudo

```python
Pessoa.objects.all()
```

### Buscar um registro

```python
pessoa = Pessoa.objects.get(nome='Rodolfo')
```

- Caso não encontre, levanta um exceção `DoesNotExist`
- Caso encontre mais de um objeto, levanta um exceção `MultipleObjectsReturned`

### Update

```python
pessoa.email = 'rodolfo@email.com'
pessoa.save()
```

### Filtar

```python
pessoa_procurada = Pessoa.objects.filter(nome='Rodolfo', email='rodolfo@rodolfo.com')
```

### Ordenar

```python
receitas_ordenadas = Pessoa.objects.order_by('-nome')
```

- Sinal negativo na frente do indica ordem decrescente, para ordem crescente deixe sem sinal
