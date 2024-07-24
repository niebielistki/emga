from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='songs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class AnalysisResult(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    result = models.JSONField()
    analyzed_at = models.DateTimeField(auto_now_add=True)
