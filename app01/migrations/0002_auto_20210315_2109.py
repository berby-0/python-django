# Generated by Django 2.2.5 on 2021-03-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='attribute_text',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='job',
            name='companyind_text',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='companysize_text',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='companytype_text',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='job',
            name='degreefrom',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobwelf_list',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='providesalary_text',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='workarea_text',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='workyear',
            field=models.CharField(max_length=8),
        ),
    ]