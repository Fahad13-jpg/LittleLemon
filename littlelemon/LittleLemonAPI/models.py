from django.db import models

# Create your models here.
class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    
    def __str__(self):
        def get_item(self):
            return f'{self.title} : {str(self.price)}'