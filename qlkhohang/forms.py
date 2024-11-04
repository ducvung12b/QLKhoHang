# inventory/forms.py
from django import forms
from .models import HangHoa

class HangHoaForm(forms.ModelForm):
    class Meta:
        model = HangHoa
        fields = ['ten', 'mota', 'donvitinh']
