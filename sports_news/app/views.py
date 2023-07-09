from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import Sports, News, Matches, Tours
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from app.serializers import NewsSerializer

class NewsViewSet(ViewSet):


    def create(self, request):
        
        serializer = NewsSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST, data={"error": serializer.errors})
        
        serializer.save()

        return Response(status=HTTP_200_OK, data="News successfully created")
  
    
    def get_sport_news(self, request, sport_id):
        """
        Get news by sport id
        """
        
        # checking if requested sport_id is valid

        if not Sports.objects.filter(id = sport_id).exists():
            return Response(status=HTTP_400_BAD_REQUEST, data={"error":"Invalid sports"})
        
        # fetching news for sport_id

        news_queryset = News.objects.filter(sportid = sport_id)

        if not news_queryset.exists():
            return Response(status=HTTP_200_OK, data = "No news found")
        
        news_data = []
        for news_instance in news_queryset:
            news_data.append({"title": news_instance.title, "description": news_instance.description})

    
        return Response(status=HTTP_200_OK, data = news_data)
        
    
    def get_tour_news(self, request, tour_id):
        """
        Get news by tour id
        """
        # checking if requested tour_id is valid

        if not Sports.objects.filter(id = tour_id).exists():
            return Response(status=HTTP_400_BAD_REQUEST, data={"error":"Invalid sports"})
        
        # fetching news for tour_id

        news_queryset = News.objects.filter(tourid = tour_id)

        if not news_queryset.exists():
            return Response(status=HTTP_200_OK, data = "No news found")
        
        news_data = []
        for news_instance in news_queryset:
            news_data.append({"title": news_instance.title, "description": news_instance.description})
        
    
        return Response(status=HTTP_200_OK, data = news_data)

    def get_match_news(self, request, match_id):
        """
        Get new by match id
        """
        # checking if requested match_id is valid

        if not Matches.objects.filter(id = match_id).exists():
            return Response(status=HTTP_400_BAD_REQUEST, data={"error":"Invalid sports"})
        
        # fetching news for match_id

        news_queryset = News.objects.filter(matchid = match_id)
        
        if not news_queryset.exists():
            return Response(status=HTTP_200_OK, data = "No news found")
        
        news_data = []
        for news_instance in news_queryset:
            news_data.append({"title": news_instance.title, "description": news_instance.description})
        
    
        return Response(status=HTTP_200_OK, data = news_data)
