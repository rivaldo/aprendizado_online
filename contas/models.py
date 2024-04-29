from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfil_foto', blank=True, null=True)
    
    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def criar_ou_atualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    instance.profile.save()
    
    