# Generated by Django 4.0.3 on 2022-03-23 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msapp', '0003_courses_sessionyearmodel_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='msapp.courses'),
        ),
    ]