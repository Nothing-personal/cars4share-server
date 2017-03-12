from django.test import TestCase
from cars4share.models import Feedback


# Create your tests here.
class FeedbackTestCase(TestCase):

    @staticmethod
    def set_up():
        Feedback.objects.create(
            message='test',
            rate=5
        )
