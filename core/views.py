from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from core.tasks import send_alert  # ✅ Add this import
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    send_alert.delay("🚀 Someone just accessed the public view!")
    return Response({"message": "This is a public endpoint. No login needed."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}! You have accessed a protected endpoint."})

def test_view(request):
    return JsonResponse({"test": "core.urls is working"})
