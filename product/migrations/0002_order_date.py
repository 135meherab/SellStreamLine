<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-05-12 06:54
=======
# Generated by Django 4.2.7 on 2024-05-12 02:21
>>>>>>> 5571fe046d49c44c5f20f0d6840f20318b931b77

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
