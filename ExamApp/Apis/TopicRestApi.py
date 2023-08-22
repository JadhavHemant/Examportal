from rest_framework.views import APIView
from ExamApp.models import *
from ExamApp.Serializer import *
from rest_framework.response import Response
from rest_framework.views import status

class TpoicApi(APIView):
    def get(self,request,format=None):
        model=TopicModel.objects.all()
        serializer=TopicSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer=TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ContentWiseRestApi(APIView):
    def get(self, request, topic_id):
        content = ContentModel.objects.filter(topic_id=topic_id)
        serializer = ContentSerializer(content, many=True)
        return Response(serializer.data)
    
    
class TopicUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return TopicModel.objects.get(pk=pk)
        except TopicModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = TopicSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               