from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class IsIncidentCreator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and (request.user.role.key == 'INCIDENT_CREATOR')

class IsStationPersonnel(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and (request.user.role.key == 'STATION_PERSONNEL')

class IsHeadQuarterPersonnel(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and (request.user.role.key in  ['ADN_HEAD_QUARTER', 'HEAD_QUARTER'])