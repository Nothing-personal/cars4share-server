from django.test import TestCase
from cars4share.models import Feedback


# Create your tests here.
class FeedbackTestCase(TestCase):
    def set_up(self):
        feedback = Feedback.objects.create(
            message="Test feedback",
            rating=5
        )
