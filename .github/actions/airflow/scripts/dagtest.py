import sys
from airflow.models import DagBag

def test(*args):
    print("Passed arguments")
    print(args)
    bag = DagBag(dag_folder=args[1], include_examples=False)
    
    if bag.import_errors:
        raise ValueError(bag.import_errors)

    if bag.import_errors or not bag.dags:
        raise ValueError(bag.dags)


if __name__ == "__main__":
    test(*sys.argv)