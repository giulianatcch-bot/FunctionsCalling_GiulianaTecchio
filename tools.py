class ProductInfoTool:
    def get_info(self, product_name: str) -> str:
        # Simulazione database prodotti
        prodotti = {
            "maglione lana bio": "Realizzato in 100% lana merino biologica, certificata GOTS. Biodegradabile.",
            "jeans riciclati": "Denim ottenuto da cotone riciclato al 90%, risparmio idrico del 70%."
        }
        return prodotti.get(product_name.lower(), "Prodotto non trovato nel catalogo eco.")

class StockTool:
    def check_stock(self, product_name: str, size: str) -> str:
        # Simulazione controllo magazzino
        return f"Il prodotto '{product_name}' taglia {size} è attualmente disponibile in negozio."

class AppointmentTool:
    def book_appointment(self, date: str, time: str) -> str:
        # Simulazione prenotazione
        return f"Prenotazione confermata per una consulenza stile sostenibile il giorno {date} alle ore {time}."