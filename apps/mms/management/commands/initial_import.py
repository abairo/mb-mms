from django.core.management.base import BaseCommand, CommandError
from apps.mms.utils.data_import import initial_import
import time


class Command(BaseCommand):
    help = 'Realiza o carregamento inicial dos dados'

    def handle(self, *args, **options):
        start = time.time()
        result = initial_import('BRLBTC')
        end = time.time()

        self.stdout.write(self.style.SUCCESS(f'BRLBTC: {result} em {end - start} segundos'))

        start = time.time()
        result = initial_import('BRLETH')
        end = time.time()

        self.stdout.write(self.style.SUCCESS(f'BRLETH: {result} em {end - start} segundos'))
        self.stdout.write(self.style.SUCCESS('Carregamento realizado com sucesso...'))
