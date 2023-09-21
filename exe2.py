import sqlite3
import os


with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()


connection = sqlite3.connect("stephen_king_adaptations.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
        movieID INTEGER PRIMARY KEY,
        movieName TEXT,
        movieYear INTEGER,
        imdbRating REAL
    )
"""
for line in stephen_king_adaptations_list:
    movie_data = line.strip().split(',')
    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
                   (movie_data[0], int(movie_data[1]), float(movie_data[2])))
connection.commit()


while True:
    print("选项:")
    print("1. 电影名称搜索")
    print("2. 电影年份搜索")
    print("3. 电影评分搜索")
    print("4. 停止")
    choice = input("请输入您的选择: ")

    if choice == "1":
        movie_name = input("请输入电影名称: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        result = cursor.fetchone()
        if result:
            print(f"电影名称: {result[1]}")
            print(f"电影年份: {result[2]}")
            print(f"IMDB评分: {result[3]}")
        else:
            print("我们的数据库中没有找到这部电影")
    elif choice == "2":
        movie_year = input("请输入电影年份: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (int(movie_year),))
        results = cursor.fetchall()
        if results:
            for result in results:
                print(f"电影名称: {result[1]}")
                print(f"电影年份: {result[2]}")
                print(f"IMDB评分: {result[3]}")
        else:
            print("我们的数据库中没有找到该年份的电影")
    elif choice == "3":
        movie_rating = input("请输入最低IMDB评分: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (float(movie_rating),))
        results = cursor.fetchall()
        if results:
            for result in results:
                print(f"电影名称: {result[1]}")
                print(f"电影年份: {result[2]}")
                print(f"IMDB评分: {result[3]}")
        else:
            print("数据库中没有找到符合该评分标准的电影")
    elif choice == "4":
        break

connection.close()
