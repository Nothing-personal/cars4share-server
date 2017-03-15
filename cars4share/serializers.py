from rest_framework import serializers
import cars4share.models as models


# While using Meta class inside, methods create and update will be set automatically
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
