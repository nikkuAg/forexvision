from typing import Any

from django.core.management.base import BaseCommand
from forex_backend.constants import ONE_YEAR
from forex_backend.utils import sync_database


class Command(BaseCommand):
    help = "Populate database with 1 year of exchange rate data"

    def handle(self, *args: Any, **options: Any) -> str | None:
        sync_database(ONE_YEAR)
        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
