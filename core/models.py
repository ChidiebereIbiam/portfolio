from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    about_me = models.TextField()
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=250)
    profile_photo = models.ImageField(upload_to="profile/")
    cv = models.FileField(upload_to='cv/')
    years_of_experience = models.CharField(max_length=250)
    happy_clients = models.CharField(max_length=250)
    awards = models.CharField(max_length=250)
    github = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    google = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    icon_class = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    field_of_study = models.CharField(max_length=250)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.school} | {self.degree} "

class Experience(models.Model):
    title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, blank=True)
    current_job = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.company_name}"

class Project(models.Model):
    title = models.CharField(max_length=250, null=True)
    project_info = models.TextField()
    client = models.CharField(max_length=250)
    industry = models.CharField(max_length=250)
    technology = models.CharField(max_length=250)
    date = models.DateField()
    url = models.URLField(max_length=200)
    image1 = models.ImageField(upload_to="project/")
    image2 = models.ImageField(upload_to="project/", null=True, blank=True)
    image3 = models.ImageField(upload_to="project/", null=True, blank=True)


    def __str__(self):
        return f"{self.title} | {self.client}"

class Contact (models.Model):
    address = models.TextField()
    phone1 = models.CharField(max_length=250)
    phone2 = models.CharField(max_length=250,null=True, blank = True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
    

class Skills (models.Model):
    name = models.CharField(max_length=250, unique=True)
    level_of_expertise = models.IntegerField(default=0)

    def __str__(self):
        return self.name