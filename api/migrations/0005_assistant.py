# Generated by Django 4.2.7 on 2023-11-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_professor_lab_professor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('lab_number', models.CharField(default=0, max_length=20)),
                ('phone_number', models.CharField(default=0, max_length=20)),
            ],
        ),
    ]