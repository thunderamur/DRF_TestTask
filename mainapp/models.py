from django.db import models


class BaseModel(models.Model):
    name = models.CharField('Название', max_length=50)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class District(BaseModel):
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Category(BaseModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CompanyGroup(BaseModel):
    class Meta:
        verbose_name = 'Сеть предприятий'
        verbose_name_plural = 'Сети предприятий'


class Product(BaseModel):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Company(BaseModel):
    company_group = models.ForeignKey(CompanyGroup, verbose_name='Группа компаний', on_delete=models.PROTECT)
    description = models.TextField('Описание', blank=True)
    districts = models.ManyToManyField(District, verbose_name='Районы')

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'


class Price(models.Model):
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name='Предприятие', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'{self.price} ({self.product.name} ({self.company.name}))'
