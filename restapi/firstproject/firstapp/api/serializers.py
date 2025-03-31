from rest_framework.serializers import ModelSerializer
from firstapp.models import HydJobs

class HydJobsSerializer(ModelSerializer):
    class Meta:
        model=HydJobs
        fields='__all__'

