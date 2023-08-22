from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import *
from ExamApp.Serializer import *

class ExamQuestionApi(APIView):
    def get(self,request,format=None):
        models=ExamQuestionModel.objects.all()
        serializer=ExamSerializer(models,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ExamidWiseRestApi(APIView):
    def get(self, request, exam_id):
        content = ExamQuestionModel.objects.filter(exam_id=exam_id)
        serializer = ExamSerializer(content, many=True)
        return Response(serializer.data)
                   
    