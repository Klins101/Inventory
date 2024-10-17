import pandas as pd

# Generating more data for stock_recommendations.csv
stock_data = {
    'product': [f'Dummy product {i}' for i in range(1, 21)],  # 20 products
    'current_stock': [233, 6, 8, 250, 98, 115, 267, 113, 100, 150, 95, 45, 300, 120, 60, 190, 180, 170, 140, 130],
    'optimal_stock': [120, 100, 100, 120, 50, 30, 50, 120, 80, 90, 70, 40, 150, 100, 60, 110, 90, 80, 70, 60],
    'category': ['high_demand']*10 + ['low_demand']*10
}
stock_df = pd.DataFrame(stock_data)

# Generating more data for product_recommendations.csv
product_data = {
    'product': [f'Dummy product {i}' for i in range(1, 21)],
    'item1': [f'Product {i}' for i in range(1, 21)],
    'item2': [f'Product {i}' for i in range(21, 41)],
    'type': ['related']*10 + ['bundle']*10
}
product_df = pd.DataFrame(product_data)

# Generating more data for price_recommendations.csv
price_data = {
    'product': [f'Dummy product {i}' for i in range(1, 21)],
    'current_price': [15, 29, 10.99, 25.49, 30, 40, 50, 60, 25, 22, 18, 35, 45, 55, 65, 75, 80, 90, 100, 110],
    'discount': [10, 50, 70, 25, 15, 20, 35, 45, 55, 30, 40, 25, 60, 70, 50, 20, 10, 15, 30, 40]
}
price_df = pd.DataFrame(price_data)

# Saving the data to CSV files
stock_df.to_csv('data/stock_recommendations.csv', index=False)
product_df.to_csv('data/product_recommendations.csv', index=False)
price_df.to_csv('data/price_recommendations.csv', index=False)
