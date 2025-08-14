from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer
import qrcode
from io import BytesIO
from django.http import HttpResponse

def get_full_short_url(request, code):
    """Builds the absolute short URL."""
    return request.build_absolute_uri(f"/{code}")

@api_view(["POST"])
def create_short_url(request):
    """
    Accepts a long URL and returns a shortened URL.
    """
    original_url = request.data.get("url")

    if not original_url:
        return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = URLSerializer(data={"original_url": original_url})
    if serializer.is_valid():
        url_obj = serializer.save()
        short_url = get_full_short_url(request, url_obj.short_code)
        return Response({"short_url": short_url}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def redirect_url(request, code):
    """
    Redirects the given short code to the original URL.
    """
    try:
        url_obj = URL.objects.get(short_code=code)
        return redirect(url_obj.original_url)
    except URL.DoesNotExist:
        return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(["GET"])
def qr_code(request, code):
    try:
        url_obj = URL.objects.get(short_code=code)
        img = qrcode.make(url_obj.original_url)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return HttpResponse(buffer, content_type="image/png")
    except URL.DoesNotExist:
        return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)