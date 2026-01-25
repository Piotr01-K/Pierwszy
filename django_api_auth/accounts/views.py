from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page   #  dodane lesson 27 task 3
from django.utils.decorators import method_decorator   #  dodane lesson 27 task 3
from rest_framework.permissions import AllowAny   #  dodane lesson 27 task 3


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username
        })
    
#  dodane lesson 27 task 3
@method_decorator(cache_page(60), name='get')
class ProtectedView(APIView):
    #   permission_classes = [IsAuthenticated]  # zahashowany na czas wykonania lesson 27 task 3
    permission_classes = [AllowAny]   #  dodane na czas wykonania lesson 27 task 3
    def get(self, request):
        print(">>> WIDOK WYKONUJE SIĘ (nie z cache)")
        return Response({
            #   "username": request.user.username
            "message": "cache test",
        })
