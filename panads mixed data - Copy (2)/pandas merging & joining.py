import pandas as pd
df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "name":['shreshth','Kajal','Aman']
})
df_orders=pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,450,550]
})
df_merged=pd.merge(df_customers , df_orders , on="CustomerID", how="right")
print("outer join")
print(df_merged)
