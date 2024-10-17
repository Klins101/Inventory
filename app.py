from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data from CSV files
def load_stock_recommendations():
    stock_df = pd.read_csv('data/stock_recommendations.csv')
    high_demand = stock_df[stock_df['category'] == 'high_demand'].to_dict('records')
    low_demand = stock_df[stock_df['category'] == 'low_demand'].to_dict('records')
    return {'high_demand': high_demand, 'low_demand': low_demand}

def load_product_recommendations():
    product_df = pd.read_csv('data/product_recommendations.csv')
    related_products = product_df[product_df['type'] == 'related'].to_dict('records')
    bundle_offers = product_df[product_df['type'] == 'bundle'].to_dict('records')
    return {'related_products': related_products, 'bundle_offers': bundle_offers}

def load_price_recommendations():
    price_df = pd.read_csv('data/price_recommendations.csv')
    return {'high_search_low_purchase': price_df.to_dict('records')}

@app.route('/')
def inventory_optimization():
    view_all = request.args.get('view_all', 'false').lower() == 'true'

    # Load data from CSV files
    stock_recommendations = load_stock_recommendations()
    product_recommendations = load_product_recommendations()
    price_recommendations = load_price_recommendations()

    # Limit to first 4 records if 'view_all' is not set to True
    if not view_all:
        stock_recommendations['high_demand'] = stock_recommendations['high_demand'][:4]
        stock_recommendations['low_demand'] = stock_recommendations['low_demand'][:4]
        product_recommendations['related_products'] = product_recommendations['related_products'][:4]
        product_recommendations['bundle_offers'] = product_recommendations['bundle_offers'][:4]
        price_recommendations['high_search_low_purchase'] = price_recommendations['high_search_low_purchase'][:4]

    return render_template('inventory_optimization.html', 
                           stock_recommendations=stock_recommendations,
                           product_recommendations=product_recommendations,
                           price_recommendations=price_recommendations,
                           view_all=view_all)

if __name__ == '__main__':
    app.run(debug=True)
