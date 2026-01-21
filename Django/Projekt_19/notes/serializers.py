#    dodane w ramach task 6 lesson 25
from rest_framework import serializers
from .models import Note

#   Dodane w ramach task 10 Lesson 25
class NoteSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Tytuł notatki musi mieć co najmniej 5 znaków."
            )
        return value

    class Meta:
        model = Note
        fields = '__all__'

