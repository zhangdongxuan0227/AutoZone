# Generated by Django 2.1.5 on 2019-08-05 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20190801_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singel_apis',
            name='Apiexpectresult',
            field=models.CharField(max_length=200, null=True, verbose_name='预期结果'),
        ),
        migrations.AlterField(
            model_name='singel_apis',
            name='Apiformdata',
            field=models.CharField(max_length=800, null=True, verbose_name='表单参数'),
        ),
        migrations.AlterField(
            model_name='singel_apis',
            name='Apischarger',
            field=models.CharField(max_length=50, null=True, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='singel_apis',
            name='Apistatuscode',
            field=models.CharField(max_length=200, null=True, verbose_name='状态码'),
        ),
    ]
