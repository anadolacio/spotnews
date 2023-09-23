from django.db import models
from django.core.exceptions import ValidationError


def word_counter(word):
    text = word.split()
    if len(text) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, blank=False, validators=[word_counter]
    )

    content = models.TextField(
        null=False, blank=False, validators=[word_counter]
    )

    author = models.ForeignKey(
        "Users", on_delete=models.CASCADE, null=False, blank=False
    )

    created_at = models.DateField(
        null=False,
        blank=False,
    )

    image = models.ImageField(blank=True, null=True, upload_to="img/")

    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
