from django.conf import settings
from django.urls import path, include
from django.urls.conf import re_path
from base.views import health_check
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=settings.PROJECT_TITLE,
        default_version=settings.PROJECT_VERSION,
        description="popms Api description",
        contact=openapi.Contact(email="tanzeemrahhat80@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

v1_patterns = [
    path('accounts/', include('accounts.api.urls', namespace='accounts.apis')),
    # path('', include('devices.api.urls', namespace='devices.apis')),
    path('pop/', include('pops.api.urls', namespace='pops.apis')),
]

urlpatterns = [
    path('', health_check),
    path('api/', include([path('v1.0/', include(v1_patterns))])),
    path('admin/', admin.site.urls)
]

urlpatterns += [path('api-auth/', include('rest_framework.urls')), ]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
