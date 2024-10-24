from django.db import models
from model_utils import Choices
from django.core.validators import FileExtensionValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed


class MainPage(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    main_img = models.FileField()
    description = models.CharField(max_length=256)
    duration = models.CharField("duration",max_length=50)
    lesson_duration = models.CharField("lesson_duration",max_length=50)
    lesson_days = models.CharField("day_lessons",max_length=256)
    age_limit = models.CharField("age limit",max_length=100)
    requirement = models.CharField(max_length=256)
    about = models.CharField(max_length=256)

    def __str__(self):
       return f"{self.title}"

    class Meta:

       db_table = "main"
       verbose_name = "main"
       verbose_name_plural = "mains"


class Footer(models.Model):
    instagram = models.CharField(max_length=256)
    youtube = models.CharField(max_length=256)
    facebook = models.CharField(max_length=256)
    reception_time = models.CharField(max_length=256)
    lunch = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
       return f"{self.instagram}"

    class Meta:

       db_table = "footer"
       verbose_name = "footer"
       verbose_name_plural = "footer"



class Gender(models.TextChoices):
    Male = "Erkak", ("Erkak")
    FeMale = "Ayol", ("Ayol")


class YesNo(models.TextChoices):
    Yes = "Yes", ("yes")
    No = "No", ("no")
   
class StartAppCategory(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "startappcategory"
        verbose_name = "startappcategory"
        verbose_name_plural = "startappcategories"
        
    

class Purposes(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "purpose"
        verbose_name = "purpose"
        verbose_name_plural = "purpose"
    




class Registration(models.Model):
   full_name = models.CharField(max_length=256)
   gender = models.CharField(max_length=256,choices=Gender.choices)
   date_birth = models.DateField(null=True, blank=True)
   address = models.CharField(max_length=256)
   phone = models.CharField(max_length=256)
   startap_name = models.CharField(max_length=256)
   category = models.ManyToManyField(StartAppCategory)
   another_category=models.CharField(max_length=256, null=True)
   about_startapp = models.CharField(max_length=256) 
   about_team = models.CharField(max_length=256)
   purpose = models.ManyToManyField(Purposes)
   project_prototype = models.CharField(max_length=256,choices=YesNo.choices)
   startap_image = models.FileField(upload_to= "startap_image/%Y/%m")
   presentation = models.FileField(
        ("presentation"),
        validators=[FileExtensionValidator(["pptx", "pdf"])],
        upload_to= "presentation/%Y/%m"
    )
   agree = models.BooleanField(default=False)

   def __str__(self):
       return f"{self.full_name}"

   class Meta:
       db_table = "form"
       verbose_name = "form"
       verbose_name_plural = "forms"

