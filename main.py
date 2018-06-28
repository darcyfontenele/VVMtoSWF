import csv

# list_vvm_files = ['snap01.csv','snap02.csv','snap03.csv','snap04.csv','snap05.csv','snap06.csv','snap07.csv']
list_vvm_files = ['snap01.csv']


print("Reading VisaulVM files...")

vvm_class = {}
vvm_total = 0

for vvm_file in list_vvm_files:
    print("Reading VisualVM file: ",vvm_file)
    with open(vvm_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for line in reader:
            print(line["Class Name - Live Objects"]),
            print(line["Live Bytes [%]"]),
            print(line["Live Bytes"]),
            print(line["Live Objects"])
            if line["Class Name - Live Objects"].startswith('br.org.eldorado.ead2pcd.'):
                (a,b,class_name) = line["Class Name - Live Objects"].rpartition('.')
                (class_name,a,b) = class_name.rpartition('$$EnhancerByCGLIB$$')
                #class_name.rpartition('$$EnhancerByCGLIB$$')[0]
                if class_name.endswith('[]'):
                   class_name =class_name[:-2]
                if class_name in vvm_class:
                    vvm_class[class_name] += line["Live Objects"]
                    vvm_total += float(line["Live Objects"])
                else:
                    vvm_class[class_name] = line["Live Objects"]
                    vvm_total += float(line["Live Objects"])
        csvfile.close()