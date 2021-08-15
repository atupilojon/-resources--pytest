from pytest import mark

# if setup.py present, code could be installed as library
# so that there's no need include path
# pip install -e .
from pytest_resources import do_lower_case
# from src.for_testing import do_lower_case


@mark.coverage
def check_lower_case():
    assert do_lower_case('SomeThing') == 'something'
