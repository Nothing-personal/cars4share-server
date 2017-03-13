from rest_framework_mongoengine import serializers
import cars4share.models as models


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

# No need to serialize EmbeddedDocument, as DRF-Mongoengine does this automatically
