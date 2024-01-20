from django.shortcuts import render
from .utils import send_otp, verify_otp


def request_otp(request):
    if request.method == "POST":
        phone = request.POST.get("phone").strip()
        if not phone.startswith("+91"):
            phone = "+91" + phone

        response = send_otp(phone)
        return render(request, "otp.html", {"response": response})

    return render(request, "otp.html")


def verify_otp_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone").strip()
        otp = request.POST.get("otp").strip()
        if not phone.startswith("+91"):
            phone = "+91" + phone

        response = verify_otp(phone, otp)
        return render(request, "verify_otp.html", {"response": response})

    return render(request, "verify_otp.html")
