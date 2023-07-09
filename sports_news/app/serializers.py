from rest_framework import serializers
from app.models import News, Tours, Matches, Sports


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 50)
    discription = serializers.CharField(max_length = 1000, required = False)
    tourid = serializers.PrimaryKeyRelatedField(queryset = Tours.objects.all(), required = False)
    matchid = serializers.PrimaryKeyRelatedField(queryset = Matches.objects.all(), required = False)
    sportid = serializers.PrimaryKeyRelatedField(queryset = Sports.objects.all(), required = False)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        
        tourid = attrs.get("tourid")
        matchid = attrs.get("matchid")
        
        # validating if either tour or match will be provided for creating news 
        if not (tourid or matchid):
            raise serializers.ValidationError("Provide match or tour for creating news")
        
        # if news is created for a match, taking corresponding tour or sport before creating
        if matchid:
            attrs['tourid'] = matchid.tourid
            attrs['sportid'] = matchid.tourid.sportid
        
        # if news is created for a tour, taking corresponding sport before creating, in this case match will be null
        if tourid:
           attrs['sportid'] = tourid.sportid     

        return attrs


    def create(self, validated_data):
       return News.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.discription = validated_data.get('discription', instance.discription)

        return instance
    