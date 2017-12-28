from django.contrib.auth.models import User
from polls.models import Question
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User.
    """
    url = serializers.HyperlinkedIdentityField(view_name="restapi:user-detail")    
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Question.
    """
    url = serializers.HyperlinkedIdentityField(view_name="restapi:question-detail")  
    class Meta:
        model = Question
        fields = ('question_text','pub_date','url')