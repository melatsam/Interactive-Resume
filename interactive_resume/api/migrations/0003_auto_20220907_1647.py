# Generated by Django 3.2.15 on 2022-09-07 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220907_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.education'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='expirience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.exprience'),
        ),
    ]