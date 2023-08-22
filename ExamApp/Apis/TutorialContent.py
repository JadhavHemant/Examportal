from rest_framework.views import APIView
from ExamApp.models import *
from ExamApp.Serializer import *
from rest_framework.response import Response
from rest_framework.views import status

class TContentApi(APIView):
    def get(self,request,format=None):
        model=TutorialContentModel.objects.all()
        serializer=TutorialContentSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=TutorialContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TDataWiseRestApi(APIView):
    def get(self, request, id):
        contdata = TutorialsData.objects.filter(tutorial_content_id=id)
        serializer = TutorialDataSerializer(contdata, many=True)
        return Response(serializer.data)

class ContentWiseVedioRestApi(APIView):
    def get(self, request, id):
        contdata = VedioModel.objects.filter(tutorial_content_id=id)
        serializer = VedioDataSerializer(contdata, many=True)
        return Response(serializer.data)    
    
class TContentUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return TutorialContentModel.objects.get(pk=pk)
        except TutorialContentModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TutorialContentSerializer(topic)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = TutorialContentSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               