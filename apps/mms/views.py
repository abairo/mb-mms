from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import response, status
from .models import MMS
from .serializers import MMSSerializer
from .usecases import FilterMMS
from .converters import timestamp_to_date


class MMSView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MMSSerializer
    queryset = MMS.objects.all()
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        ts_from = timestamp_to_date(int(self.request.GET.get('from')))
        ts_to = timestamp_to_date(int(self.request.GET.get('to')))
        mms_range = int(self.request.GET.get('range'))
        pair = self.kwargs.get('pair')

        usecase = FilterMMS(repository=self.get_queryset())

        data = usecase(pair=pair, mms_range=mms_range,
                       ts_from=ts_from, ts_to=ts_to)

        serializer = self.get_serializer_class()
        data = serializer(data, many=True).data

        return response.Response(data=data, status=status.HTTP_200_OK)
