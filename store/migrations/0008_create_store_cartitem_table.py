# Generated by Django 4.0.6 on 2022-07-12 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_create_store_cart_table'),
    ]

    operations = [
        migrations.RunSQL("""
        CREATE TABLE store_cartitem (
            id SERIAL,
            product_id INT NOT NULL,
            cart_id VARCHAR(36) NOT NULL,
            quantity INT NOT NULL DEFAULT 1 CHECK ( quantity > 0 ),
            UNIQUE (product_id, cart_id),
            PRIMARY KEY (id),
            CONSTRAINT fk_product
                FOREIGN KEY (product_id)
                REFERENCES store_product(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_cart
                FOREIGN KEY (cart_id)
                REFERENCES store_cart(id)
                ON DELETE CASCADE
        );
    """, """
        DROP TABLE store_cartitem;
    """)
    ]
