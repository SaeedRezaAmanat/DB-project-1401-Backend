# Generated by Django 4.0.6 on 2022-07-15 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_add_category_dummy_data'),
    ]

    operations = [
        migrations.RunSQL("""
        insert into store_stores (name, owner) values ('Gutkowski LLC', 'Nestor');
        """, """ SELECT * FROM store_product """)
    ]