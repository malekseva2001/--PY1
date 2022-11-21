import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(IN) -> list[dict]:
    with open(INPUT_FILE, "r") as f:
        for x in f:
            x.split("\n")
        results = []
        for line in f:
            words = line.split(',')  # get each item in one line
            listOfFloat = map(float, words[1:])  # convert string to float
            tup = (words[0], listOfFloat)
            results.append(zip(dict(tup)))
        kkk = json.dump(results, f, indent=4)
    return kkk
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
