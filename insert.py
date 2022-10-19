from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_books(books):
    query = "INSERT INTO test(id,name) " \
            "VALUES(%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    id1=input('Type your id: ')
    el1=input('Type your text: ')
    books = [(id1, el1)]
    insert_books(books)

if __name__ == '__main__':
    main()
