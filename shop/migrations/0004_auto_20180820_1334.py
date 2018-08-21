# Generated by Django 2.1 on 2018-08-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180820_1224'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название категории'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
