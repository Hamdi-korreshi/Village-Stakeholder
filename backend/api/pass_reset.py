# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import ChangePasswordSerializer
import sys

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            print("hamdi:", serializer.data, file=sys.stderr)
        print("Serializer validated data:", serializer.validated_data, file=sys.stderr)
        print("Request data:", request.data, file=sys.stderr)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data["old_pass"]):
                return Response(
                    {"detail": "Current password is incorrect."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(serializer.data["new_pass"])
            user.save()
            return Response(
                {"detail": "Password updated successfully."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
