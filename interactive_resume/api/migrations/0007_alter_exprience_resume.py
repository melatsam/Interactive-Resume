# Generated by Django 3.2.15 on 2022-09-10 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_education_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exprience',
            name='resume',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='expriences', to='api.resume'),
        ),
    ]
