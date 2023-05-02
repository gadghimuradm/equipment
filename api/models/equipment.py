from django.db import models


class EquipmentType(models.Model):
    """ Equipment type model """
    title = models.CharField(verbose_name='Наименование', max_length=128)
    mask = models.CharField(verbose_name='Маска серийного номера', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тип оборудования'
        verbose_name_plural = 'типы оборудования'


class Equipment(models.Model):
    """ Equipment model """
    type = models.ForeignKey(to=EquipmentType, verbose_name='Тип оборудования', related_name='equipments',
                             on_delete=models.CASCADE)
    serial_number = models.CharField(verbose_name='Серийный номер', max_length=32)
    note = models.TextField(verbose_name='Примечание', blank=True, default='')

    def __str__(self):
        return f'{self.type}: {self.serial_number}'

    class Meta:
        verbose_name = 'оборудование'
        verbose_name_plural = 'оборудование'
