from __future__ import print_function
from config import *
import gensim.models

def load_models(mode=None, emb_type=None):

    if emb_type == "vec": binary = False
    elif emb_type == "bin": binary = True
    else: raise Exception()

    print('\n\n**** Model:', mode, " binary:", binary)

    if mode == "doc2vec":  
        word_model = gensim.models.doc2vec.Doc2Vec.load(MODEL_PATH + mode + ".model")
    else:
        word_model = gensim.models.KeyedVectors.load_word2vec_format(MODEL_PATH + mode + ".model", binary=binary)
        #word_model = gensim.models.Word2Vec.load_word2vec_format(MODEL_PATH + mode + ".model", binary=binary)   

    word_model.init_sims(replace=True) # clean up RAM

    # not used currently!
    bigram_model = None

    print("**** Model:", mode, " LOADED\n\n")
   
    return word_model, bigram_model 

def print_details(task_res, msg):
    print("\n" + msg)
    for res in task_res:
        print("Task: %s -- Found: %s -- Correct: %s\n" % (res[0], res[1], res[2]))

def print_latex_version(results, method, FILTER_SECTIONS):
    """
        create a latex version of the results dictionary 
        --> for easy updates of publication data
    """
    vals, counts = [],[]
    for sec in FILTER_SECTIONS:
        data = results[sec]

        vals.append(str(round(data['perc']*100, 2)))
        counts.append(str(data['counts']))

    print('Number of tasks:       &', " & ".join(counts) , " \\\\ \hline ")
    print(method, "               & ", " & ".join(vals) , " \\\\ ")


if __name__ == "__main__":
    model, crap = load_models(mode='asoif_w2v-default', emb_type='bin')
    print('\n\nMODEL', model)
 
