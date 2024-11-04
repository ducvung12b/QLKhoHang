from django.db import models

class Kho(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100,null=True)
    diachi = models.CharField(max_length=255)

    def __str__(self):
        return self.ten

class HangHoa(models.Model):
    DON_VI_TINH_CHOICES = [
        ('KG', 'Kilogram'),
        ('CAI', 'Cái'),
        ('CHAI', 'Chai'),
        ('HOP', 'Hộp'),
    ]

    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100,null=True)
    mota = models.TextField()
    donvitinh = models.CharField(max_length=4, choices=DON_VI_TINH_CHOICES)

    def __str__(self):
        return self.ten

class KhoHangHoa(models.Model):
    id = models.AutoField(primary_key=True)
    hanghoa = models.ForeignKey(HangHoa, on_delete=models.CASCADE)
    kho = models.ForeignKey(Kho, on_delete=models.CASCADE)
    soluong = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hanghoa.ten} in {self.kho.ten} - {self.soluong} units"
