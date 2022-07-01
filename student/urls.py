from django.urls import path
from . import views
from .models import Student

from .views import RecordsListView,RecordsDetailView,RecordCreateView,RecordUpdateView,RecordDeleteView,RecordsByYearsListView

urlpatterns = [
    path('',views.studhome,name="student-home"),
    path('records/filtered',views.show,name="records-filtered"),
    path('records/',RecordsListView.as_view(),name="records-list"),
    path('records/create',RecordCreateView.as_view(),name="record-create"),
    path('records/<int:pk>/detail',RecordsDetailView.as_view(),name="record-detail"),
    path('records/<int:pk>/update',RecordUpdateView.as_view(),name="record-update"),
    path('records/<int:pk>/delete',RecordDeleteView.as_view(),name="record-delete"),
    path('recordsy/<str:year>',RecordsByYearsListView.as_view(),name="records-year")
]

