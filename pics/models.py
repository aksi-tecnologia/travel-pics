from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'pics_category'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Folder(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'pics_folder'
        managed = True
        verbose_name = 'Pasta'
        verbose_name_plural = 'Pastas'


class Photo(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    photo_date = models.DateField()
    size = models.PositiveIntegerField()  # size in bytes
    storage_url = models.URLField()
    view_url = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    is_public = models.BooleanField(default=True)  # Field to define if the photo is public or private
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



