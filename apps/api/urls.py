

from django.urls import path
from apps.api.views import DummyEmployList
urlpatterns = [
    path('employes/', DummyEmployList.as_view(), name="dummy_list"),

]
