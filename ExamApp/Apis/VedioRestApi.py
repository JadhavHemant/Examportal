from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ExamApp.models import VedioModel
from ExamApp.Serializer import VedioDataSerializer
from ExamApp.VedioUpload import uploaded_file  
class VedioApi(APIView):
    def get(self, request, format=None):
        model = VedioModel.objects.all()
        serializer = VedioDataSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        uploaded_file(request.FILES.get('vedio'))  
        data = request.data
        serializer = VedioDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VedioUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return VedioModel.objects.get(pk=pk)
        except VedioModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND   
        
    def get(self, request, pk, format=None):
        vediod = self.get_object(pk)
        serializer = VedioDataSerializer(vediod)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model = self.get_object(pk)
        uploaded_file(request.FILES.get("vedio"))  
        data = request.data
        serializer = VedioDataSerializer(model,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    