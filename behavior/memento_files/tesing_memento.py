
import pickle
import json
import shelve

if __name__=='__main__':
    dict = {'a':1, 'b':2}
    l = [1,2,3,4]
    # with open('d','wb') as f:
    #     pickle.dump(dict,f)
    #     pickle.dump(l,f)
    #     f.close()
    # with open('d','rb') as f:
    #     e = pickle.load(f)
    #     print(e)
    #     e1 = pickle.load(f)
    #     print(e1)
    #     f.close()
    # with open('o','wb') as f:
    #     p = pickle.Pickler(file=f)
    #     p.dump(dict)
    #     p.dump(l)
    #     f.close()
    # with open('o', 'rb') as f:
    #     up = pickle.Unpickler(file=f)
    #     print(up.load())
    #     f.close()

    # with open('j','w') as f:
    #     # json.dump(dict,f)
    #     json.dump(l,f)
    #     f.close()
    # with open('j', 'r') as f:
    #     p = json.load(f)
    #     print(p)

    with shelve.open('spam') as db:
        db['eggs'] = 'eggs receipt'
        db['ouch'] = dict
        db.close()
    with shelve.open('spam') as db:
        print(db['eggs'])
        print(db['ouch'])
        db['ouch'] = 'new ouch'
        print(db['ouch'])
        db.close()

