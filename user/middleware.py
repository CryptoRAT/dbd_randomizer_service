


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log or print request information
        print("cookies: ", list(request.COOKIES))
        response = self.get_response(request)
        return response