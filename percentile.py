'''
Reference implementation of computing percentiles.

Author: Masoud Mansoury
'''

from collections import defaultdict
import os
import os.path
import math

class Percentile:
    def __init__(self):
        # self.fold = 1

        self.transformation_type = "user" # possible values: user and item
        self.percentile_position = "first" # possible values: first, floormedian, ceilmedian, last, and zscore
        self.percentile_smoothed = True # possible values: True and False
        self.percentile_smoothedparam = 5 # a paramter related to smoothing. It's an integer value and will be applied when self.smoothed is True
        self.input = "input\\rating.txt"
        self.output = "output\\percentile.txt"
        self.dictionary = {}
        self.rating_scale = []

    # creating user/item profile, it would be like <userid/itemid, [rate1, rate2, rate3, ...]>
    def create_profile(self):
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                if self.transformation_type is "user":
                    per.dictionary.setdefault(data[0].rstrip(), []).append(data[2].rstrip())
                elif self.transformation_type is "item":
                    per.dictionary.setdefault(data[1].rstrip(), []).append(data[2].rstrip())

    # percentile computation for first index
    def compute_firstindex_percentile(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                i = 0
                if self.transformation_type is "item":
                    i = 1
                values = sorted(map(float,list(per.dictionary.get(data[i].rstrip()))))
                # find the index of the first occurrence of repeated numbers e.g., repeated ratings
                position = values.index(float(data[2].rstrip())) + 1
                # percentile computation
                p = 0.0
                if(self.percentile_smoothed):
                    p = 100 * float(position + ((self.getRatePosition(float(data[2].rstrip())) -1 ) * self.percentile_smoothedparam)) / (len(values) + 1 + (len(self.rating_scale) * self.percentile_smoothedparam))
                else:
                    p = float(100 * position) / float(len(values) + 1)
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(p) + '\n')

        out.close()

    # percentile computation for floor median index
    def compute_floormedianindex_percentile(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                i = 0
                if self.transformation_type is "item":
                    i = 1
                values = sorted(map(float,list(per.dictionary.get(data[i].rstrip()))))
                # find the index of the floor median occurrence of repeated numbers e.g., repeated ratings
                last = len(values) - 1 - values[::-1].index(float(data[2].rstrip())) + 1
                first = values.index(float(data[2].rstrip())) + 1
                position = int(math.floor(float(last+first))/2)
                # percentile computation
                p = 0.0
                if(self.percentile_smoothed):
                    p = 100 * float(position + ((self.getRatePosition(float(data[2].rstrip()))-1) * self.percentile_smoothedparam) + (int(math.floor(float(self.percentile_smoothedparam/2))))) / (len(values) + 1 + (len(self.rating_scale) * self.percentile_smoothedparam))
                else:
                    p = float(100 * position) / float(len(values) + 1)
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(p) + '\n')

        out.close()

    # percentile computation for ceil median index
    def compute_ceilmedianindex_percentile(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                i = 0
                if self.transformation_type is "item":
                    i = 1
                values = sorted(map(float,list(per.dictionary.get(data[i].rstrip()))))
                # find the index of the ceil median occurrence of repeated numbers e.g., repeated ratings
                last = len(values) - 1 - values[::-1].index(float(data[2].rstrip())) + 2
                first = values.index(float(data[2].rstrip())) + 1
                position = int(math.ceil(float(last+first))/2)
                # percentile computation
                p = 0.0
                if(self.percentile_smoothed):
                    p = 100 * float(position + ((self.getRatePosition(float(data[2].rstrip()))-1) * self.percentile_smoothedparam) + (int(math.ceil(float(self.percentile_smoothedparam/2))))) / (len(values) + 1 + (len(self.rating_scale) * self.percentile_smoothedparam))
                else:
                    p = float(100 * position) / float(len(values) + 1)
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(p) + '\n')

        out.close()

    # percentile computation for last index
    def compute_lastindex_percentile(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                i = 0
                if self.transformation_type is "item":
                    i = 1
                values = sorted(map(float,list(per.dictionary.get(data[i].rstrip()))))
                # find the index of the last occurrence of repeated numbers e.g., repeated ratings
                position = len(values) - 1 - values[::-1].index(float(data[2].rstrip())) + 1
                # percentile computation
                p = 0.0
                if(self.percentile_smoothed):
                    p = 100 * float(position + (self.getRatePosition(float(data[2].rstrip())) * self.percentile_smoothedparam)) / (len(values) + 1 + (len(self.rating_scale) * self.percentile_smoothedparam))
                else:
                    p = float(100 * position) / float(len(values) + 1)
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(p) + '\n')

        out.close()

    def compute_zscore(self):
        self.delete_outputfile()
        out = open(self.output,"w")
        with open(self.input) as f:
            for line in f:
                data = line.split("\t")
                # sorting the values correspoding to the key e.g., ratings
                i = 0
                if self.transformation_type is "item":
                    i = 1
                values = sorted(map(float,list(per.dictionary.get(data[i].rstrip()))))
                # compute mean of rating profile
                mean = float(sum(values)) / max(len(values),1)
                # compute standard deviation of rating profile
                nominator = 0.0
                for j in range(len(values)):
                    nominator += math.pow(float(values[j]-mean),2)
                std = math.sqrt(nominator/float(len(values)))
                # zscore computation
                z = 0.0
                if(std != 0.0):
                    z = float(float(data[2].rstrip())-mean)/std
                out.write(data[0].rstrip() + '\t' + data[1].rstrip() + '\t' + str(z) + '\n')

        out.close()

    def transform(self):
        if(self.percentile_position is "first"):
            self.compute_firstindex_percentile()
        elif (self.percentile_position is "floormedian"):
            self.compute_floormedianindex_percentile()
        elif (self.percentile_position is "ceilmedian"):
            self.compute_ceilmedianindex_percentile()
        elif (self.percentile_position is "last"):
            self.compute_lastindex_percentile()
        elif (self.percentile_position is "zscore"):
            self.compute_zscore()

    # delete output file if exists
    def delete_outputfile(self):
        try:
            if os.path.exists(self.output):
                os.remove(self.output)
        except OSError:
            print("error")
            pass

    def getRatePosition(self, rate):
        for i in range(len(self.rating_scale)):
            if rate == self.rating_scale[i]:
                return i + 1
        return 0

    def create_ratingscale(self):
        with open(self.input) as f:
            for line in f:
                rate = line.split("\t")[2]
                if(float(rate) not in self.rating_scale):
                    self.rating_scale.append(float(rate))
        self.rating_scale.sort()


if __name__ == '__main__':
    per = Percentile()
    per.create_ratingscale()
    per.create_profile()
    per.transform()
