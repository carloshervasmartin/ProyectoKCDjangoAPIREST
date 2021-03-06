from rest_framework.views import APIView
from rest_framework.response import Response
from entries.models import EntryModel
from entries.api.serializers import EntrySerializer

class EntryListAPI(APIView):
    def get(self, request):
        entries = EntryModel.objects.all()
        
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = EntrySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = 201)
             
        return Response(data=serializer.errors, status=400)
    
class EntryListDetailAPI(APIView):
    def get(self, request, pk):
        entry = EntryModel.objects.get(pk=pk)
        
        serializer = EntrySerializer(entry)
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        entry = EntryModel.objects.get(pk=pk)
        
        serializer = EntrySerializer(entry, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = 201)
             
        return Response(data=serializer.errors, status=400)
    
    def delete(self, request, pk):
        entry = EntryModel.objects.get(pk=pk)
        
        entry.delete()
        
        return Response(status=204)
    