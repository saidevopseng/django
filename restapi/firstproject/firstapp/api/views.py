 
from rest_framework import viewsets
from firstapp.api.serializers import HydJobsSerializer
from firstapp.models import HydJobs

# create your views here
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    queryset=HydJobs.objects.all()
    serializer_class=HydJobsSerializer
    