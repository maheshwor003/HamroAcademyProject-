# Generated by Django 4.0.3 on 2022-09-10 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_number', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=40)),
                ('max_numb_students', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='Administration.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTimes',
            fields=[
                ('pid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('time', models.CharField(choices=[('9:30 - 10:30', '9:30 - 10:30'), ('10:30 - 11:30', '10:30 - 11:30'), ('11:30 - 12:30', '11:30 - 12:30'), ('12:30 - 1:30', '12:30 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], default='11:30 - 12:30', max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_number', models.CharField(max_length=6)),
                ('seating_capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('section_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('num_class_in_week', models.IntegerField(default=0)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.courses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.departments')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.instructors')),
                ('meeting_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.meetingtimes')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administration.rooms')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='instructors',
            field=models.ManyToManyField(to='Administration.instructors'),
        ),
    ]
