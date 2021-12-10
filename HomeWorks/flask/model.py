import pymysql

def getStaff():
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'QAZ1234'
    db = 'ikea'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()

    sql = """
    SELECT _id, name, id, price, URL, imgPath FROM ikea_data;
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def getStaff():
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'QAZ1234'
    db = 'ikea'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()

    sql = """
    SELECT _id, name, productID, price, URL, imgPath FROM pinkoi_data;
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data



if __name__ == '__main__':
    for r in getStaff():
        print(r)