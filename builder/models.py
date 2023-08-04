from django.db import models

# Create your models here.


# signup
class Users(models.Model):
    SrNo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField( max_length=200)
    contact = models.IntegerField(null=True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
 
# resume docx UPLOAD
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    contact_information = models.TextField()
    resume_objective = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    extracurricular_activities = models.TextField()
    skills = models.TextField()
    hobbies_and_interests = models.TextField()
    additional_sections = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='static\img\products')
    tags = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.title