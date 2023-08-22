from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import *
from ExamApp.Serializer import *
# from django.contrib.auth import authenticate

class AddStudentApi(APIView):
    def get(self,request,format=None):
        models=CandidateModel.objects.all()
        serializer=CandidateSerializer(models,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class StudentLoginApi(APIView):
    def post(self, request):
        candidate_email=request.data.get('candidate_email')
        password=request.data.get('password')  
        try:
            Candidate=CandidateModel.objects.get(candidate_email=candidate_email, password=password)
            return Response({'id': Candidate.id}, status=status.HTTP_200_OK)
        except CandidateModel.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)   
            
        
class IdWiseStudentData(APIView):
      def get(self, request, id):
        try:
            model = CandidateModel.objects.get(pk=id)
        except CandidateModel.DoesNotExist:
            return Response({"error": "Candidate not found"}, status=404)      
        serializer = CandidateSerializer(model)
        return Response(serializer.data)
    
class AddStudentUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return CandidateModel.objects.get(pk=pk)
        except CandidateModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
    
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = CandidateSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = CandidateSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                   
    