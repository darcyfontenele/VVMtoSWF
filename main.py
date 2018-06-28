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

for instance in list_instance:
    print(instance)

f = open("swttest.swf", "w+")
