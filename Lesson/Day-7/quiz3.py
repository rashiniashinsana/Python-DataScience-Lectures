import pandas as pd 

data = {
    # 'Order_ID' : [101, 102, 103, 104, 105],
    'Product' : ["Laptop", 'Smartphone', 'DeskChair', 'Monitor', 'Bookshelf'],
    'Category' : ['Electornic','Electornic', 'Furniture', 'Electronic', 'Furniture'],
    'QTY' : [2, 5, 10, 4, 2],
    'Price_per_unit' : [1000, 800, 50, 200, 300],
}


df = pd.DataFrame(data, index=[101, 102, 103, 104, 105])

print("Q1)\n",df)


df['total_revenue'] = df['QTY'] * df['Price_per_unit']
print("\nQ2)\n",df)

best_selling_index = df['total_revenue'].idxmax()  
best_selling_product = df.loc[best_selling_index]
print("\nBest-selling product:\n", best_selling_product)


# best_selling_index = df['total_revenue'] == df['total_revenue'].max()
# print(best_selling_index)
