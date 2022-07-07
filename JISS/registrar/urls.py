from django.urls import path

from . import views

urlpatterns = [
    path('',views.registrar,name = "registrar"),
    path('pending/',views.pendingcases.as_view(),name="pending case"),
    path('newcase/',views.casescreate.as_view(), name="case_add"),
    path('resolved/',views.resolvedcases.as_view(), name="resolved cases"),
    path('hearing/',views.hearings.as_view(), name = "allot_hearing_date"),
    path('particular_case/',views.case_status.as_view(), name = "search_particular_case"),
    path('hearing_update/',views.update_hearing.as_view(), name = "update_hearing"),
    path('case_closed/',views.case_resolved.as_view(), name = "case_closed")
]






