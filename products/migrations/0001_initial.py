# Generated by Django 3.1.1 on 2020-09-29 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('PAID', 'Paid'), ('NEW', 'New'), ('IN_PROGRESS', 'In progress')], default=products.constants.StatusChoices['NEW'], max_length=255)),
                ('price', models.DecimalField(decimal_places=2, help_text='Current price of products', max_digits=15)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, help_text='Old price of products', max_digits=15, null=True)),
                ('is_billed', models.BooleanField(default=False, help_text='Product is billed', verbose_name='is billed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ('-id',),
            },
        ),
    ]
