import argparse


def get_line(file):
    list_all = []
    with open(file, 'r') as f1:
            con = f1.readlines()
            for line in con:
                line = line.strip()
                if line[0] != '#':
                    list_all.append(line)
    return list_all

def AddHeader(file1, file2):
    with open(file1, 'r') as fr:
        with open(file2, 'w') as fw:
            con = fr.readlines()
            for line in con:
                line = line.strip()
                if i[0] == "#":
                    fw.write(line + '\n')

def FirstDeal():
    first_deal = []
    for x in samtool:
        for y in gatk:
            if x.split('\t')[0] == y.split('\t')[0] and x.split('\t')[1] == y.split('\t')[1]:
                if y.split('\t')[7].split(';')[3].split('=')[0] == 'DP' \
                    and 5 <= int(y.split('\t')[7].split(';')[3].split('=')[1]) <= 100:
                    first_deal.append(y)
    return first_deal

def SecondDeal(List):
    for i in range(len(List)-1):
        if int(List[i+1].split('\t')[1]) - int(List[i].split('\t')[1]) <= 5:
            List.remove(List[i+1])

def AddResult(file):
    with open(file, 'a+') as f:
        for i in first_deal:
            f.write(i + '\n')

def main():
    parser = argparse.ArgumentParser(description="For example: python filter_snp.py -i1 sample.sample.samtools.raw.vcf -i2 sample.gatk.raw.vcf -o gatk_filter.vcf")
    parser.add_argument("-i1", "--input1", metavar='', type=str, required=True, help="sample.samtools.raw.vcf")
    parser.add_argument("-i2", "--input2", metavar='', type=str, required=True, help="sample.gatk.raw.vcf")
    parser.add_argument("-o", "--output", metavar='', type=str, required=True, help="gatk_filter.vcf")
    args = parser.parse_args()
    
    samtool = get_line(args.input1)
    gatk = get_line(args.input2)
    AddHeader(args.input2, args.output)
    firstdeal = FirstDeal()
    SecondDeal(firstdeal)
    AddResult(args.output)

if __name__ == "__main__":
    main()