# Generated by Django 5.2.3 on 2025-06-29 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studenr_id',
            new_name='student_id',
        ),
    ]
