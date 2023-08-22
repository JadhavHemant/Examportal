from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import *
from ExamApp.Serializer import *

class StudentExamApi(APIView):
    def get(self,request,format=None):
        models=CandidateExamModel.objects.all()
        serializer=CandidateExamSerializer(models,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=CandidateExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class StudentExamUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return CandidateExamModel.objects.get(pk=pk)
        except CandidateExamModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = CandidateExamSerializer(topic)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = CandidateExamSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                   
    