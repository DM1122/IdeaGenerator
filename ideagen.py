import os
import random


def loadData():
    if not os.path.isdir('data'):
        print('No database found. Creating one now...')
        os.mkdir('data')
    
    if not os.listdir('data'):
        input('Please import data. Press any key to continue...')

    #region constructing dictionary
    data = dict()
    for filename in os.listdir('data'):
        name = os.path.splitext(filename)[0]
        with open('data/'+filename, 'r') as f:
            text = f.read()
            data[name] = text.split('\n')
    
    keys = list(data.keys())
    #endregion

    return data
    


def generate(data):
    desc1 = random.choice(data['descriptors'])
    typ = random.choice(data['types'])
    desc2 = random.choice(data['descriptors'])
    sub = random.choice(data['subjects'])
    act = random.choice(data['actions'])
    obj = random.choice(data['objects'])
    
    if desc1[0] in 'aeiou':
        det = 'An'
    else:
        det = 'A'

    # {A, An} {descriptor} {type} about {descriptor2} {subject} {action} {object}
    idea = '{} {} {} about {} {} {} {}'.format(det, desc1, typ, desc2, sub, act, obj)

    return idea


if __name__ == '__main__':
    data = loadData()

    while True:
        output = generate(data)
        print(output)
        input()
        


