import pandas
import openpyxl

df = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")
print(df)
print(df.values.tolist())
print("-"*100)

print(df.loc[0])
print(df.loc[0].tolist())
print(list(df.loc[0]))
print(tuple(df.loc[1]))

print(df.index)
print(60 * "-")

list = []
for i in df.index:
    print(df.loc[i].tolist())
    list.append(df.loc[i].tolist())
print(list)

print(60 * "-")
list = []
for i in df.index:
    print(tuple(df.loc[i]))
    list.append(tuple(df.loc[i]))
print(list)

print(60 * "-")
df=pandas.read_excel(io="../test_data/login_test_data.xlsx", sheet_name="test_add_valid_employee")
print(df)

print(df.values.tolist())

print(df.get(["User Name"]))

print("*"*100)
print("*"*100)
print("*"*100)

"""read json file"""
dic=pandas.read_json(path_or_buf="../test_data/data.json",typ="dictionary")
print(dic)
print(dic['browser'])
print(dic[1])
