# Generated by Django 3.1.2 on 2020-10-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.IntegerField(choices=[(0, 'przy odbiorze'), (1, 'online')], default=0, null=True),
        ),
    ]