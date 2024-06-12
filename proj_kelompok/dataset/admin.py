from django.contrib import admin
from .models import Dataset

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('nama_dataset', 'pembuat_dataset', 'verifikator_dataset', 'jumlah_records', 'jumlah_attribute', 'tanggal_mulai', 'tanggal_selesai', 'status_penyelesaian')
