import csv
from django.db import migrations
from .. import models


class Migration(migrations.Migration):

    def load_data(self, schema_editor):

        with open('/Users/anand/Projects/inmar/inmar/csv_data/sku_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            sku_data_object = []

            location = set()
            department = set()
            category = set()
            sub_category = set()
            sku_data = []

            for row in reader:
                location.add(row.get("LOCATION"))
                department.add(row.get("DEPARTMENT"))
                category.add(row.get("CATEGORY"))
                sub_category.add(row.get("SUBCATEGORY"))
                sku_data.append({
                    'SKU': row.get('SKU'),
                    'NAME': row.get('NAME'),
                    'LOCATION': row.get('LOCATION'),
                    'DEPARTMENT': row.get('DEPARTMENT'),
                    'CATEGORY': row.get('CATEGORY'),
                    'SUBCATEGORY': row.get('SUBCATEGORY')
                })

            locations = [models.Location(name=l_name.strip()) for l_name in location]
            models.Location.objects.bulk_create(locations, ignore_conflicts=True)
            locations = {l.name: l for l in models.Location.objects.all()}

            departments = [models.Department(name=d_name.strip()) for d_name in department]
            models.Department.objects.bulk_create(departments, ignore_conflicts=True)
            departments = {d.name: d for d in models.Department.objects.all()}

            categories = [models.Category(name=c_name.strip()) for c_name in category]
            models.Category.objects.bulk_create(categories, ignore_conflicts=True)
            categories = {c.name: c for c in models.Category.objects.all()}

            sub_categories = [models.SubCategory(name=c_name.strip()) for c_name in sub_category]
            models.SubCategory.objects.bulk_create(sub_categories, ignore_conflicts=True)
            sub_categories = {sc.name: sc for sc in models.SubCategory.objects.all()}

            for row in sku_data:
                sku_data_object.append(
                    models.SKUData(
                        sku=int(row.get("SKU").strip()),
                        name=row.get("NAME").strip(),
                        location=locations.get(row.get("LOCATION").strip()),
                        department=departments.get(row.get("DEPARTMENT").strip()),
                        category=categories.get(row.get("CATEGORY").strip()),
                        sub_category=sub_categories.get(row.get("SUBCATEGORY").strip())
                    )
                )
            models.SKUData.objects.bulk_create(sku_data_object)

    dependencies = [
        ('location', '0003_skudata'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=migrations.RunPython.noop),
    ]
