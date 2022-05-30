from django.urls import path

from .views import OpenTrackingView

urlpatterns = [
    path(
        'open/<str:path>/', OpenTrackingView.as_view(),
        name="open_tracking"
    )
]
