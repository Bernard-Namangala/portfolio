# Generated by Django 2.2.8 on 2020-03-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0007_auto_20200309_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=2087)),
                ('icon', models.ImageField(upload_to='images/social')),
            ],
        ),
    ]
