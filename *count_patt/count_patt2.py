import re

class Count():
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        dcit = {}
        patt1 = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = patt1.search(line)
                if m:
                    key = m.group()
                    dcit[key] = dcit.get(key, 0) + 1
                    # if key not in dcit:
                    #     dcit[key] = 1
                    # else:
                    #     dcit[key] += 1

        return dcit

if __name__ == '__main__':
    logfile = 'access_log'
    ip = '^(\d+\.){3}\d+'
    IP = Count(logfile)
    print(IP.count_patt(ip))