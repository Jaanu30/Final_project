from django.db import models

class SentimentReview(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to current time on creation

    def __str__(self):
        return f"{self.sentiment} - {self.text[:50]}..."  # Display first 50 characters of the review

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} - {self.sentiment}"
