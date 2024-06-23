from django.shortcuts import render, redirect
from.forms import ItemForm

def cargar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposito_app:cargar_item_success')
    else:
        form = ItemForm()
    return render(request, 'deposito_app/cargar_item.html', {'form': form})