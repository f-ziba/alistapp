# Generated by Django 3.2.3 on 2021-05-21 12:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.FloatField(blank=True, null=True)),
                ('sizes', models.CharField(default='Large', max_length=30, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('available', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock'), ('ReStocked', 'ReStocked')], default='In Stock', max_length=15)),
                ('quantity_instock', models.IntegerField(blank=True, default=1000, null=True)),
                ('minquantity', models.IntegerField(blank=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(blank=True)),
                ('latest', models.BooleanField(blank=True)),
                ('banner', models.BooleanField(blank=True)),
                ('offer', models.BooleanField(blank=True)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
    ]
