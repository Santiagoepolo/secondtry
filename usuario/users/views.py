from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializerRead, UserSerializerWrite, UserSerializer3
from .models import User


# Create your views here.
class UserView(APIView):
    
    def get_serializer_class (self,request):
        if request.method == 'GET':
            return UserSerializerRead
        return UserSerializerWrite

    #Para consultar todos los usuarios
    def get(self,request,pk=None, format = None):
        if pk:
            condition_many = False
            queryset= User.objects.get(pk=pk,deleted_at__isnull=True)
        else:
            condition_many = True
            queryset = User.objects.filter(deleted_at__isnull=True)
        serializer=self.get_serializer_class(request)
        serialized_users = serializer(queryset, many=condition_many)
        return Response(serialized_users.data, status=200)
        
    def post(self, request, format =None):
        print(request.data)
        serializer = self.get_serializer_class(request)(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
        
    def put(self,request,pk=None,format=None):
        serielizer=self.get_serializer_class
        queryset= User.objects.get(pk=pk)
        serielizer=self.get_serializer_class(request)(instance=queryset, data=request.data)
        serielizer.is_valid(raise_exception=True)
        update_user=serielizer.update(queryset,serielizer.validated_data)
        return Response(UserSerializerRead(update_user).data,status=200)
        
    def delete(self,request,pk=None,format=None):
            queryset=User.objects.get(pk=pk)
            queryset.soft_delete()
            return Response(status=200)
        