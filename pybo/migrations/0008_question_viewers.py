# Generated by Django 3.1.3 on 2022-06-20 08:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0007_auto_20220608_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='viewers',
            field=models.ManyToManyField(related_name='viewers_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
