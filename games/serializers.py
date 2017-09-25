from rest_framework import serializers
from games.models import Game

"""
Django REST Framework uses a two-phase process for serialization. The serializers are
mediators between the model instances and Python primitives. Parser and renderers handle
as mediators between Python primitives and HTTP requests and responses. We will
configure our mediator between the Game model instances and Python primitives by
creating a subclass of the rest_framework.serializers.Serializer class to declare
the fields and the necessary methods to manage serialization and deserialization

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    game_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)
"""
class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'release_date',
            'game_category',
            'played'
        )


#create methods received the validated data in validated_data argument
    #code creates and returns a new game instance based on received validated data
    def create(self, validated_data):
        return Game.objects.create(**validated_data)


    """
    The update method receives an existing Game instance that is being updated and the new
    validated data in the instance and validated_data arguments. The code updates the
    values for the attributes of the instance with the updated attribute values retrieved from the
    validated data, calls the save method for the updated Game instance and returns the
    updated and saved instance.
    """
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date',
                                                   instance.release_date)
        instance.game_category = validated_data.get('game_category',
                                                    instance.game_category)
        instance.played = validated_data.get('played', instance.played)

        instance.save()

        return instance
