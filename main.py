'''
Author: javohir-a abdusamatovjavohir@gmail.com
Date: 2025-01-11 21:03:15
LastEditors: javohir-a abdusamatovjavohir@gmail.com
LastEditTime: 2025-01-11 21:03:21
FilePath: /todo_app/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

# Student data (replace this with your actual data structure)
students = [
    {"first_name": "Abdulloh", "last_name": "Normaxammadov"},
    {"first_name": "Afruzbek", "last_name": "Buxorov Adham o'g'li"},
    {"first_name": "Asilbek", "last_name": "Nurboyev Shohiddin o'g'li"},
    {"first_name": "Azizbek", "last_name": "Mirzavaliyev Ilyosbek o'g'li"},
    {"first_name": "Azizbek", "last_name": "Xayrullayev Askar o'g'li"},
    {"first_name": "Behruz", "last_name": "Eshdavlatov Behzod o'g'li"},
    {"first_name": "Bekzod", "last_name": "Niyozov Davlatali o'g'li"},
    {"first_name": "Bexruz", "last_name": "Hakimov Hamidovich"},
    {"first_name": "Bilol", "last_name": "Erkinboyev G'yrat o'g'li"},
    {"first_name": "Boburxon", "last_name": "Mahamatov Mahmud o'g'li"},
    {"first_name": "Diyorbek", "last_name": "Xaydarov Dilmurod o'g'li"},
    {"first_name": "Elchin", "last_name": "Toyirov Xusan o'g'li"},
    {"first_name": "Ibrohimjon", "last_name": "Bahodirov Bunyodjon o'g'li"},
    {"first_name": "Isfandiyor", "last_name": "Vohidov"},
    {"first_name": "Isroil", "last_name": "Muxtorov Isoq o'g'li"},
    {"first_name": "Javohirbek", "last_name": "Rahmatillayev Mamatohir O'g'li"},
    {"first_name": "Nurmuhammad", "last_name": "Mahmudov Farxod o'g'li"},
    {"first_name": "Zikrilloxon", "last_name": "Imomaliyev Nurali o'g'li"},
]

# Directory where folders will be created
base_directory = "students_directories"

# Create base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Create directories for each student
for student in students:
    directory_name = student["first_name"]
    directory_path = os.path.join(base_directory, directory_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    else:
        print(f"Directory already exists: {directory_path}")

print("All directories created.")
