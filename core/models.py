from django.db import models



# O'qituvchi haqida ma'lumotlar
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teachers/')  

    def __str__(self):
        return self.name


# Kurslar
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField() 
    start_date = models.DateField()
    teacher = models.ForeignKey(
        Teacher,
        related_name='courses',  
        on_delete=models.SET_NULL,  
        null=True, 
        blank=True 
    )

    def __str__(self):
        return self.title


# Yangiliklar
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Fikrlar
class Feedback(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
