# Generated by Django 4.0 on 2022-08-23 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0003_alter_course_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject_teacher',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachername', to='Administration.instructor'),
        ),
    ]
