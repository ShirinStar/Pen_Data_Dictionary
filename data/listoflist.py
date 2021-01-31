import json
import random
import pickle
from itertools import chain, combinations, permutations

def gen_subsets(rel):
  sets = set()
  if len(rel) > 100:
    return sets
  print("length of relationships: " + str(len(rel)))
  for i in range(2, 5):
    bucket = set(combinations(rel, i))
    sets = sets.union(bucket)
    print("set lengths: " + str(len(sets)))

  return sets

def build_counts(): 
  f = open("/Users/shirin/other_projects/cooper_hewitt/Pen_Data_Dictionary/Pen_Data_Dictionary/data/visitsItems_listevening.txt", "r")
  data = json.loads(f.read())
  relation_counts = {}
  ctr = 0
  vi_length = len(data)
  for visit_items in data:
    ctr += 1
    print("on visit item: #" + str(ctr) + " out of total items: #" + str(vi_length))
    subsets = gen_subsets(visit_items)

    print("total subsets length: " + str(len(subsets)))
    for rel in subsets:
      relation_counts[rel] = relation_counts.get(rel, 0) + 1


  import pdb; pdb.set_trace()

  print("before filter")
  relation_counts = dict(filter(lambda elem: elem[1] > 1, relation_counts.items()))
  print("before sorting")
  answer = dict(sorted(relation_counts.items(), key=lambda item: item[1]))
  print("before pickling")
  f = open("/Users/shirin/other_projects/cooper_hewitt/Pen_Data_Dictionary/relation_counts_eveningTime.json", "wb")
  pickle.dump(answer, f)
  f.close()
  import pdb; pdb.set_trace()


def get_counts():
  f = open("/Users/shirin/relation_counts.json", "rb")
  data = pickle.load(f)
  f.close()

build_counts()