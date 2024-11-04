# inventory/views.py
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import HangHoaForm
from django.db.models import Sum

def themhanghoa(request):
    if request.method == 'POST':
        form = HangHoaForm(request.POST)
        if form.is_valid():
            hanghoa = form.save()
            messages.success(request, f'Đã Thêm {hanghoa.ten} thành công.')
            return redirect('dshanghoa')
    else:
        form = HangHoaForm()
        success_message = None

    kho_list = Kho.objects.all()
    return render(request, 'app/themhanghoa.html', {'form': form, 'kho_list': kho_list, 'success_message': success_message})



def dshanghoa(request):
    hanghoas = HangHoa.objects.all()
    for hanghoa in hanghoas:
        hanghoa.total_quantity = KhoHangHoa.objects.filter(hanghoa=hanghoa).aggregate(total=Sum('soluong'))['total'] or 0

    return render(request, 'app/dshanghoa.html', {'hanghoas': hanghoas})


def suahanghoa(request, id_hang_hoa):
    hanghoa = get_object_or_404(HangHoa, pk=id_hang_hoa)
    
    if request.method == 'POST':
        form = HangHoaForm(request.POST, instance=hanghoa)
        if form.is_valid():
            hanghoa = form.save()
            messages.success(request, f'Đã Sửa {hanghoa.ten} thành công.')
            return redirect('dshanghoa')
    else:
        form = HangHoaForm(instance=hanghoa)
        success_message = None

    return render(request, 'app/suahanghoa.html', {'form': form, 'hanghoa': hanghoa, 'success_message': success_message})
