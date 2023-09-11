import csv
from django.db import migrations
from .. import models


class Migration(migrations.Migration):

    def load_data(self, schema_editor):
        with open('/Users/anand/Projects/inmar/inmar/csv_data/data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            location = set()
            department = set()
            category = set()
            sub_category = set()

            meta_data = []
            for row in reader:
                location.add(row.get("Location"))
                department.add(row.get("Department"))
                category.add(row.get("Category"))
                sub_category.add(row.get("SubCategory"))
                meta_data.append({
                    "Location": row.get("Location"),
                    "Department": row.get("Department"),
                    "Category": row.get("Category"),
                    "SubCategory": row.get("SubCategory"),
                })

            locations = [models.Location(name=l_name.strip()) for l_name in location]
            models.Location.objects.bulk_create(locations)
            locations = {l.name: l for l in models.Location.objects.all()}

            departments = [models.Department(name=d_name.strip()) for d_name in department]
            models.Department.objects.bulk_create(departments)
            departments = {d.name: d for d in models.Department.objects.all()}

            categories = [models.Category(name=c_name.strip()) for c_name in category]
            models.Category.objects.bulk_create(categories)
            categories = {c.name: c for c in models.Category.objects.all()}

            sub_categories = [models.SubCategory(name=c_name.strip()) for c_name in sub_category]
            models.SubCategory.objects.bulk_create(sub_categories)
            sub_categories = {sc.name: sc for sc in models.SubCategory.objects.all()}

            meta_data_object = []
            for row in meta_data:
                meta_data_object.append(
                    models.MetaData(
                        location=locations.get(row.get("Location").strip()),
                        department=departments.get(row.get("Department").strip()),
                        category=categories.get(row.get("Category").strip()),
                        sub_category=sub_categories.get(row.get("SubCategory").strip())
                    )
                )
            models.MetaData.objects.bulk_create(meta_data_object)

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=migrations.RunPython.noop),
    ]
