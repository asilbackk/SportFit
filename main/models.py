from django.db import models

class Sport_Type(models.Model):
    
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='sport_type/')

    def __str__(self):
        return self.name


class Viloyat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Shaxar(models.Model):
    name = models.TextField(max_length=255)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Arena(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(Shaxar, on_delete=models.CASCADE)
    type = models.ForeignKey(Sport_Type, on_delete=models.CASCADE)
    toztash_joyi  = models.BooleanField(default=False)
    dush = models.BooleanField(default=False)
    orindiq = models.BooleanField(default=False)
    ochish_vaqti = models.TimeField()
    yopish_vaqti = models.TimeField()
    trener = models.CharField(max_length=255)
    bio = models.TextField(max_length=255)
    oxirgi_tamir = models.DateField()
    maydon = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Arena_Index(models.Model):
    name = models.TextField(max_length=255)
    img  = models.ImageField(upload_to='Arena_Index')

    def __str__(self):
        return self.name



class Img(models.Model):
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE,related_name='image')
    img = models.ImageField(upload_to='arena/')

