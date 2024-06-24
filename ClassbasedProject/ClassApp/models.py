from django.db import models



# Create your models here.
class regmodel(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=80)
    phone = models.IntegerField()
    password = models.CharField(max_length=10)

class StudentDetails(models.Model):
    student_name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')
    dob = models.DateField()
    email = models.EmailField(max_length=80)
    maths_score = models.IntegerField()
    Physics_score = models.IntegerField()
    Chemistry_score = models.IntegerField()

    #total_score = models.IntegerField()

    def __str__(self):
        return self.student_name
    def __str__(self):
        return self.dob
    def __str__(self):
        return self.email
    def __int__(self):
        return self.maths_score
    def __int__(self):
        return self.Physics_score
    def __int__(self):
        return self.Chemistry_score

   # def __int__(self):
         #self.total_score = self.maths_score + self.Physics_score + self.Chemistry_score

class Uploadimage(models.Model):
    itemname = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.itemname

