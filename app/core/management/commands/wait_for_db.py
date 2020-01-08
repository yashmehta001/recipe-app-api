import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    "Command to pause execution until db avaliable"

    def handle(self, *args, **options):
        "Commands"
        self.stdout.write('waiting for Database!!!')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database not avaliable wait 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Avaliable!!!'))
