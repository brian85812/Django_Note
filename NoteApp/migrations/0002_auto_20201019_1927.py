# Generated by Django 3.1.2 on 2020-10-19 19:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NoteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
