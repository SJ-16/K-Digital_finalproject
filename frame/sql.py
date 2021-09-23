class Sql:
    selone = "SELECT * FROM main.client WHERE pwd='%s' AND email='%s'"
    selall = "SELECT * FROM main.client"
    insert = "INSERT INTO main.client (pwd,name,email,phone_num) VALUES ('%s','%s','%s','%s')"
    update = "UPDATE main.client SET pwd='%s', name='%s', email='%s',phone_num='%s' WHERE id='%s'"
    delete = "DELETE FROM main.client WHERE email='%s'"