# Generated by Django 4.0.6 on 2022-07-15 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_create_store_product_stores_table'),
    ]

    operations = [
        migrations.RunSQL("""
insert into store_category (name) values ('Games');
insert into store_category (name) values ('Clothing');
insert into store_category (name) values ('Grocery');
insert into store_category (name) values ('Electronics2');
insert into store_category (name) values ('Shoes');
insert into store_category (name) values ('Electronics');
insert into store_category (name) values ('Baby');
insert into store_category (name) values ('Computers');
insert into store_category (name) values ('Garden');
insert into store_category (name) values ('Health');
insert into store_category (name) values ('Garden2');
insert into store_category (name) values ('Grocery2');
insert into store_category (name) values ('Music');
insert into store_category (name) values ('Kids');
insert into store_category (name) values ('Clothing2');
        """, """ SELECT * FROM store_product """)
    ]
