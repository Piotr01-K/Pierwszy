import time   #  dodane lesson 27 task 7
from django.core.cache import cache   #  dodane lesson 27 task 7
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

#  dodane lesson 27 task 7
class SelectiveCacheView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # szybkie dane (np. info o użytkowniku)
        user_info = {
            "user": request.user.username if request.user.is_authenticated else "anonymous"
        }

        # symulacja skomplikowanych obliczeń – cache
        cache_key = "expensive_calculation_result"
        expensive_result = cache.get(cache_key)

        if expensive_result is None:
            print("❌ Cache MISS – wykonuję skomplikowane obliczenia...")
            time.sleep(3)  # symulacja ciężkiej pracy
            expensive_result = {
                "value": 42,
                "source": "computed"
            }
            cache.set(cache_key, expensive_result, timeout=60)
        else:
            print("✅ Cache HIT – biorę wynik z cache")
            expensive_result["source"] = "cache"

        # odpowiedź
        return Response({
            "user_info": user_info,
            "expensive_part": expensive_result
        })
