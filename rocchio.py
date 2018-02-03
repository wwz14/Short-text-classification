__author__ = 'WenzaoWang'
# -*- coding: utf-8 -*-

from numpy import *



# attrs: democratic hillary sanders obama republican trump
# below are counts of the above words

# counts of the attrs words in dnc docs

DNCS =   \
       array([[14,  12,   31,   3,  1,  3],
             [7,   4,    3,    3,  2,  0 ],
             [7,   5,    11,   2,  2,  3],
             [10,  4,    27,   5,  2,  10]])

# counts of the attrs words in trump docs
TRUMPS = \
       array([[1,   0,    0,    0,  20, 28],
             [0,   3,    0,    0,  4,  18],
             [1,   5,    2,    0,  3,  29],
             [0,   1,    3,    1,  2,  11],
             [0,   5,    0,    14, 3,  23]])
# total counts of the attrs words in both dnc documents and trump documents
TOTAL_COUNT = \
       array([40,  39,   77,   28, 39, 125])
# total counts of the attrs words in dnc documents
DNC_COUNT = \
       array([38,  25,   72,   13, 7,  16])
# total counts of the attrs words in trump documents
TRUMP_COUNT= \
       array([2,   14,   5,    15, 32, 109])

n = \
       array([6,    8,   6,     6,  9,  8])

# 3 test data are all TRUMP's report,expect output is that "doc belongs to trump "

TESTS =  \
    array([[[0,   3,    0,    0,  17, 18]],
           [[0,   0,    0,    0,  2,  6]],
           [[0,   0,    0,    0,  10, 21]]])


N = array([9,   9,  9,  9,  9,  9])

# 4 dnc documents
R_DNC = 4
# 5 trumo documents
R_TRUMP = 5


# the process of rocchio algorithm

def cal_v(N, n, total_count, COUNTS):
    w = cal_w(N, n, total_count, COUNTS)

    v = sum(w, 0)/R_DNC

    return v


def cal_w(N, n, total_count, COUNTS):
    tf = 1.0* n/N
    idf = log2(1.0* (COUNTS+1)/total_count)

    multi_result = tf*idf


    dividends = sqrt(sum(pow(multi_result, 2), 1))

    # calculate the w value of each doc vector
    w = divide(multi_result.transpose(), dividends.transpose()).transpose()

    return w


def cal_sim(v1, v2):
    sim = 1.0*sum(v1*v2)/(sqrt(sum(pow(v1, 2)))*sqrt(sum(pow(v2, 2))))
    return sim

if __name__=="__main__":
    v_dnc = cal_v(N, n, TOTAL_COUNT, DNCS)
    v_trump = cal_v(N, n, TOTAL_COUNT, TRUMPS)
    print v_dnc

    print v_trump

    for item in TESTS:
        w_test = cal_w(N, n, TOTAL_COUNT, item)
        sim_dnc = cal_sim(w_test, v_dnc)
        sim_trump = cal_sim(w_test, v_trump)
        if sim_dnc > sim_trump:
            print "doc belongs to dnc",
        else:
            print "doc belongs to trump"

        print "similarities are:"
        print "dnc ", sim_dnc
        print "trump", sim_trump

        print ""
