import requests

class CurrencyConverter:
        def __init__(self):
                    # In a real application, this data would come from an external API
                            self.exchange_rates = {
                                                'USD': 1,            # Assuming USD as base
                                                            'EUR': 0.85,
                                                                        'GBP': 0.75,
                                                                                    'INR': 75.50,
                                                                                                'JPY': 110.25
                                                                                                        }

                                def convert(self, amount, from_currency, to_currency):
                                            if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
                                                            return "Currency not supported"

                                                                # Convert from base currency (USD)
                                                                        amount_in_usd = amount / self.exchange_rates[from_currency]
                                                                                # Convert to target currency
                                                                                        converted_amount = amount_in_usd * self.exchange_rates[to_currency]
                                                                                                return round(converted_amount, 2)

                                                                                            # Example Usage
                                                                                            converter = CurrencyConverter()
                                                                                            amount = 100
                                                                                            from_currency = 'EUR'
                                                                                            to_currency = 'INR'

                                                                                            converted_amount = converter.convert(amount, from_currency, to_currency)
                                                                                            print(f"{amount} {from_currency} is {converted_amount} {to_currency}")

