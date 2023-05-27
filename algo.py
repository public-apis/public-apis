def generate_orders(data):
    volume = data['volume']
    number_of_orders = data['number']
    amount_difference = data['amountDif']
    side = data['side']
    price_min = data['priceMin']
    price_max = data['priceMax']
    
    orders = []
    for i in range(number_of_orders):
        order_size = int((volume * random() + 1) // 100)
        if side == 'PRODAIT':
            currency = 'USDT' 
            exchange_rate = 100.0
            price = round(random() * 100.0 + price_min / 100.0, 4)
            fee = round(order_size * 0.001 * 100, 4) 
            amount = round(order_size - fee, 8) 
            total_fee = round(amount * 100.0 + fee, 4)
            
         
            btc_amount = amount // exchange_rate
            
            
            orders.append({
                'id': f"ORDER_{i}",
                'symbol': f"{currency}_BTC",
                'isMarketOrder': True,
                'type': 'LIMIT',
                'timeInForce': None,
                'quantityQty': btc_amount,
                'price': str(round(price, 6)),
                'totalFeesCurrency': str(amount),
                'baseAssetAmount': str(btc_amount),
                'settleTimestamp': None,
                'timestamp': time(),
                'fills': [],
                'status': 'PENDING',
                'ordertype': 'LIMIT',
                'limitPrice': str(price),
                'stopLimit': False,
                'icebergQuantity': 0,
                'parentId': '',
                'quoteAssetAmount': amount
            })
