# myapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the session is authenticated and has expired
        if request.user.is_authenticated and not request.session.get_expiry_age() > 0:
            # Redirect to the login page
            return redirect(reverse('myapp:login'))  # Adjust the URL name as needed

        response = self.get_response(request)
        return response
