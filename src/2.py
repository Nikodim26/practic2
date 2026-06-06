import json
import os


def dsdsfds(city):
    a_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(a_path + '\\in.json') as file:
        b = json.load(file)[city]
        tt = []
        for c, t in b.items():
            tt.append(t)

        a = {}
        a[city] = {"Average temperature": round((sum(tt) / len(tt)), 2)}
        with open(a_path + '\\out.json', 'w') as file:
            json.dump(a, file,indent=4)
        return a


if __name__ == '__main__':
    print(dsdsfds('Moscow'))
