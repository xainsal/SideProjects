import os
import zipfile

os.mkdir("zips")
td = input("Enter the directory Path: ")
cd = os.getcwd()
entries = os.listdir(td)
print(entries)
for x in entries:
    if x == "main.py":
        continue
    else:
        os.chdir(td + "//" + x)
        print(x)
        file = os.listdir()
        print(file)
        with zipfile.ZipFile(cd + "//" + "zips//" + x + '.zip', 'w') as new_zip:
            for name in file:
                new_zip.write(name)

