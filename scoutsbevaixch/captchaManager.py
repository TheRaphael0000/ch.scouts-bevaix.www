from cachetools import TTLCache

from captcha.image import ImageCaptcha
import base64
import secrets
import random


class CaptchaManager():
    # small letters without jil0o to avoid confusion
    characters = "abcdefghkmnpqrstuvwxyz23456789"
    def __init__(self):
        self.cache = TTLCache(maxsize=100, ttl=120)

    def generate(self):
        captcha = ImageCaptcha()
        id = secrets.token_urlsafe(15)
        value = "".join(random.choices(CaptchaManager.characters, k=4))
        image64 = base64.b64encode(captcha.generate(value).getvalue()).decode('utf-8')
        self.cache[id] = value
        return id, image64

    def test(self, id, value):
        return id in self.cache and self.cache[id] == value.lower()