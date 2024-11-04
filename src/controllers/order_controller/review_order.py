
def review_order(order):
    if(order):
        total = 0
        print('{:<20}{:<10}{:<10}{:<10}'.format('NAME', 'RATE', 'QTY', 'TOTAL'))
        print('-'*50)
        for item in order:
            sum = item['sale_price'] * item['quantity']
            total += sum
            print('{:<20}{:<10}{:<10}{:<10}'.format(item['name'], item['sale_price'], item['quantity'], sum))

        print(f'TOTAL : {total}')
    else:
        print('items not available to review') 