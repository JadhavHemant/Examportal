from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import *
from ExamApp.Serializer import *

class ContentApi(APIView):
    def get(self,request,format=None):
        models=ContentModel.objects.all()
        serializer=ContentSerializer(models,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ContentWiseAPIView(APIView):
    def get(self, request, content_id):
        cities = ContentQuestionsModel.objects.filter(content_id=content_id)
        serializer = ContentQuestionSerializer(cities, many=True)
        return Response(serializer.data)


    
class ContentUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return ContentModel.objects.get(pk=pk)
        except ContentModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = ContentSerializer(topic)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = ContentSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                   
    