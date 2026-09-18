
from django.shortcuts import render
from django.conf import settings
from scoutsbevaixch.captchaManager import CaptchaManager

captchaManager = CaptchaManager()


def contacts(request):
    get_captcha_id = request.GET.get('id', None)
    get_captcha_value = request.GET.get('value', None)

    correct = captchaManager.test(get_captcha_id, get_captcha_value)

    if correct:
        contacts = settings.CONTACTS
        return render(request, "contacts.html", context={"contacts": contacts})

    captcha_id, captcha_image = captchaManager.generate()

    return render(request, "contacts.html", context={"captcha_id": captcha_id, "captcha_image": captcha_image, "captcha_try": get_captcha_id is not None})