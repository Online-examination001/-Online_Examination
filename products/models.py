from django.db import models


from django.db.models.signals import pre_save

class Products(models.Model):
    unique_id = models.CharField( verbose_name= "unique id",unique=True,editable=False,max_length=50)
    title = models.CharField(verbose_name="Short title", max_length=255)
    description = models.CharField(verbose_name="Product description",max_length=1000 )
    price =models.FloatField(verbose_name="Price per unique use")
    date_added = models.DateTimeField(verbose_name="Added date", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date updated",auto_now=True )

    def __str__(self):
        return self.unique_id + " - " + self.title

def presave_product_reciever(sender, instance, *args, **kwargs ):
    if not instance.unique_id:
        instance.unique_id = "PD"+instance.title[0:5]
        counter = 1
        unique_id = instance.unique_id
        while Products.objects.filter(unique_id=unique_id):
            unique_id =  unique_id + str(counter)
            counter += 1
            instance.unique_id = unique_id
       
            
            
pre_save.connect( presave_product_reciever,sender=Products)
