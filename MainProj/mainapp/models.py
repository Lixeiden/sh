from django.db import models


class TelegrafModel(models.Model):
    uri = models.CharField(primary_key=True, max_length=6, verbose_name='Link')
    created = models.DateField(auto_now_add=True, verbose_name='Creation date')
    file = models.FileField(upload_to='uploads/', verbose_name='Path to the file', blank=True)
    content = models.TextField(db_index=True, verbose_name='Content')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('pub', kwargs={'uri': self.uri})

    def __str__(self):
        return self.uri

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['-created', 'uri']
