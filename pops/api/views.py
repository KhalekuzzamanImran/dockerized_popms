from rest_framework import viewsets, filters, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import generics
from pops.api.serializers import PopSerializer, PopDeviceSerializer, PopDeviceStatesSerializer, POPMSA006HistorySerializer, LatestPOPMSA006DataSerializer, POPMSA006DataSerializer
from pops.models import Pop, PopDevice, PopDeviceState
from django_filters.rest_framework import DjangoFilterBackend


class PopViewOnly(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PopSerializer
    # queryset = Pop.objects.filter(is_active=True)
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'network_status', 'user__id']
    search_fields = ['code', 'name']
    http_method_names = ['get', 'head']

    # dynamically set queryset
    def get_queryset(self):
        return self.request.user.user_pops.filter(is_active=True)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    # dynamically set queryset
    # def get_queryset(self):
    #     return self.request.user.user_pops.filter(is_active=True)

    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance).data
    #     pops = PopDevice.objects.filter(pop__id=instance.id)
    #     serializer_pop_devices = PopDeviceSerializer(pops, many=True).data
    #     serializer['pops'] = serializer_pop_devices
    #     return Response(serializer)


class PopDeviceViewOnly(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = PopDeviceSerializer
    queryset = PopDevice.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'pop_name']
    search_fields = ['code', 'name']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        pop_ids = [str(pop.id) for pop in self.request.user.user_pops.filter(is_active=True)]
        pops = PopDevice.objects.filter(pop_name__id__in=pop_ids)  # Here, pop_name is attributeName
        return pops


    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


class PopDeviceStatesViewSet(viewsets.ModelViewSet): 
    queryset = PopDeviceState.objects.filter(is_active=True)
    serializer_class = PopDeviceStatesSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get', 'head']

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)




# POPMS viewset
class LatestPOPMSA006ViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestPOPMSA006DataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'date']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = PopDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', 'POPMSA006')
        topic =  self.request.query_params.get('topic', 'POPMS/CelestialHubPoP/status')
        date = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, date=date)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    


class POPMSA006HistoryViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = POPMSA006HistorySerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'date']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = PopDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        date =  self.request.query_params.get('date', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and date:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, date=date)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

class POPMSA006DataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = POPMSA006DataSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'date']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = PopDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code, date='TODAY')
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, date='TODAY')

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

