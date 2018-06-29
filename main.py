import csv

# list_vvm_files = ['snap01.csv','snap02.csv','snap03.csv','snap04.csv','snap05.csv','snap06.csv','snap07.csv']
list_csv_files = ['snap01.csv']
list_instance = []

print("Reading VisualVM files...")

for vvm_file in list_csv_files:
    print("Reading VisualVM file: ",vvm_file)
    with open(vvm_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        list_instance_tmp = None
        for line in reader:
            # print(line["Class Name - Live Objects"]),
            # print(line["Live Bytes [%]"]),
            # print(line["Live Bytes"]),
            # print(line["Live Objects"])
            list_instance_tmp = [line["Class Name - Live Objects"], line["Live Bytes [%]"],
                                 line["Live Bytes"], line["Live Objects"]]
            list_instance.append(list_instance_tmp)
        csvfile.close()

with open("DellWorkload.swf", "w+") as f:
    print("Writing SWF file...")
    f.write(';1-Job Number\n')
    f.write(';2-Submit Time\n')
    f.write(';3-Wait Time\n')
    f.write(';4-Run Time\n')
    f.write(';5-Number of Allocated Processors\n')
    f.write(';6-Average CPU Time Used\n')
    f.write(';7-Used Memory\n')
    f.write(';8-Request Number of Processors\n')
    f.write(';9-Requested Time\n')
    f.write(';10-Requested Memory\n')
    f.write(';11-Status\n')
    f.write(';12-User ID\n')
    f.write(';13-Group ID\n')
    f.write(';14-Executable (Application) Number\n')
    f.write(';15-Queue Number\n')
    f.write(';16-Partition Number\n')
    f.write(';17-Preceding Job Number\n')
    f.write(';18-Think Time From Preceding Job\n')
    f.write(';\n')
    index = 1
    submit_sum = 0
    run_time = 10
    for instance in list_instance:
        f.write('{} {} -1 {} -1 -1 {} -1 -1 -1 -1 1 1 -1 -1 -1 -1 -1 \n'.format(index, submit_sum, run_time, instance[2]))
        index += 1
        submit_sum += run_time
    f.close()
