from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
#from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from watchlist_app.api.serializers import WatchlistSerializer, StreamingPlatformSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamingPlatform, Review

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        movie_id = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=movie_id)

        review_user = self.request.user

        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie.")
 
        serializer.save(watchlist=movie, review_user=review_user)

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']
        return Review.objects.filter(watchlist=movie_id)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

###Watchlist###
class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
### Streaming Platform###

# class StreamingPlatform(viewsets.ViewSet):
#     def list(self, request):
#         querySet = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(querySet, many=True)
#         return Response(serializer.data)
#     def retrieve(self, request, pk=None):
#         querySet = StreamingPlatform.objects.get(pk=pk)
#         platform = get_object_or_404(StreamingPlatform, pk=pk)
#         serializer = StreamingPlatformSerializer(platform)
#         return Response(serializer.data)

class StreamingPlatformListAV(APIView):
    def get(self, request):
        streamingPlatforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streamingPlatforms, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamingPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            streamingPlatform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'Error': 'Streaming Platformn not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(streamingPlatform, context={'request': request})   #request for hyperlinked serializer*
        return Response(serializer.data)
    
    def put(self, request, pk):
        streamingPlatform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(streamingPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        streamingPlatform = StreamingPlatform.objects.get(pk=pk)
        streamingPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)