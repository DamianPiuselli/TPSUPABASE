import pandas as pd

if __name__ == "__main__":

    # Carga de datasets
    df_sales = pd.read_csv(rf"Sales_Data\annex2.csv")
    df_item = pd.read_csv(rf"Sales_Data\annex4.csv")
    df_category = pd.read_csv(rf"Sales_Data\annex1.csv")
    df_wholesale = pd.read_csv(rf"Sales_Data\annex3.csv")

    # Normalizacióm de tabla items
    df_item = df_item.merge(
        df_category[["item_code", "category_code"]], how="left", on="item_code"
    )

    # Normalización de tabla category
    df_category = df_category.drop(["item_code", "item_name"], axis=1)

    df_category = df_category.drop_duplicates().reset_index(drop=True)

    # Normalización de tabla sales
    df_sales = df_sales[
        [
            "quantity_sold",
            "unit_selling_price",
            "sale_or_return",
            "discount",
            "date",
            "time",
            "item_code",
        ]
    ]

    # Normalización de tabla wholesale
    df_wholesale = df_wholesale[["date", "wholesale_price", "item_code"]]

    # Save dataframes to CSV in a folder named "parsed"
    df_sales.to_csv(r"parsed/df_sales.csv", index=False)
    df_item.to_csv(r"parsed/df_item.csv", index=False)
    df_category.to_csv(r"parsed/df_category.csv", index=False)
    df_wholesale.to_csv(r"parsed/df_wholesale.csv", index=False)
