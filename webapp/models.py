from django.db import models

CATEGORY = [('other', 'Разное'), ('dairy', 'Молочные продукты'), ('fruit', 'Фрукты'), ('seafood', 'Морепродукты')]


# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=100, null=True, blank=False, verbose_name='Имя продукта')
    descr_product = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    category = models.CharField(max_length=25, null=True, blank=False, choices=CATEGORY, default=CATEGORY[0][0],
                                verbose_name='Категория')
    remainder = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.id}.{self.name_product}:{self.category}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ItemCart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, blank=True, related_name='items_cart')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.pk}. {self.product}:{self.quantity}'

    @property
    def product_sum(self):
        return self.product.price * self.quantity

    class Meta:
        db_table = 'itemcart'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class OrderProduct(models.Model):
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="Количество")


class Order(models.Model):
    products = models.ManyToManyField("webapp.Product", related_name='orders',
                                      verbose_name='Продукты', through=OrderProduct)
    user = models.CharField(max_length=30, blank=True, verbose_name='Покупатель')
    phone = models.CharField(max_length=30,  verbose_name='Телефон')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
