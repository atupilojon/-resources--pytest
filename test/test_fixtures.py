from pytest import mark


@mark.web
def check_fixture_web_eldetape(firefox_browser):
    firefox_browser.get('https://www.eldestapeweb.com/')
    assert True


@mark.web
def check_fixture_web_minutouno(firefox_browser):
    firefox_browser.get('https://www.minutouno.com/')
    assert True
