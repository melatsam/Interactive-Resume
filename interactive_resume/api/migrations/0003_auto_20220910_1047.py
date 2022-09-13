# Generated by Django 3.2.15 on 2022-09-10 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220910_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='expirience',
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exprience',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.resume'),
            preserve_default=False,
        ),
    ]