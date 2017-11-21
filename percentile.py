'''
Reference implementation of computing percentiles.

Author: Masoud Mansoury
'''

from collections import defaultdict
import os
import os.path

class Percentile:
    def __init__(self):
        self.transformtype = "user" # possible values: user, item
        self.input = "input\\rating.txt"
        self.output = "output\\percentile.txt"
        self.dictionary = {}


    # creating user/item profile, it would be like <userid/itemid, [rate1, rate2, rate3, ...]>
    def create_profile(self):
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                if self.transformtype is "user":
                    per.dictionary.setdefault(data[0].rstrip(), []).append(data[2].rstrip())
                elif self.transformtype is "item":
                    per.dictionary.setdefault(data[1].rstrip(), []).append(data[2].rstrip())

    # percentile computation
    def compute_percentile(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                values = sorted(map(float,list(per.dictionary.get(data[0].rstrip()))))
                # find the index of the last occurrence of repeated numbers e.g., repeated ratings
                position = len(values) - 1 - values[::-1].index(float(data[2].rstrip())) + 1
                # percentile computation
                p = float(100 * position) / float(len(values) + 1)
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(p) + '\n')

        out.close()

    # delete output file if exists
    def delete_outputfile(self):
        try:
            if os.path.exists(self.output):
                os.remove(self.output)
        except OSError:
            print "error"
            pass

if __name__ == '__main__':
    per = Percentile()
    per.create_firstdictionary()
    per.compute_percentile()
