import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV file'


    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                defaults = {
                    'name': row['name'],
                    'price': row['price'],
                    'release_date': datetime.strptime(row['release_date'], '%Y-%m-%d'),
                    'lte_exists': row['lte_exists'] == '1',
                    'image': row['image']
                }
                phone, created = Phone.objects.update_or_create(
                    id=row['id'],
                    defaults=defaults
                )
                self.stdout.write(self.style.SUCCESS(f'Phone {phone.id} {"created" if created else "updated"}'))