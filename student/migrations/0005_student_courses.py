# Generated by Django 2.2.1 on 2019-10-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20191008_1612'),
        ('student', '0004_auto_20190723_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(blank=True, to='Course.Course'),
        ),
    ]
