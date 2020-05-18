def add_new_column_in_new_file(name_old_file, name_new_file):
    data = open(name_old_file, 'r', encoding='utf-8')
    new_data = open(name_new_file, 'a+', encoding='utf-8')
    next(data)
    new_data.write('file;N;-2;-1;0;1;2;p-2;p-1;p0;p1;p2;TypeExperiment;Target;N_Type_Target;N_Type;Type_Target;N_Target;Hit;Type_Result;Target_Result;Result_N_Type_Target;N_Type_Result;Type_Target_Result;N_Target_Result' + '\n')
    splited_data = []
    for line in data:
        splited_data = line.split(';')
        new_data.write(line.replace('\n', ''))
        for i in range(12, 18):
            new_data.write(';' + splited_data[i] + '_' + splited_data[18].replace('\n', ''))
        new_data.write('\n')


add_new_column_in_new_file('VGorb_plus_res.csv', 'VGorb_with_new_column.csv')
add_new_column_in_new_file('W2Gorb_plus_res.csv', 'W2Gorb_with_new_column.csv')

# Замечание:
# Type_Result = 12 + 18
# Target_Result = 13 + 18
# Result_N_Type_Target = 14 + 18
# N_Type_Result = 15 + 18
# Type_Target_Result = 16 + 18
# N_Target_Result = 17 + 18