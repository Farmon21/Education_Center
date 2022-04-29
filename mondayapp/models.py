from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    teaching_course = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.full_name


class Application(models.Model):
    client_name = models.CharField(max_length=200)
    client_last_name = models.CharField('Client last name', max_length=255, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    client_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Client name: {self.client_name},  Phone number: {self.client_phone_number}"