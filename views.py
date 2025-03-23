from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from .models import SentimentReview , Review # Import the model

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def index(request):
    reviews = SentimentReview.objects.all().order_by('-created_at')  # Fetch past reviews
    return render(request, 'index.html', {'reviews': reviews})

def sentiment_analysis(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        encoded_text = tokenizer(txt, return_tensors='pt')
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Determine sentiment
        sentiment = "Neutral"
        if scores[0] > scores[1] and scores[0] > scores[2]:
            sentiment = "Negative"
        elif scores[2] > scores[1] and scores[2] > scores[0]:
            sentiment = "Positive"

        # Save to database
        SentimentReview.objects.create(text=txt, sentiment=sentiment)

        # Retrieve updated reviews
        reviews = SentimentReview.objects.all().order_by('-created_at')

        return render(request, 'index.html', {'txt': txt, 'neg': scores[0], 'neu': scores[1], 'pos': scores[2], 'reviews': reviews})

    return render(request, 'index.html', {'reviews': SentimentReview.objects.all().order_by('-created_at')})

def review_history(request):
    reviews = SentimentReview.objects.all()  # Fetch all reviews
    return render(request, 'review_history.html', {'reviews': reviews})
