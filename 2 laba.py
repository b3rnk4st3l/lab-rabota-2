def get_shopping_list():
    shopping_list = {}
    num_items = int(input("Введите количество товаров: "))
    for i in range(num_items):
        item_name = input("Введите название товара: ")
        shops = int(input("Введите количество магазинов, в которых продается данный товар: "))
        prices = {}
        for j in range(shops):
            shop_name = input(f"Введите название магазина {j + 1}: ")
            price = float(input(f"Введите цену товара {item_name} в магазине {shop_name}: "))
            prices[shop_name] = price
        shopping_list[item_name] = prices
    return shopping_list

def find_best_deal(shopping_list):
    overall_costs = {}
    for item in shopping_list:
        best_deal_shop = min(shopping_list[item], key=shopping_list[item].get)
        overall_costs[best_deal_shop] = overall_costs.get(best_deal_shop, 0) + shopping_list[item][best_deal_shop]
    best_deal = min(overall_costs, key=overall_costs.get)
    return overall_costs, best_deal


shopping_list = get_shopping_list()
overall_costs, best_deal = find_best_deal(shopping_list)

print("Список магазинов и общая стоимость покупок в каждом:")
for shop in overall_costs:
    print(shop, ":", overall_costs[shop])
print("Магазин, в котором можно сэкономить больше всего денег:", best_deal)
