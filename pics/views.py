from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PicsView(APIView):
    authentication_classes = [TokenAuthentication]  # Define que a autenticação será feita por token
    permission_classes = [IsAuthenticated] # valida se foi autenticado com o token

    def get(self, request):
            
        return Response({'message': 'Hello, world!'})

