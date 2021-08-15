from pytest import mark


@mark.principal
def check_passing():
    assert True


@mark.bulk
@mark.xfail(reason="Will fail")
def check_fail():
    assert False


@mark.principal
class FunctionsTests:
    @mark.optional
    def check_optional(self):
        assert True


@mark.bulk
@mark.skip(reason="Some situation")
def check_skip():
    assert False
