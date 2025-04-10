from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ContactModelSerializer


class ContactAddView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)