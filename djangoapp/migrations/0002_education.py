# Generated by Django 4.2.4 on 2023-10-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30)),
                ('university', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.candidate')),
            ],
        ),
    ]