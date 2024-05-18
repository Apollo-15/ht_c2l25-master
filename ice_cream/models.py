import uuid
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill, ResizeToCover

class IceCream(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    on_main = models.BooleanField('На главную?', default=True)
    
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='icecreams/',
        processors=[ResizeToFit(820, 440)],
        format='WEBP',
        options={'quality': 90},
        blank=True,
        null=True
    )
    
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна', default=0.0)

    class Meta:        
        ordering = ('name',)
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return f'{self.name}'

    def main_image(self):
        main_image = self.images.filter(is_main=True).first()
        if main_image:
            return main_image
        return self.images.first()

def get_image_path(instance, filename):
    return f'ice_cream/{instance.ice_cream.id}/{filename}'    
    
class Image(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE, related_name='images')

    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to=get_image_path,
        processors=[],
        format='WEBP',
        options={'quality': 90},
    )

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToCover(300, 300)],
        format='WEBP',
        options={'quality': 50},
    )

    is_main = models.BooleanField(default=False, verbose_name='Основне зображення')

    def save(self, *args, **kwargs):
        if self.is_main:
            Image.objects.filter(ice_cream=self.ice_cream).update(is_main=False)
        super().save(*args, **kwargs)