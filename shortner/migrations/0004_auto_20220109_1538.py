# Generated by Django 3.2.9 on 2022-01-10 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_profilemodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilemodel',
            options={'ordering': ['last_name']},
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='name',
            new_name='user',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]