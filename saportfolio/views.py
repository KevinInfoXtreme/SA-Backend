from rest_framework import viewsets
from .models import Project,Disponibilite
from .serializers import ProjectSerializer,DisponibiliteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DisponibilitesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        disponibilites = Disponibilite.objects.all()
        serializer = DisponibiliteSerializer(disponibilites, many=True)
        return Response(serializer.data)