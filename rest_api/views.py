from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_api.models import User, UserTasks
from rest_api.serializers import UserSerializer, UserTaskSerializer
import json



@api_view(['GET'])
def get_users(request):


    if request.method == 'GET':
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)


    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT'])
def get_user(request, nick):


    try:

        user = User.objects.get(user_nickname=nick)

    except:

        return Response(status=status.HTTP_404_NOT_FOUND)


    match request.method:


        case 'GET':

            serializer = UserSerializer(user)

            return Response(serializer.data)


        case 'PUT':

            serializer = UserSerializer(user, data=request.data)
            
            if serializer.is_valid() and nick == request.data['user_nickname']:

                serializer.save()

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
            else:
                
                return Response(status=status.HTTP_404_NOT_FOUND)


        case _:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):


    match request.method:


        case 'GET':

            try:

                if request.GET['user']:

                    try:

                        user = User.objects.get(user_nickname=request.GET['user'])
                        serializer = UserSerializer(user)
                        
                        return Response(serializer.data)
                    
                    except:

                        return Response(status=status.HTTP_404_NOT_FOUND)
                
                else:

                    return Response(status=status.HTTP_400_BAD_REQUEST)

            except:

                    return Response(status=status.HTTP_400_BAD_REQUEST)


        case 'POST':

            new_user = request.data
            serializer = UserSerializer(data=new_user)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            return Response(status=status.HTTP_400_BAD_REQUEST)


        case 'PUT':

            try:

                updated_user = User.objects.get(pk=request.data['user_nickname'])
            
            except:

                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(updated_user, data=request.data)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)


        case 'DELETE':

            try:

                user_to_delete = User.objects.get(pk=request.data['user_nickname'])
                user_to_delete.delete()

                return Response(status=status.HTTP_202_ACCEPTED)
            
            except:

                return Response(status=status.HTTP_400_BAD_REQUEST)


        case _:

            return Response(status=status.HTTP_400_BAD_REQUEST)