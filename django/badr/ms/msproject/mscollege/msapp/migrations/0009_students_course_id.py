# Generated by Django 4.0.3 on 2022-03-25 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msapp', '0008_remove_students_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='msapp.courses'),
        ),
    ]