

from django.urls import path
from apps.api.views import DummyEmployList,DummyExportList
urlpatterns = [
    path('employes/', DummyEmployList.as_view(), name="dummy_list"),
    path('employes/export', DummyExportList.as_view(), name="dummy_export_list"),

]
