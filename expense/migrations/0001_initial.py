# Generated by Django 2.2.4 on 2019-09-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_item', models.IntegerField(default=0)),
                ('unit', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
