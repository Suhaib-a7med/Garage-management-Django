from django.db import models

# Create your models here.
class Mechanics(models.Model):
    image = models.ImageField(upload_to="mechanics", default="default.jpg")
    name = models.CharField(max_length=255)
    proffesion = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'mechanics'

class Reservations(models.Model):
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    bookDate = models.DateField()
    bookTime = models.TimeField()
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=255, null=True,)
    mechanic_id = models.ForeignKey(Mechanics, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'reservation'