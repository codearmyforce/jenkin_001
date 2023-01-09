import sqlglot

sql = """select * from employee"""
output=sqlglot.transpile(sql, write='spark', identify=True, pretty=True)[0]
print(output)

