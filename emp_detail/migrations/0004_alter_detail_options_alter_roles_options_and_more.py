# Generated by Django 4.2.1 on 2023-06-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_detail', '0003_alter_detail_image_upload_alter_detail_qr_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detail',
            options={'verbose_name': 'Detail', 'verbose_name_plural': 'Details'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AddField(
            model_name='detail',
            name='template_id',
            field=models.IntegerField(default=0),
        ),
    ]
