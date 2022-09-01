# Generated by Django 4.0.5 on 2022-09-01 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0002_alter_course_instructors_alter_instructor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=20, null=True)),
                ('Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.course')),
            ],
        ),
        migrations.CreateModel(
            name='Meetingtime',
            fields=[
                ('Mid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField(null=True)),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Seat_capacity', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('Section_id', models.IntegerField(primary_key=True, serialize=False)),
                ('No_of_classin_week', models.CharField(max_length=20, null=True)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.department')),
                ('Meetingtime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.meetingtime')),
                ('Room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.room')),
                ('instructors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.instructor')),
            ],
        ),
    ]
