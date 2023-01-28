from rest_framework import serializers
from .models import TelegrafModel

class MainSerializer(serializers.ModelSerializer):
    '''List of all fields'''

    class Meta:
        model = TelegrafModel
        fields = ('uri', 'created', 'file', 'content') # exclude = ('file',)
