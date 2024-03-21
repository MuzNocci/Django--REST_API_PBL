from rest_framework import serializers
from rest_api.models import User, UserTasks



class UserSerializer(serializers.ModelSerializer):


    class Meta:

        model = User
        fields = '__all__'



class UserTaskSerializer(serializers.ModelSerializer):


    class Meta:

        model = UserTasks
        fields = ['user_nickname', 'user_task']