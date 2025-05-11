from django.db import models
import django.core.validators


class Type(models.Model):
    name = models.CharField(verbose_name="имя", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тип"
        verbose_name_plural = "типы"


class Category(models.Model):
    name = models.CharField(verbose_name="имя")
    type = models.ForeignKey(
        Type,
        on_delete=models.DO_NOTHING,
        verbose_name="тип",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Subcategory(models.Model):
    name = models.CharField(verbose_name="имя")
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="категория",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"


class Status(models.Model):
    name = models.CharField(verbose_name="имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"


class Entry(models.Model):
    date = models.DateField(
        default=django.utils.timezone.now,
        verbose_name="дата",
        editable=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="статус",
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="тип",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="подкатегория",
    )
    amount = models.IntegerField(
        verbose_name="сумма",
        validators=[
            django.core.validators.MinValueValidator(1),
        ],
    )
    comment = models.CharField(
        null=True,
        blank=True,
        verbose_name="комментарий",
    )

    def __str__(self):
        return str(self.date)

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.category != self.subcategory.category:
            raise ValidationError(
                "Подкатегория должна соответствовать выбранной категории"
            )
        if self.type != self.category.type:
            raise ValidationError("Категория должна соответствовать выбранному типу")

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
