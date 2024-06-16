from django.db import models


# Create your models here.

class CoinFlip(models.Model):
    RESULT_CHOICES = [
        ('heads', 'Орел'),
        ('tails', 'Решка')
    ]
    coin_side = models.CharField(max_length=30, choices=RESULT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_flip(n):
        flips = CoinFlip.objects.order_by('-timestamp')[:n]
        stats = {'heads': 0, 'tails': 0}
        for flip in flips:
            if flip.result == 'heads':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats

    def __str__(self):
        return f'{self.coin_side} at {self.timestamp}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    public_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


