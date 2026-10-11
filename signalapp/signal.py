from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Mymodel

@receiver(post_save, sender=Mymodel)
def my_model_post_save_handler(sender, instance, created, **kwargs):
    if created:
        print(f"A new MyModel instance was created:{instance}")
    else:
        print(f"MyModel instnace  was update :{instance}")


