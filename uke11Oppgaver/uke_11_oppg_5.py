from decimal import *


class NoPrice(Exception):
    """Exception for when there is no price for the product"""
    pass


class NotEnoughPaid(Exception):
    """Exception for when customer has not paid enough"""
    pass


def product_price(product, prices_filename):
    price = False
    with open(prices_filename, 'r') as prices:
        for line in prices:
            name, file_price = line.strip().split(';')
            if name == product:
                price = file_price
    if price == False:
        raise NoPrice
    return Decimal(str(price))


def product_amount(a, product, cash_register_filename):
    """Get amount of product in cash register history"""
    amount = 0
    with open(cash_register_filename, "r") as cash_register:
        for line in cash_register:
            action, name = line.strip().split(";")
            if name == product and a == action:
                amount += 1
    return int(amount)


def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    # din kode her
    purchase_return_list = []
    products = []
    returned_list = []
    returned_product = []
    total = Decimal(0)
    paid = Decimal(0)

    with open(cash_register_filename, 'r') as cash_register:
        with open(prices_filename, 'r') as prices:
            for line in cash_register:
                action, value = line.strip().split(';')
                if action == 'pay':
                    paid += Decimal(str(value))
                elif action == 'buy':
                    if value in products:
                        continue
                    products.append(value)

                    amount = product_amount(action, value, cash_register_filename)
                    cost = product_price(value, prices_filename) * Decimal(str(amount))
                    total += cost
                    purchase_return_list.append(tuple((amount, value, cost)))

                elif action == 'return':
                    if value in returned_product:
                        continue
                    returned_product.append(value)
                    amount = product_amount(action, value, cash_register_filename)
                    cost = product_price(value, prices_filename) * Decimal(str(amount)) * -1
                    total += cost
                    returned_list.append(tuple((amount * -1, value, cost)))
    purchase_return_list.sort(key=lambda x: x[1])
    returned_list.sort(key=lambda x: x[1])
    for tuples in returned_list:
        purchase_return_list.append(tuples)

    mva_total = total * Decimal('0.2')
    change = total - paid

    if change > 0:
        raise NotEnoughPaid
    return tuple((purchase_return_list, total, mva_total, paid, change))


def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)

#print(receipt('prices.txt', 'cash_register.txt'))