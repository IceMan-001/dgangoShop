# Generated by Django 5.1.2 on 2024-11-09 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.CharField(editable=False, max_length=256, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(default='в обработке', max_length=50)),
                ('payment', models.CharField(default='картой', max_length=50)),
                ('delivery', models.CharField(default='самовывоз из магазина', max_length=50)),
                ('address', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cartuser')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.ImageField(upload_to='')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product')),
            ],
        ),
    ]
