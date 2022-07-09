# Generated by Django 4.0.6 on 2022-07-07 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_review'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE store_product (
                id int,
                title varchar(255),
                price decimal(5, 3),
                inventory int,
                last_update timestamp DEFAULT current_timestamp
            )
        """)
    ]