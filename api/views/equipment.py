from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api.models import EquipmentType, Equipment
from api.serializers import EquipmentTypeSerializer, EquipmentSerializer


class EquipmentTypeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ Equipment type ViewSet
        Allowed actions: List, Create
    """
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """ Equipment ViewSet
        Allowed actions: List, Retrieve, Create, Update, Destroy
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def create(self, request, *args, **kwargs):
        bulk = isinstance(request.data, list)

        if not bulk:
            return super().create(request, *args, **kwargs)

        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        return self.perform_create(serializer)
