from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    job_title = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{ self.name } <{ self.email }>"
