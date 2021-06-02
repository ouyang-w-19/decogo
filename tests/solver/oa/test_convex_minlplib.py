import csv
import importlib
import os

from decogo.solver.decogo import DecogoSolver


def filter(row):
    """Rule for filtering the problem filter all problems s.t. number of
    blocks != 1 and avg block size !=1 and number blocks != nvars
    """

    def str2bool(s):
        return s in ['True', 'true']

    if str2bool(row['convex']) is False:
        result = False
    else:
        num_blocks = float(row['nlaghessianblocks'])
        avg_block_size = float(row['laghessianavgblocksize'])
        nvars = float(row['nvars'])

        if num_blocks == 1 or num_blocks == nvars or \
                num_blocks == nvars - 1 or avg_block_size == 1:
            result = False
        else:
            result = True

    return result


if __name__ == '__main__':
    # directory where csv data file is located
    dirname = 'tests\\examples\\minlplib_data\\instancedata_updated.csv'

    # infeasible problems
    inf_problems = ['ball_mk4_05', 'ball_mk4_10', 'ball_mk4_15']

    # already executed problems
    problem_executed = []

    # get directory name where csv file is stored
    root_name = os.path.dirname(os.getcwd())
    while True:
        base = os.path.basename(root_name)
        if base == 'decogo':
            break
        else:
            root_name = os.path.dirname(root_name)

    dirname = os.path.join(root_name, dirname)

    problem_names = []

    with open(dirname, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if filter(row):
                problem_names.append(row['name'])
    csvfile.close()

    # exclude problems which were already executed
    for name in problem_executed:
        problem_names.remove(name)

    # exclude infeasible problems
    for name in inf_problems:
        problem_names.remove(name)

    # solver settings
    with open('decogo.set', 'w') as file:
        file.write("maxtime = 5400")
        file.close()

    # run the problems
    for name in problem_names:
        module_obj = \
            importlib.import_module('tests.examples.minlplib.' + str(name))
        input_model = module_obj.model
        input_model.name = name

        solver = DecogoSolver()
        solver.optimize(input_model,
                        file_name='logs\\convex_examples\\' + name + '.txt')

