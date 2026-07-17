
#create the database connection
connection = mysql.connector.connect(host = "localhost" , username = "root" , password = "123456789" , database = "todo")

# to check the connection is establish or not
if connection.is_connected():
    print("database is connected")
else:
    print("database is not connected")

#create table for todo app task
task = "create table if not exists task (taskname text , mobile text)"

