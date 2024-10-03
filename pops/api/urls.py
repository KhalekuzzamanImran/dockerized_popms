from pops.api.views import PopViewOnly, PopDeviceViewOnly, PopDeviceStatesViewSet, POPMSA006HistoryViewSet, LatestPOPMSA006ViewSet,POPMSA006DataViewSet
from django.urls import path, include

from rest_framework import routers

app_name = 'pops'

router = routers.DefaultRouter()
router.register(r'pops', PopViewOnly, 'get_pops')
router.register(r'pop-devices', PopDeviceViewOnly, 'get_pop_devices')
router.register(r'pop-device-states', PopDeviceStatesViewSet, 'get_device_states')
router.register(r'popmsa006-latest-data', LatestPOPMSA006ViewSet, 'get_popmsa006_latest_data')
router.register(r'popmsa006-history-data', POPMSA006HistoryViewSet, 'get_popmsa006_history_data')
router.register(r'popmsa006-data', POPMSA006DataViewSet, 'get_popmsa006_data')


urlpatterns = [
    path('', include(router.urls)),
]
