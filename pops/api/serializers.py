from base.serializers import DynamicFieldsModelSerializer
from pops.models import Pop, PopDevice, PopDeviceState
from pops.POPMSA006_mongo_models import POPMSA006, TodayPOPMSA006, TemporaryPOPMSA006, Last7DaysPOPMSA006, Last30DaysPOPMSA006, ThisYearPOPMSA006
from pops.temporary_popmsa006_models import POPMSA006ExternalInfo, TodayPOPMSA006ExternalInfo, TemporaryPOPMSA006ExternalInfo, Last7DaysPOPMSA006ExternalInfo, Last30DaysPOPMSA006ExternalInfo, ThisYearPOPMSA006ExternalInfo

class PopSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Pop
        fields = '__all__'


class PopDeviceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = PopDevice
        fields = '__all__'

        
class PopDeviceStatesSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = PopDeviceState
        fields = '__all__'  # Include all fields by default



# POPMSA006 serializers
class POPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = POPMSA006
        fields = '__all__'

class TemporaryPOPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TemporaryPOPMSA006
        fields = '__all__'


class TodayPOPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TodayPOPMSA006
        fields = '__all__'


class Last7DaysPOPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Last7DaysPOPMSA006  
        fields = '__all__'


class Last30DaysPOPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Last30DaysPOPMSA006  
        fields = '__all__'

class ThisYearPOPMSA006Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ThisYearPOPMSA006  
        fields = '__all__'



# POPMSA006 External Info serializers
class POPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = POPMSA006ExternalInfo  
        fields = '__all__'

class TodayPOPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TodayPOPMSA006ExternalInfo 
        fields = '__all__'

class TemporaryPOPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TemporaryPOPMSA006ExternalInfo  
        fields = '__all__'


class Last7DaysPOPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Last7DaysPOPMSA006ExternalInfo  
        fields = '__all__'


class Last30DaysPOPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Last30DaysPOPMSA006ExternalInfo  
        fields = '__all__'

class ThisYearPOPMSA006ExternalInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ThisYearPOPMSA006ExternalInfo  
        fields = '__all__'


class LatestPOPMSA006DataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = PopDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayPOPMSA006.objects.all()
            data['popmsa006_latest_data'] = TodayPOPMSA006Serializer(queryset.last(), many=False).data
            queryset = TodayPOPMSA006ExternalInfo.objects.all()
            data['popmsa006_external_info'] = TodayPOPMSA006ExternalInfoSerializer(queryset.last(), many=False).data
            
        except:
            data = []

        return data


class POPMSA006HistorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = PopDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == 'POPMSA006'):
            if (instance.topic == 'POPMS/CelestialHubPoP/status'):

                data = super().to_representation(instance)
                if instance.date == 'TODAY':
                    mongo_queryset = TodayPOPMSA006.objects.all()
                    data['latest_data'] = TodayPOPMSA006Serializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayPOPMSA006Serializer(mongo_queryset, many=True).data
                    
                    mongo_queryset = TodayPOPMSA006ExternalInfo.objects.all()
                    data['latest_external_info'] = TodayPOPMSA006ExternalInfoSerializer(mongo_queryset.last(), many=False).data
                    data['external_info'] = TodayPOPMSA006ExternalInfoSerializer(mongo_queryset, many=True).data

                elif instance.date == 'LAST_7_DAYS':

                    mongo_queryset = Last7DaysPOPMSA006.objects.all()
                    data['latest_data'] = Last7DaysPOPMSA006Serializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysPOPMSA006Serializer(mongo_queryset, many=True).data

                    mongo_queryset = Last7DaysPOPMSA006ExternalInfo.objects.all()
                    data['latest_external_info'] = Last7DaysPOPMSA006ExternalInfoSerializer(mongo_queryset.last(), many=False).data
                    data['external_info'] = Last7DaysPOPMSA006ExternalInfoSerializer(mongo_queryset, many=True).data

                elif instance.date == 'LAST_30_DAYS':

                    mongo_queryset = Last30DaysPOPMSA006.objects.all()
                    data['latest_data'] = Last30DaysPOPMSA006Serializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysPOPMSA006Serializer(mongo_queryset, many=True).data

                    mongo_queryset = Last30DaysPOPMSA006ExternalInfo.objects.all()
                    data['latest_external_info'] = Last30DaysPOPMSA006ExternalInfoSerializer(mongo_queryset.last(), many=False).data
                    data['external_info'] = Last30DaysPOPMSA006ExternalInfoSerializer(mongo_queryset, many=True).data

                elif instance.date == 'THIS_YEAR': 
                    mongo_queryset = ThisYearPOPMSA006.objects.all()
                    data['latest_data'] = ThisYearPOPMSA006Serializer(mongo_queryset.last(), many=False).data
                    data['data'] = ThisYearPOPMSA006Serializer(mongo_queryset, many=True).data

                    mongo_queryset = ThisYearPOPMSA006ExternalInfo.objects.all()
                    data['latest_external_info'] = ThisYearPOPMSA006ExternalInfoSerializer(mongo_queryset.last(), many=False).data
                    data['external_info'] = ThisYearPOPMSA006ExternalInfoSerializer(mongo_queryset, many=True).data


        return data
    

class POPMSA006DataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = PopDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = {}

        if (instance.device_code.code == 'POPMSA006'):
            if (instance.topic == 'POPMS/CelestialHubPoP/status'):

                data = super().to_representation(instance)
                data['test'] = 'Test Value'
                return data
    



