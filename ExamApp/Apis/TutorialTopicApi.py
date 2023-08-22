from rest_framework.views import APIView
from ExamApp.models import *
from ExamApp.Serializer import *
from rest_framework.response import Response
from rest_framework.views import status

class TutorialTopicApi(APIView):
    def get(self,request,format=None):
        model=TutorialModel.objects.all()
        serializer=TutorialTopicSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=TutorialTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ContentWiseRestApi(APIView):
    def get(self, request, id):
        content = TutorialContentModel.objects.filter(tutorial_id=id)
        serializer = TutorialContentSerializer(content, many=True)
        return Response(serializer.data)
    
    
class TutorialTopicUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return TutorialModel.objects.get(pk=pk)
        except TutorialModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        tutorial = self.get_object(pk)
        serializer = TutorialTopicSerializer(tutorial)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = TutorialTopicSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               