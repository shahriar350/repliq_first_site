from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from admin_app.models import Category, Brand, Ingredient, Manufacturer, Supplier, MedicinePhysicalState, \
    RouteOfAdministration
from auth_app.models import Users


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        categories = ["Analgesics", "Analgesics", "Antianxiety Drugs", "Antiarrhythmics"]
        ingredients = ["Clonazepam", "Minoxidil", "ingredient1", "ingredient2"]
        brands = ["Square Pharmaceuticals", "Incepta Pharmaceutical Ltd.", "Beximco Pharmaceuticals LTD.",
                  "Opsonin Pharma Ltd."]
        manufacturers = ["manufacturers1", "manufacturers2", "manufacturers3", "manufacturers4"]
        suppliers = ["suppliers1", "suppliers2", "suppliers3", "suppliers4", "suppliers5"]
        medicinePhysicalStates = ["medicinePhysicalStates", "medicinePhysicalStates1", "medicinePhysicalStates2",
                                  "medicinePhysicalStates3", "medicinePhysicalStates4"]
        routeOfAdministrations = ["routeOfAdministrations", "routeOfAdministrations1", "routeOfAdministrations3",
                                  "routeOfAdministrations2", "routeOfAdministrations4"]
        with transaction.atomic():
            for category in categories:
                Category.objects.create(
                    name=category
                )
            for i in manufacturers:
                Manufacturer.objects.create(
                    name=i
                )
            for i in suppliers:
                Supplier.objects.create(
                    name=i
                )
            for i in medicinePhysicalStates:
                MedicinePhysicalState.objects.create(
                    name=i
                )
            for i in routeOfAdministrations:
                RouteOfAdministration.objects.create(
                    name=i
                )
            for brand in brands:
                Brand.objects.create(
                    name=brand
                )
            for ingredient in ingredients:
                Ingredient.objects.create(
                    name=ingredient
                )
