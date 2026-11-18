"""查询已收到的轨迹片段原文及其来源身份。"""
from .ledger import entities

def current(connection, collection):
    result = []
    for row in entities(connection, collection):
        if row['type'] != 'trajectory_chunk':
            continue
        result.append({'id': row['id'], 'version': row['version'],
                       'source_sha256': row['source'], **row['payload']})
    return result
