from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import *
from ExamApp.Serializer import *

class QuestionApi(APIView):
    def get(self,request,format=None):
        models=ContentQuestionsModel.objects.all()
        serializer=ContentQuestionSerializer(models,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=ContentQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class QuestionUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return ContentQuestionsModel.objects.get(pk=pk)
        except ContentQuestionsModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = ContentQuestionSerializer(topic)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = ContentQuestionSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                   
    