from rest_framework.views import APIView
from ExamApp.models import *
from ExamApp.Serializer import *
from rest_framework.response import Response
from rest_framework.views import status

class DataApi(APIView):
    def get(self,request,format=None):
        model= TutorialsData.objects.all()
        serializer= TutorialDataSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer= TutorialDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class DataUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return  TutorialsData.objects.get(pk=pk)
        except  TutorialsData.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        tutorial = self.get_object(pk)
        serializer =  TutorialDataSerializer(tutorial)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer =  TutorialDataSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               