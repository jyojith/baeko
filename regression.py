import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the generated data
data = pd.read_csv('bakery_pos_data.csv')

# Define bakery items with SKUs, names, and prices
bakery_items = [
    { 'sku': "SKU101", 'name': "Croissant", 'price': 2.5 },
    { 'sku': "SKU102", 'name': "Chocolate Cake", 'price': 15.0 },
    { 'sku': "SKU103", 'name': "Blueberry Muffin", 'price': 2.0 },
    { 'sku': "SKU104", 'name': "Roggenmischbrot", 'price': 3.0 },
    { 'sku': "SKU105", 'name': "Weißbrot", 'price': 2.0 },
    { 'sku': "SKU106", 'name': "Dinkelbrötchen", 'price': 1.5 },
    { 'sku': "SKU107", 'name': "Baguette", 'price': 3.5 },
    { 'sku': "SKU108", 'name': "Brezel", 'price': 1.0 },
    { 'sku': "SKU109", 'name': "Apple Strudel", 'price': 4.5 },
    { 'sku': "SKU110", 'name': "Cinnamon Roll", 'price': 2.2 },
    { 'sku': "SKU111", 'name': "Sourdough Bread", 'price': 3.8 },
    { 'sku': "SKU112", 'name': "Cherry Danish", 'price': 3.0 },
    { 'sku': "SKU113", 'name': "Eclair", 'price': 2.8 },
    { 'sku': "SKU114", 'name': "Pretzel", 'price': 1.2 },
    { 'sku': "SKU115", 'name': "Bagel", 'price': 1.8 },
    { 'sku': "SKU116", 'name': "Fruit Tart", 'price': 4.2 },
    { 'sku': "SKU117", 'name': "Almond Croissant", 'price': 3.3 },
    { 'sku': "SKU118", 'name': "Pumpernickel Bread", 'price': 2.7 },
    { 'sku': "SKU119", 'name': "Strawberry Shortcake", 'price': 5.5 },
    { 'sku': "SKU120", 'name': "Pain au Chocolat", 'price': 2.7 },
    # Add more bakery items here...
]

# Select features for the linear regression model
features = ['TransactionID', 'Quantity', 'Price']  # You can add more features if needed

# Select the target variable (demand/quantity)
target = 'Quantity'

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Dictionary to store product-specific predictions
product_predictions = {}

# Loop through bakery items
for bakery_item in bakery_items:
    sku = bakery_item['sku']
    item_data = test_data[test_data['SKU'] == sku]

    # Train the model using the training data
    model.fit(train_data[features], train_data[target])

    # Make predictions on the item's test data
    predictions = model.predict(item_data[features])

    # Store predictions for the product
    product_predictions[sku] = {
        'actual': item_data[target].tolist(),
        'predicted': predictions.tolist()
    }

    # Plot actual quantity vs. predicted quantity for the current product
    plt.figure(figsize=(10, 6))
    plt.scatter(item_data[target], predictions, color='blue')
    plt.xlabel('Actual Quantity')
    plt.ylabel('Predicted Quantity')
    plt.title(f'Actual vs. Predicted Quantity for Product {sku}')
    plt.grid()
    plt.show()

# Print product-specific predictions
for sku, predictions in product_predictions.items():
    print(f"Product {sku}:")
    print("Actual Quantities:", predictions['actual'])
    print("Predicted Quantities:", predictions['predicted'])
    print()
