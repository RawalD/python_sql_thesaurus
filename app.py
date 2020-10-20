import mysql.connector

connection = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = connection.cursor()
user_word = input("Enter word to search: ").lower()
query = cursor.execute(
    f"SELECT * FROM Dictionary WHERE Expression = '{user_word}'")
results = cursor.fetchall()

if results:
    print(f"{user_word.capitalize()} :")
    for result in results:
        print(result[1])
else:
    print("No Result Found")
