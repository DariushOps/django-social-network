# Generated by Django 4.0.5 on 2022-07-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]