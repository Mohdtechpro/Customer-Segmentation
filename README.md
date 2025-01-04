# Customer Segmentation Using K-means Clustering

## Project Overview
This project demonstrates customer segmentation using K-means clustering. It segments customers based on their age, spending behavior, and shopping mall attributes to provide insights for targeted marketing strategies.

## Features
- **Data Preprocessing**: Merging customer, invoice, and mall datasets.
- **Feature Engineering**: Total spent and store density.
- **Clustering**: Using K-means to create customer segments.
- **Visualization**: Scatter plots to show cluster distribution.

## Files and Folders
- **data/**:
  - `customer_data.csv`: Customer demographic data.
  - `sales_data.csv`: Transaction details.
  - `shopping_mall_data.csv`: Mall attributes.
- **scripts/**:
  - `customer_segmentation.py`: Python script for data processing and clustering.
- **visuals/**:
  - `elbow_curve.png`: Elbow method plot.
  - `customer_segments.png`: Cluster scatter plot.
- **README.md**: Project documentation.

## How to Run
1. Install the required libraries:
   ```bash
   pip install pandas matplotlib scikit-learn

2. Run the Python script:
python scripts/Mall Customer data.py

3. View the outputs:
Visualizations: ![Elbow Curve](https://github.com/user-attachments/assets/23032c45-5422-4cde-ad25-3ff4f71e6aec)
![Customer Segment](https://github.com/user-attachments/assets/b94f9942-ab1b-4c09-a024-317b7166598e)

## Visualizations
- Elbow Curve
- Customer Segments

## Insights
- Cluster 0: High-spending middle-aged customers.
- Cluster 1: Younger customers with moderate spending.
- Cluster 2: Senior customers with low spending.
- Cluster 3: Middle-aged customers with high store density visits.





