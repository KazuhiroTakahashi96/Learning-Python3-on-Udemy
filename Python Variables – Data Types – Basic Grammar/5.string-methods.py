# ------------------------------------------------------------
# -----------------**## String Methods ##**-------------------

# 1- len() 文字の長さ
address = "Afghanistan"
print(address)
# print(len(address))

# 2- [] Notation インデックス番号の値を教えてくれる
# print(address[0])
# print(address[7])
# print(address[-1])
# print(address[-4])

# 3- [] Notation
# print(address[0:4])
# print(address[-7:-1])
# print(address[0:])
# print(address[:9])
# print(address[:])

# 4- Concatenation ->>>> Formatted Strings くっ付ける
country = "USA"
city = "NYC"
# full_address = city + ", " + country
# full_address = f"{city}, {country}"
# print(full_address)

# 5- upper() 大文字にする
# print(address.upper())

# 6- lower()　小文字にする
# print(city.lower())

# 7- title() 単語の最初の文字だけ大文字にする
# print(full_address.title())

# 8- strip() 空白を削除する？ lは左側、rは右側だけ
# job = "       Programmer   "
# print(job)
# print(job.strip())
# print(job.lstrip())
# print(job.rstrip())

# 9- find() その文字が何番目か返す(インデックス番号で)
# print(address.find("n"))
# print(address.find("i"))

# 10- replace() 置換する
# print(address.replace("f", "Z"))

# 11- in operator 存在するかbooleanで返す
# print("ne" in address)
# print("ni" in address)

# 12- not operator
# print("ne" not in address)
# print("ni" not in address)
