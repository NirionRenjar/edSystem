from django.db import models


class AccessLevels(models.Model):
    level = models.CharField(max_length=120)


class User(models.Model):
    name = models.CharField(max_length=120)
    access_level = models.ForeignKey(AccessLevels, on_delete=models.PROTECT)


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    duration = models.PositiveSmallIntegerField()


class Product(models.Model):
    owner = models.CharField(max_length=120)
    user_access = models.ForeignKey(AccessLevels, on_delete=models.PROTECT)
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class ViewStatistics(models.Model):
    viewLesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewingUser = models.ForeignKey(User, on_delete=models.CASCADE)
    viewingDuration = models.PositiveSmallIntegerField()
    videoWatched = models.BinaryField()

