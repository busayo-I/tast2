from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    
    #def validate(self, value):
        #if any(char.isdigit() for char in value):
           #raise serializers.validateError('NAME SHOULD BE ONLY LETTERS.')
           #return validate()