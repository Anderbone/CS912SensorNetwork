import collections
from sys import argv

def all_msg(file):
    count =0

    for line in file:
        rec = 'Received'
        if rec in line:
            count += 1
    return count


def id_value_finishtime(file):
    id_avg = collections.defaultdict(lambda: 0)
    for line in file:
        if line.startswith('Test') or line.startswith('TEST'):
            continue
        t = line.split(':')
        if t[2].startswith('My avg'):
            id = t[1]

            id_avg[int(id)] = int(t[2].strip().split()[3])
            flag = 1
            if len(id_avg) == 64:

                value = id_avg[1]
                for i in id_avg:
                    if id_avg[i] != value:
                        flag = 0
                        break;
                if flag == 1:
                    for i in sorted(id_avg.keys()):
                        print(i, id_avg[i])

                    return t[0]

    wrong_count = 0
    for i in sorted(id_avg.keys()):

        if id_avg[i] != 28:
            wrong_count += 1
            print(i, id_avg[i])

    print('wrong count')
    print(wrong_count)


def gettime(file):
    with open(file, 'r') as f1:
        next(f1)
        time = id_value_finishtime(f1)
        print(f'latency(time when all motes get correct number): {time}')
        return int(time)

def getmsg(file):
    with open(file, 'r') as f1:
        next(f1)
        msg = all_msg(f1)
        print(f'total number of message during this simulation: {msg}')
        return int(msg)

def getall(file):
    gettime(file)
    getmsg(file)



if __name__ == '__main__':
    getall(argv[1])


