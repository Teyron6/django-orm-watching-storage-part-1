import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

def passcard_info(num):
    print('owner_name:', Passcard.objects.all()[num].owner_name)
    print('passcode:', Passcard.objects.all()[num].passcode)
    print('created_at:', Passcard.objects.all()[num].created_at)
    print('is_active:', Passcard.objects.all()[num].is_active)


if __name__ == '__main__':
    # Программируем здесь
    print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    ### number_of_active = 0
    ### for passcard in Passcard.objects.all():
    ###     if passcard.is_active:
    ###         number_of_active+=1
    number_of_active = len(Passcard.objects.filter(is_active=True))
    print('Активных пропусков:', number_of_active)