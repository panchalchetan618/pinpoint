from django.urls import path
from .views import request_otp, verify_otp_view

urlpatterns = [
    path("", request_otp, name="request_otp"),
    path("verify/", verify_otp_view, name="verify_otp"),
]
