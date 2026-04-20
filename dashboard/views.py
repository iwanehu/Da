from django.shortcuts import render
from .models import Crypto
from django.shortcuts import redirect
from .management.commands.update_crypto import Command as UpdateCommand

def crypto_index(request):
    cryptos = Crypto.objects.all().order_by('-market_cap')
    
    # Preparamos los datos específicamente para el gráfico
    context = {
        'cryptos': cryptos,
        'cryptos_symbols': [c.symbol for c in cryptos],
        # Importante: convertimos Decimal a float para que JSON lo entienda
        'cryptos_prices': [float(c.price) for c in cryptos],
    }
    return render(request, 'dashboard/index.html', context)


def refresh_prices(request):
    cmd = UpdateCommand()
    cmd.handle() 
    return redirect('crypto_index')