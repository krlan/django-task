from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class School(models.Model):
    img = models.URLField("Image URL", max_length=200)
    name = models.CharField("School name", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-name"]
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school:school", kwargs={
            "slug_school": self.slug
        })


class Classroom(models.Model):
    school = models.ForeignKey(School)
    number = models.IntegerField("Classroom number", validators=[MaxValueValidator(100000),
                                                                MinValueValidator(0)])

    class Meta:
        ordering = ["-number"]
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return '{0} {1}'.format(self.school, self.number)

    def get_absolute_url(self):
        return reverse("school:classroom", kwargs={
            "slug_school": self.school.slug,
            "class": self.pk
        })


class Student(models.Model):
    classroom = models.ForeignKey(Classroom)
    name = models.CharField("Full name", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-name"]
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school:student", kwargs={
            "slug_school": self.classroom.school.slug,
            "class": self.classroom.pk,
            "slug": self.slug
        })
