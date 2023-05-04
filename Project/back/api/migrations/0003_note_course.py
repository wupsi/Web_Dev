# Generated by Django 3.0.5 on 2023-04-25 18:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200424_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='course',
            field=models.ForeignKey(db_column='course', default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.Course', to_field='short_name'),
            preserve_default=False,
        ),
    ]