admin_table  = "admin"
getAdminByLogin = "SELECT * FROM " + admin_table + " WHERE username=%s AND password=%s"
getAdminById = "SELECT * FROM " + admin_table + " WHERE id=%s"
getAllAdmin = "SELECT * FROM " + admin_table
addAdmin = "INSERT INTO " + admin_table + " (username, password, role)" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

shop_table = "shop"
getShopById = "SELECT * FROM " + shop_table + " WHERE id=%s"
getAllShop = "SELECT * FROM " + shop_table
addShop = "INSERT INTO " + shop_table + " (username, password, role)" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"



