from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import userSerializer


@api_view(['GET'])
def get_user(request):
    users = user.objects.all()
    serializer = userSerializer(users, many = True)
    return Response(serializer.data)



@api_view(['POST'])
def create_user(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create  delete and update option

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user_obj = user.objects.get(pk=pk)
        user_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_user(request, pk):
    try:
        user_obj = user.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = userSerializer(user_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
