import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


if __name__ == '__main__':
    print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    number_of_active = Passcard.objects.filter(is_active=True).count()
    print('Активных пропусков:', number_of_active)