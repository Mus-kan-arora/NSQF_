# Generated by Django 5.0.2 on 2024-07-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_customuser_submission_date_assignment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='center_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
