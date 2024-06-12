from django.db import models

class Dataset(models.Model):
    nama_dataset = models.CharField(max_length=100)
    pembuat_dataset = models.CharField(max_length=100)
    verifikator_dataset = models.CharField(max_length=100, blank=True, null=True)
    jumlah_records = models.IntegerField()
    jumlah_attribute = models.IntegerField()
    deskripsi_sumber = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status_penyelesaian = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_dataset
