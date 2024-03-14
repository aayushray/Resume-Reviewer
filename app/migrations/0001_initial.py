# Generated by Django 5.0 on 2024-03-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('resume_file', models.FileField(upload_to='resumes/')),
                ('feedback', models.TextField(blank=True)),
            ],
        ),
    ]
