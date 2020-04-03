# Generated by Django 2.2.8 on 2020-03-09 10:28

from django.db import migrations, models
import django.db.models.deletion
import my_portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0006_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='technologies',
            options={'verbose_name_plural': 'Technologies'},
        ),
        migrations.AddField(
            model_name='home',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='images/profile'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to=my_portfolio.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='my_portfolio.Project'),
        ),
        migrations.AlterField(
            model_name='technologies',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='my_portfolio.Project'),
        ),
    ]
