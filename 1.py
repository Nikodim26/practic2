from datetime import datetime
import json

json_str = '''[
    {
        "name": "Event 1",
        "start_date": "2022-01-01",
        "end_date": "2022-01-05"
    },
    {
        "name": "Event 2",
        "start_date": "2022-02-15",
        "end_date": "2022-02-18"
    },
    {
        "name": "Event 3",
        "start_date": "2022-03-10",
        "end_date": "2022-03-20"
    }
]'''


a = json.loads(json_str)
print(type(a))
d= []
for i in a:

    start = datetime.strptime(i["start_date"], "%Y-%m-%d")
    end = datetime.strptime(i["end_date"], "%Y-%m-%d")
    d.append((end-start).days)

print(d)