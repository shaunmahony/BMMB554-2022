import sys

def parse_fasta(fh):
    fa = {}
    current_short_name = None
    # Part 1: compile list of lines per sequence
    for ln in fh:
        if ln[0] == '>':
            # new name line; remember current sequence's short name
            long_name = ln[1:].rstrip()
            current_short_name = long_name.split()[0]
            fa[current_short_name] = []
        else:
            # append nucleotides to current sequence
            fa[current_short_name].append(ln.rstrip())
    # Part 2: join lists into strings
    for short_name, nuc_list in fa.items():
        # join this sequence's lines into one long string
        fa[short_name] = ''.join(nuc_list)
    return fa

if len(sys.argv) >= 2 :
    f=1
    while f < len(sys.argv):
        file = sys.argv[f]
        with open(file, 'r') as seq_file :
            fa = parse_fasta(seq_file)
            for i in fa.keys() :
                print("Sequence {} is {}bp long".format(i, len(fa[i])))
        f+=1
else :
    print("No FASTA file provided")

