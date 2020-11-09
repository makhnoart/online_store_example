# Generated by Django 2.2.9 on 2020-06-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200625_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Pocket'), (2, 'New'), (3, 'In progress'), (4, 'Done'), (5, 'Canceled')], default=1),
        ),
    ]
