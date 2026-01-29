from rest_framework import serializers
from .models import Product
from .models import Author, Book    # dodane w ramach task 9 i 10 lesson 25

#   Dodane w ramach task 2 Lesson 25
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

#   Dodane w ramach task 9 Lesson 25
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )
    author_name = serializers.StringRelatedField(
        source="author",
        read_only=True
    )

    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author", "author_name"]

