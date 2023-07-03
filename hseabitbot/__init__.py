import requests, pandas, numpy

file = requests.get(f"https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_AMI.xlsx")
pandas_transformed_file = pandas.read_excel(file.content, 'TDSheet')

def replace_with_ones(table: numpy.ndarray) -> None:
    table[(table == 'Да') | (table == 'Yes')] = 1
    table[(table == 'Нет') | (table == 'No')] = 0

a = pandas_transformed_file.to_numpy()

replace_with_ones(a)

print(a[17,])

print(numpy.sum(a[16:, 4] * a[16:, ]))