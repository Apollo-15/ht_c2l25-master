# Generated by Django 5.0.6 on 2024-05-15 09:13

import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('name',), 'verbose_name': 'мороженое', 'verbose_name_plural': 'мороженое'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='icecreams/', verbose_name='Зображення'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Ціна'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Кількість'),
        ),
    ]
