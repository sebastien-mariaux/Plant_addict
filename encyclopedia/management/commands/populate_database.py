import sys
import os
import csv
import json
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from encyclopedia.models import PlantOrder, PlantClass, Family, Specie, Genus, Branch


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--source',
            help='Path to source file',
        )
        parser.add_argument(
            '-d',
            '--delete',
            action='store_true',
            help='Delete data before populating database',
        )

    def handle(self, *args, **options):
        sys.stdout.write('Populating encyclopedia database...\n')
        if options['delete']:
            delete_data()
        handle_file(options['source'])


def handle_file(file: str):
    if os.path.isfile(file):
        write_to_database(file)
    else:
        sys.stdout.write('Input file does not exist')


def write_to_database(file: str):

    with open(file, encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        header = next(csv_reader)
        header_index = {header[i]: i for i in range(len(header))}
        for index, row in enumerate(csv_reader):
            handle_row(index, row, header_index)

def handle_row(index: int, row: list, header_index: dict):
    if row[header_index['verbatimTaxonRank']] != 'species':
        return

    family_name = row[header_index['family']]
    genus_name = row[header_index['genus']]
    specie_name = row[header_index['scientificName']]
    # sys.stdout.write(f"Creating specie {specie_name} index {index}...\n")

    if Specie.objects.filter(name=specie_name).first():
        return

    family = Family.objects.get_or_create(name=family_name)[0]

    # classification error in datasource
    if genus_name in correction_mapping:
        family = Family.objects.get_or_create(name=correction_mapping[genus_name])[0]

    try:
        genus = Genus.objects.get_or_create(name=genus_name, family=family)[0]
        # sys.stdout.write(json.dumps(row[header_index['verbatimTaxonRank']]))
    except IntegrityError:
        sys.stderr.write(
            f"Error: {genus_name} specie {specie_name} index {index} family {family_name}\n")
        return

    Specie.objects.create(name=specie_name, genus=genus)


def delete_data():
    sys.stdout.write('Deleting data from encyclopedia database...\n')
    Specie.objects.all().delete()
    Genus.objects.all().delete()
    Family.objects.all().delete()
    PlantClass.objects.all().delete()
    PlantOrder.objects.all().delete()
    Branch.objects.all().delete()


correction_mapping = {
    'Bigelowia': 'Asteraceae',
    'Tithonia': 'Asteraceae',
    'Centaurium': 'Gentianaceae',
    'Layia': 'Asteraceae',
    'Bulbostylis': 'Cyperaceae',
    'Acosta': 'Hypnaceae',
    'Saussurea': 'Asteraceae',
    'Eriocoma': 'Poaceae',
    'Heterotrichum': 'Melastomataceae',
    # 'Trichophyllum': '????',
    # 'Hymenolepis': '????',
    'Chabraea': 'Asteraceae',
    # 'Meridiana': '????',
    # 'Theodorea': '????',
    # 'Wirtgenia': '????',

}
