import csv
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root")
cursor=conn.cursor()
cursor.execute('create database if not exists EcoChoice')
cursor.execute('use EcoChoice')

def create_table(table_name):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    query = f"""CREATE TABLE IF NOT EXISTS {table_name}(
           id BIGINT UNSIGNED PRIMARY KEY,
           name VARCHAR(100) ,
           manufacturer VARCHAR(100) ,
           price DECIMAL(10, 2) , 
           quantity Varchar(100) DEFAULT '0',
           description VARCHAR(250),
           certifications VARCHAR(250),
           image VARCHAR(500),
           rating decimal(10,2) default null
           );
           """
    cursor.execute(query)
    values = ''
    insert_query = f"insert into {table_name} (id,name,manufacturer, price, quantity, description, certifications, image) values {values};"

    csv_file = table_name+'.csv'
    file_path='./data_files/'+csv_file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                #print(row)
                values = tuple(row)
                insert_query = f"insert into {table_name} (id,name,manufacturer, price, quantity, description, certifications, image) values {values};"

                cursor.execute(insert_query)
        conn.commit()

    except FileNotFoundError:
        print('File not found')

category_dict={1:'laundry',2:'cleaning', 3:'misc_household', 4:'stationery', 5:'self_care', 6:'health'}
for table_name in category_dict.values():
    create_table(table_name)




cursor.close()
conn.close()

