class NucleicAcid():

    def seq_validation(self):
        if self.type == "DNA":
            if not all(base.upper() in ('A', 'C', 'T', 'G')
                       for base in self.seq):
                raise ValueError(f'{self.seq} is wrong sequence. \
                Must be from agct correct letters only')
        else:
            if not all(base.upper() in ('A', 'C', 'U', 'G')
                       for base in self.seq):
                raise ValueError(f'{self.seq} is wrong sequence. \
                Must be from agcu correct letters only')

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i > len(self.seq):
            raise StopIteration
        return self.seq[self.i-1]

#    I believe, this oneliner also valid, but a bit cheaty:
#         yield self.seq

    def __eq__(self, other):
        return (type(other) is type(self)) and self.seq == other.seq

    def gc_content(self):
        if self.seq:
            return sum(1 for letter in self.seq if letter in ['G', 'C']) /\
                len(self.seq)

    def reverse_compliment(self):
        if self.type == "DNA":
            replacement = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
        else:
            replacement = {'U': 'A', 'A': 'U', 'G': 'C', 'C': 'G'}
        return ''.join(replacement[i] for i in self.seq[::-1])


class DNA(NucleicAcid):
    def __init__(self, seq=''):
        self.i = 0
        self.type = "DNA"
        self.seq = seq.upper()
        self.seq_validation()

    def transcribe(self):
        return RNA(self.seq.replace('T', 'U'))


class RNA(NucleicAcid):
    def __init__(self, seq=''):
        self.i = 0
        self.type = "RNA"
        self.seq = seq.upper()
        self.seq_validation()