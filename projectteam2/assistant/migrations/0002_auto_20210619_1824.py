# Generated by Django 3.2.4 on 2021-06-19 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='doc_expiry_date',
            new_name='expiry_date',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='doc_issue_date',
            new_name='issue_date',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='doc_name',
            new_name='name',
        ),
    ]