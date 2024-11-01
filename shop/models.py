from django.db import models
from django.urls import reverse
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]

        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # вызываем родительский метод и сохраняется продукт со всеми полями
        slug_name = slugify(self.name)  # Получаем слаг-имя типа: iphone16-pro-16Gb записываем ее в переменную
        slug = f"{slug_name}-{self.pk}"  # Добавляем к имени переменной id
        self.slug = slug  #  slug = f"{slug_name}-{self.pk}" можно сразу присвоить без промежуточного значения
        super().save(*args, **kwargs)  # еще раз выполняется метод сохранения как update

    def get_absolut_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
