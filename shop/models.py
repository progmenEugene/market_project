from django.db import models
from django.urls import reverse

# Create your models here.

#Модель категории
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True, verbose_name = 'Название категории')
	slug = models.SlugField(max_length=150, db_index=True, unique = True)


	class Meta:
		ordering = ['name']
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_list_by_category', args=[self.slug])

#Модель продукта
class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
	name = models.CharField(max_length=300, db_index=True, verbose_name="Название товара")
	slug = models.SlugField(max_length=250, db_index=True, unique=True, verbose_name='Метка')
	image = models.ImageField(upload_to="images/", verbose_name="Изображение товара")
	image_1 = models.ImageField(upload_to="images/", verbose_name="Изображение товара1")
	image_2 = models.ImageField(upload_to="images/", verbose_name="Изображение товара2")
	image_3 = models.ImageField(upload_to="images/", verbose_name="Изображение товара3")
	description = models.TextField(verbose_name="Описание товара")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
	available = models.BooleanField(default=True, verbose_name='Доступность')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')



	class Meta:
		verbose_name_plural = 'Товар'
		ordering = ['name']
		index_together = [
		['id', 'slug']
		]

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('productdetail', args=[self.id, self.slug])

