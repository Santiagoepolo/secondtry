from django.db import models
from django.utils import timezone

# Create your models here.

#aqui empezamos a definir el módelo user, el cual debe heredar models.Model, lo que indica que es un modelo de django
class User(models.Model):
    username=models.CharField(max_length=20,unique=True,help_text="El nombre debe ser único")
    password=models.CharField(max_length=50)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=True,blank=True)
    update_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True,blank=True)

    
#Este es un método para representar al objeo string cuando lo imprimamos, asi veremos el nombre y no algo como "user1"
    def __str__(self) -> str:
        return f"{self.username} {self.last_name}"
    
    class Meta:
        db_table= 'users'
        
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.deleted_at = None
        self.save()
        
    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()
    
    @property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    