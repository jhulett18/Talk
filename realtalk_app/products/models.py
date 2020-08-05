from django.db import models

class Products(models.Model): #brings in inherited models from models object
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    
