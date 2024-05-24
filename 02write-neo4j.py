from neo4j import GraphDatabase
import pandas as pd
import csv
import json
from neo4j.exceptions import Neo4jError
# Neo4j数据库的连接参数
uri = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"

df = pd.read_csv("triple.csv",header=None)

# 将CSV文件中的每一行转换为字典
data = []
for index, row in df.iterrows():
    row[0]=row[0].replace("'","\"")
    row[2] = row[2].replace("'", "\"")
    # print(row[2])
    row0=json.loads(row[0])
    row2 = json.loads(row[2])
    # print(row2)

    triple = {"subject": row0, "predicate": row[1], "object": row2}
    data.append(triple)
# print(data)


# 连接Neo4j数据库
driver = GraphDatabase.driver(uri, auth=(user, password))

# 在Neo4j中创建节点和关系
with driver.session() as session:
    for triple in data:
        # 创建节点
        session.run("MERGE (s:"+triple['subject']['label']+" {name: $subject1})", subject1=triple['subject']['text'] )
        session.run("MERGE (o:"+triple['object']['label']+" {name: $object1})", object1=triple['object']['text'] )

        # 创建关系
        session.run("MATCH (s:"+triple['subject']['label']+" {name: $subject1}), (o:"+triple['object']['label']+" {name: $object1}) "
                    "MERGE (s)-[:"+triple['predicate']+"]->(o)", subject1=triple['subject']['text'] , object1=triple['object']['text'] )

# 关闭Neo4j驱动程序
driver.close()
