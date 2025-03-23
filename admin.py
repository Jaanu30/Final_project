from django.contrib import admin
from .models import SentimentReview

class SentimentReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'sentiment', 'created_at')  # Display relevant fields in the admin list view
    list_filter = ('sentiment',)  # Add filters for sentiment
    search_fields = ('text',)  # Add search capability for the review text
    ordering = ('-created_at',)  # Order by creation date descending

# Register the SentimentReview model with the SentimentReviewAdmin class
admin.site.register(SentimentReview, SentimentReviewAdmin)
