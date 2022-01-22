from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()


class RefreshSerializer(serializers.Serializer):
    refresh=serializers.CharField()