# Generated by Django 3.2.7 on 2021-10-11 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='電話')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立日期')),
                ('message', models.TextField(default='', verbose_name='聯絡訊息')),
                ('contacted', models.BooleanField(default=False, verbose_name='已聯絡')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='使用者')),
            ],
        ),
    ]
