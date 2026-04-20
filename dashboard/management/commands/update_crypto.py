import requests
from django.core.management.base import BaseCommand
from dashboard.models import Crypto

class Command(BaseCommand):
    help = 'Obtiene datos en tiempo real de CoinGecko y los guarda en Neon DB'

    def handle(self, *args, **options):
        # Endpoint para las 10 principales criptomonedas en USD
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': 'false'
        }

        self.stdout.write(self.style.WARNING("Iniciando actualización desde CoinGecko..."))

        try:
            response = requests.get(url, params=params)
            # Lanza una excepción si la respuesta no es 200 OK
            response.raise_for_status()
            data = response.json()

            count = 0
            for item in data:
                # Buscamos por símbolo (clave única)
                # Si existe, actualiza los campos en 'defaults'. Si no, crea uno nuevo.
                obj, created = Crypto.objects.update_or_create(
                    symbol=item['symbol'].upper(),
                    defaults={
                        'name': item['name'],
                        'price': item['current_price'],
                        'market_cap': item['market_cap'],
                        'image': item['image'],
                        'change_24h': item['price_change_percentage_24h'],
                    }
                )
                
                verb = "Añadida" if created else "Actualizada"
                self.stdout.write(f"  [+] {verb}: {obj.name} ({obj.symbol})")
                count += 1

            self.stdout.write(self.style.SUCCESS(f'¡Éxito! Se procesaron {count} criptomonedas en Neon.'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error de red: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error inesperado: {e}'))