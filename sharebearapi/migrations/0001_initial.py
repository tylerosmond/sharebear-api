# Generated by Django 5.1.2 on 2024-10-21 19:46

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)])),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)], verbose_name='Weight (lbs)')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('description', models.CharField(max_length=200, verbose_name='Product Description')),
                ('status', models.CharField(choices=[('available', 'Available'), ('requested', 'Requested'), ('shared', 'Shared'), ('inactive', 'Inactive')], max_length=10, verbose_name='Availability Status')),
                ('product_img', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='sharebearapi.category', verbose_name='Category')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='sharebearapi.condition', verbose_name='Condition')),
                ('min_age', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='sharebearapi.age', verbose_name='Minimum Age')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='sharebearapi.size', verbose_name='Size')),
                ('max_weight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='sharebearapi.weight', verbose_name='Maximum Weight')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_sharer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='favorited_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'favorite_sharer')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_as_owner', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='sharebearapi.product')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_as_recipient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('owner', 'recipient', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlistitem', to='sharebearapi.product', verbose_name='Wishlist Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]