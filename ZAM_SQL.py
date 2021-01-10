DT_sql = ['INTEGER','TEXT','REAL','BLOB','NULL']

def DB_CT(table_name = "zyad",columns=['fname'],type_data=[DT_sql[1]]):
    instruction = "CREATE TABLE " + table_name + " ( "
    for i in range(len(columns)):
        if i != 0 :
            instruction = instruction +" , "
        instruction = instruction + columns[i] + " " + type_data[i]
    instruction = instruction + " );"
    print(instruction)
    return instruction

def DB_insert(table_name='zyad',columns=['fname'],values=['zyaaaad'],type_data=[DT_sql[1]]):
    instruction = "INSERT INTO " + table_name + " ("
    part_VALUES="VALUES ("
    for i in range(len(values)):
        if i != 0 :
            instruction = instruction +" , "
            part_VALUES = part_VALUES +" , "
        if type_data[i] == DT_sql[1] :
            part_VALUES = part_VALUES +"'"+values[i]+"'"
        else:
            part_VALUES = part_VALUES + values[i]
        instruction = instruction + columns[i]
    instruction = instruction + ") " + part_VALUES + ");"
    print(instruction)
    return instruction


if __name__ == '__main__' :
    print(' this is made by zyad mackawy ')
