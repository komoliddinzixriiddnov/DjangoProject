from django.http import JsonResponse
from django.shortcuts import render

from DjangoProject.services import send_email


def email_verification(request):
    return render(request, 'auth/email_verification.html')


def test_email(request):
    subject = request.GET.get('subject')
    email = request.GET.get('email')
    if not subject or not email:
        return JsonResponse({'status': False, 'error': 'missing query ["subject", "email"]'}, status = 400)
    context = {
        'subject': subject,
        'email': email,
    }

    return JsonResponse({'status': 'success', 'email': email})