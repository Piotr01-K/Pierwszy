class PrintMethodMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Ten kod wykona się TYLKO RAZ – przy starcie serwera

    def __call__(self, request):
        # Ten kod wykona się przy każdym requeście
        print(f"Otrzymano zapytanie metodą {request.method}")

        response = self.get_response(request)

        # Możliwa modyfikacja response w przyszłości
        return response
