import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load data from CSV file
data = pd.read_csv('bakery_pos_data.csv')

# Map user IDs and SKUs to unique integer indices
user_id_to_index = {user_id: index for index, user_id in enumerate(data['UserID'].unique())}
sku_to_index = {sku: index for index, sku in enumerate(data['SKU'].unique())}

# Create user-product interaction matrix
user_product_matrix = np.zeros((len(user_id_to_index), len(sku_to_index)), dtype=int)
for _, row in data.iterrows():
    user_index = user_id_to_index[row['UserID']]
    sku_index = sku_to_index[row['SKU']]
    user_product_matrix[user_index, sku_index] = row['Quantity']

# Calculate user similarity using cosine similarity
user_similarity = cosine_similarity(user_product_matrix)

# Get user recommendations for a specific user
def get_user_recommendations(user_id, num_recommendations=5):
    user_index = user_id_to_index[user_id]
    similar_users = user_similarity[user_index].argsort()[::-1][1:]
    rated_products = np.where(user_product_matrix[user_index] > 0)[0]
    recommended_products = set()

    for similar_user in similar_users:
        similar_user_rated_products = np.where(user_product_matrix[similar_user] > 0)[0]
        unrated_products = np.setdiff1d(similar_user_rated_products, rated_products)
        recommended_products.update(unrated_products)

        if len(recommended_products) >= num_recommendations:
            break

    return recommended_products

# Example usage
user_id = "User8"  # Replace with the desired UserID
recommended_product_indices = get_user_recommendations(user_id)
recommended_products = [list(sku_to_index.keys())[idx] for idx in recommended_product_indices]
print(f"Recommended products for {user_id}: {recommended_products}")
print("Loaded Data:")
print(data.head())
print()

print("User ID to Index Mapping:")
print(user_id_to_index)
print()

print("SKU to Index Mapping:")
print(sku_to_index)
print()
