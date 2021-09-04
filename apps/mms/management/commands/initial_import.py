from django.core.management.base import BaseCommand, CommandError
from apps.mms.utils.data_import import initial_import


class Command(BaseCommand):
    help = 'Realiza o carregamento inicial dos dados'

    def handle(self, *args, **options):
        result = initial_import('BRLBTC')
        self.stdout.write(self.style.SUCCESS(f'BRLBTC: {result}'))
        result = initial_import('BRLETH')
        self.stdout.write(self.style.SUCCESS(f'BRLBTC: {result}'))
        self.stdout.write(self.style.SUCCESS('Carregamento realizado com sucesso...'))
