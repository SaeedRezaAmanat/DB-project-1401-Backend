# Generated by Django 4.0.6 on 2022-07-15 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_create_store_stores_table'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE store_product_stores (
                id SERIAL,
                product_id INT NOT NULL,
                store_id INT NOT NULL,
                UNIQUE (store_id, product_id),
                PRIMARY KEY (id),
                CONSTRAINT fk_product
                    FOREIGN KEY (product_id)
                    REFERENCES store_product(id)
                    ON DELETE CASCADE,
                CONSTRAINT fk_store
                    FOREIGN KEY (store_id)
                    REFERENCES store_stores(id)
                    ON DELETE CASCADE
            );
    """, """
        DROP TABLE store_product_stores;
    """)

    ]
