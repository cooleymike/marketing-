# Generated by Django 4.2.5 on 2024-11-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_projectemployeeallocatedbudget_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='account_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]