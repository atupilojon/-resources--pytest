from pytest import mark


@mark.arguments
def check_passing_data(data):
    assert data == 'argparse_test'
