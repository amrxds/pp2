from configparser import ConfigParser
import psycopg2
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config


pattern = input("Enter pattern to filter: ")
def query_data_with_pattern(pattern):
    conn = None

    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        
        # Запрос данных на основе шаблона
        cursor.execute("SELECT * FROM PhoneBook WHERE username LIKE %s OR phone_number LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
        rows = cursor.fetchall()

        # Вывод результатов
        if rows:
            print("Результаты:")
            for row in rows:
                print("ID:", row[0])
                print("Имя пользователя:", row[1])
                print("Номер телефона:", row[2])
        else:
            print("Нет результатов для указанного шаблона.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с базой данных закрыто.")

if __name__ == '__main__':

    config = load_config()
    query_data_with_pattern(pattern)