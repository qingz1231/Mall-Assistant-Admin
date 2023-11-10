admin_table  = "admin"
getAdminByLogin = "SELECT * FROM " + admin_table + " WHERE username=%s AND password=%s"
getAdminById = "SELECT * FROM " + admin_table + " WHERE user_id=%s"
getAllAdmin = "SELECT * FROM " + admin_table
addAdmin = "INSERT INTO " + admin_table + " (mall_id, username, password, role)" + " VALUES (%s, %s, %s, %s)"
deleteAdmin = "DELETE FROM " + admin_table + " WHERE user_id = %s"
updateAdminDevice = "UPDATE " + admin_table + " SET device = %s WHERE user_id = %s"
updateAdminDetail = "UPDATE " + admin_table + " SET password = %s, role = %s WHERE user_id = %s"

shop_table = "shop"
getShopById = "SELECT * FROM " + shop_table + " WHERE id=%s"
getAllShop = "SELECT * FROM " + shop_table
addShop = "INSERT INTO " + shop_table + " (mall_id, shop_name, shop_location, shop_desc, image_url, tags)" + " VALUES (%s, %s, %s, %s, %s, %s)"
deleteShop = "DELETE FROM " + shop_table + " WHERE shop_id = %s"



