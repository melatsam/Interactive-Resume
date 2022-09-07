# Generated by Django 3.2.15 on 2022-09-07 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.education'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='expirience',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.exprience'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('Female', 'Female'), ('other', 'other')], max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_des',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Amharic', 'Amharic')], max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resident',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]