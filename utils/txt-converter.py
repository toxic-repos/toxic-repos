import json

infile = "clean.txt"
outfile = "clean.json"

dict1 = {}
fields = ["datetime", "productname", "url"]
with open(infile, 'r', encoding='utf-8') as fh:
    l = 1

    for line in fh:
        description = list(line.strip().split('\t', 4))

        print(description)

        sno = 'field' + str(l)

        i = 0
        dict2 = {}
        while i < len(fields):
            dict2[fields[i]] = description[i]
            i = i + 1

        dict1[sno] = dict2
        l = l + 1

out_file = open(outfile, 'w', encoding='utf-8')
json.dump(dict1, out_file, indent='\t')
out_file.close()
