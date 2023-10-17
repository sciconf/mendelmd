# Generated by Django 4.2.6 on 2023-10-16 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manifest', models.JSONField()),
                ('status', models.CharField(max_length=30)),
                ('action', models.CharField(max_length=30)),
                ('md5', models.TextField(blank=True, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('time_taken', models.TextField(blank=True, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.ManyToManyField(to='files.file')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
