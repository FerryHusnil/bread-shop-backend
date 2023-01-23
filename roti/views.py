from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import RotiModel
from .serializers import RotiModelSerializer

class RotiModelListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        data = RotiModel.objects.filter(owner=request.user)
        serialized = RotiModelSerializer(
            data, many=True)
        response = {
            "status": 200,
            "message": "success",
            "username": request.user.username,
            "data": serialized.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RotiModelSerializer(data={
        'owner': request.user.id,
        'name': request.data["name"],
        'expired_date': request.data["expired_date"],
        'description': request.data["description"],
        'image': request.data["image"],      
        })
        
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status': "Create success",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RotiModelDetailView(APIView):
    def patch(self, request, roti_id):
        instance = RotiModel.objects.get(id=roti_id)
        serializer = RotiModelSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': "Update success",
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, roti_id):
        instance = RotiModel.objects.get(id=roti_id)
        instance.delete()
        return Response({
            'status': 'Deleted',
        }, status=status.HTTP_201_CREATED)