from django.db import models
class Mobi(models.Model):
    name = models.CharField(max_length=55,
                            verbose_name='Marka telefon')
    camera= models.CharField(max_length=55,verbose_name='Kamera telefona')
    memory = models.CharField(max_length=55)
    year_realised = models.DateTimeField()
    price = models.DecimalField(decimal_places=3,max_digits=7)
    image = models.ImageField(upload_to="images/",null=True,blank=True)




# Create your models here.
