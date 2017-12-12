from django.db import models


class ScheduleManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(date_schedule__icontains=query)
        )


class Schedule(models.Model):

    name = models.CharField('Nome do Paciente', max_length=100)
    slug = models.SlugField('Atalho')
    date_schedule = models.DateField('Data do Agendamento')
    date_schedule_start = models.TimeField('Hora início')
    date_schedule_end = models.TimeField('Hora final')
    procedure =models.TextField('Procedimento', blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ScheduleManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('schedules:details', (), {'pk': self.pk})

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['date_schedule', 'name', 'date_schedule_start']