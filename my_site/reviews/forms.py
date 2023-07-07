from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {"username": "Your Name", "review_text": "Your Feedback"}
        error_messages = {
            "username": {
                "required": "Your name must not be null!",
                "max_length": "Please, enter a shorter name!",
            }
        }
