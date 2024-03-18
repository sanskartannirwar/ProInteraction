from django.db import models

# Create your models here.


class Feedback(models.Model):
    username = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()

    def __str__(self):
         return self.username




class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    course_ch = (("Web Designing", "Web Designing"),
                 ("Full Stack Python", "Full Stack Python"),
                 ("Data Science", "Data Science"),
                 ("Web Development", "Web Development"))
    course = models.CharField(max_length=100, choices=course_ch)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name