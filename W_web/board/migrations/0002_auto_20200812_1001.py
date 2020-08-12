# Generated by Django 3.0.8 on 2020-08-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='document',
            name='attachment_img',
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(max_length=500, verbose_name='게시물 내용'),
        ),
        migrations.DeleteModel(
            name='Recommend',
        ),
    ]
