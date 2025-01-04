import pandas as pd

# Load the datasets
customer_data_path = "C:\Project_Git\Machine Learning\customer_data.csv"  # Replace with actual paths
invoice_data_path = "C:\Project_Git\Machine Learning\sales_data.csv"
mall_data_path = "C:\Project_Git\Machine Learning\shopping_mall_data.csv"

customer_data = pd.read_csv(customer_data_path)
invoice_data = pd.read_csv(invoice_data_path)
mall_data = pd.read_csv(mall_data_path)

# Preview datasets
print(customer_data.head())
print(invoice_data.head())
print(mall_data.head())

# Merge invoice data with customer data on 'customer_id'
customer_invoice_data = pd.merge(invoice_data, customer_data, on="customer_id", how="inner")

# Merge with mall data on 'shopping_mall'
full_data = pd.merge(customer_invoice_data, mall_data, on="shopping_mall", how="inner")

# Preview the merged data
print(full_data.head())

# Calculate total spent
full_data['total_spent'] = full_data['price'] * full_data['quantity']

# Convert area to numeric and calculate store density
full_data['area (sqm)'] = full_data['area (sqm)'].str.replace(',', '').astype(float)
full_data['store_density'] = full_data['store_count'] / full_data['area (sqm)']

# Select relevant features for clustering
features = full_data[['age', 'total_spent', 'store_density']]

# Handle missing values (if any)
features.fillna(0, inplace=True)

print(features.head())

from sklearn.preprocessing import StandardScaler

# Standardize numerical features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(scaled_features[:5])

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Determine optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid()
plt.show()

# Apply K-means with the optimal number of clusters
optimal_clusters = 4  # Replace with the elbow point
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
full_data['Cluster'] = kmeans.fit_predict(scaled_features)

# Preview the clustered data
print(full_data[['customer_id', 'Cluster']].head())

import seaborn as sns

# Visualize clusters based on total_spent and age
plt.figure(figsize=(10, 6))
sns.scatterplot(x=full_data['age'], y=full_data['total_spent'], hue=full_data['Cluster'], palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Age')
plt.ylabel('Total Spent')
plt.legend(title='Cluster')
plt.grid()
plt.show()
