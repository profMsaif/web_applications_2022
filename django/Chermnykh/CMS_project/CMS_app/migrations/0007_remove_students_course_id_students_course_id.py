# Generated by Django 4.0.3 on 2022-03-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS_app', '0006_remove_students_course_id_students_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='course_id',
        ),
        migrations.AddField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=1, null=True, on_delete=models.SET('null'), to='CMS_app.courses'),
        ),
    ]
