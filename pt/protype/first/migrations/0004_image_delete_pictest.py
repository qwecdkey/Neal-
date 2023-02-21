# Generated by Django 4.1.5 on 2023-02-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_pictest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='PicTest',
        ),
    ]
