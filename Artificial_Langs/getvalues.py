import sys

def main(parameters):
    with open(parameters, 'r') as f:
        pars = f.readlines()
        split_data = []
        for par in pars:
            split_data.append([line.split() for line in par.split(",")])
        return split_data


def get_mean(par):
    ratio = []
    for taxa in par:
        plus = 0.0
        minus = 0.0
        for value in taxa:
            if value == '+':
                plus = plus + 1
            elif value == '-':
                minus = minus + 1
        if plus + minus > 0:
            ratio.append(plus / (plus + minus))
    if len(ratio) > 0:
        ratio_sum = sum(ratio) / len(ratio)
    else:
        ratio_sum = 0.5
    return ratio_sum


def overall_mean(data):
    par_values = []
    for par in data:
        par_values.append(round(get_mean(par), 3))
    return par_values


if __name__ == "__main__":
    data = main(sys.argv[1])
    print(overall_mean(data))
