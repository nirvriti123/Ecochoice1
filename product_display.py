import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root", database="EcoChoice")
cursor=conn.cursor(dictionary=True)




groups = {
    "laundry": {
        "Detergents": [11, 12, 13],
        "Fabric Softeners": [21, 22, 23],
        "Stain Removers": [31, 32, 33]
    },
    "cleaning": {
        "Surface Cleaners": [11, 12, 13, 21, 22, 23, 31, 32, 33],
        "Bathroom": [41, 42, 43],
        "Dish care": [51, 52, 53, 61, 62, 63, 71, 72, 73]
    },
    "misc_household": {
        "Air Care": [11, 12, 13],
        "Paper Products": [21, 22, 23, 31, 32, 33]
    },
    "stationery": {
        "Writing Essentials": [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43],
        "Paper": [51, 52, 53, 61, 62, 63],
        "Arts and Crafts": [111, 112, 113, 121, 122, 123],
        "Office Basics": [71, 72, 73, 81, 82, 83, 91, 92, 93, 101, 102, 103]
    },
    "self_care": {
        "Skincare": [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43],
        "Haircare": [51, 52, 53, 61, 62, 63, 71, 72, 73],
        "Oral Hygiene": [81, 82, 83, 91, 92, 93, 101, 102, 103, 111, 112, 113],
        "Bath and Body": [121, 122, 123, 131, 132, 133, 141, 142, 143, 151, 152, 153, 161, 162, 163]
    },
    "health": {
        "First Aid": [11, 12, 13, 21, 22, 23, 41, 42, 43],
        "Health monitoring": [31, 32, 33]
    }
}


def products(category, product_category="All products"):
    products=[]
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="EcoChoice"
    )
    cursor = conn.cursor(dictionary=True)

    try:
        if product_category == "All products":
            query = f"""SELECT * FROM {category}"""
            cursor.execute(query)
            products += [cursor.fetchall()]
        else:
            products = []
            ids = groups[category.lower()][product_category]
            for i in ids:
                query = f"""(SELECT * FROM {category} WHERE id = %s);"""
                cursor.execute(query, (i,))
                products += cursor.fetchall()

        return products

    finally:
        cursor.close()
        conn.close()


