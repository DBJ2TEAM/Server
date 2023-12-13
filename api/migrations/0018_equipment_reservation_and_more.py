# Generated by Django 4.2.7 on 2023-12-13 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_delete_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('REQUESTED', 'Requested'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='REQUESTED', max_length=20)),
                ('day', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipment')),
            ],
        ),
        migrations.RemoveField(
            model_name='roomreservation',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='roomreservation',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='roomreservation',
            name='timetable',
        ),
        migrations.RemoveField(
            model_name='roomreservation',
            name='user',
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='day',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='time',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'Requested'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='REQUESTED', max_length=20),
        ),
        migrations.DeleteModel(
            name='RoomTimetable',
        ),
    ]