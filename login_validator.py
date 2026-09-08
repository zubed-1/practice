username = input("Username: ")
password = input("Password: ")
valid_username = "admin"
valid_password = "1234"
if username == valid_username and password == valid_password:
    print("Login successful")
else:
    print("Invalid username or password")
