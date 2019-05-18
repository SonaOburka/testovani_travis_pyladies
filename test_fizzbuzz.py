from fizzbuzz import fizzbuzz
import pytest

def test_fb_is_callable_with_1_argument():
    fizzbuzz(1)

def test_fb_returns_str():
    assert isinstance(fizzbuzz(1), str)

@pytest.mark.parametrize('num',[1,2,4])
def test_fb_1_is1(num):
    assert fizzbuzz(1) == '1'

@pytest.mark.parametrize('num',[3,6,9])
def test_fb_three_is_fizz(num):
    assert fizzbuzz(num) == 'fizz'


@pytest.mark.parametrize('num',[5,20,50])
def test_fb_three_is_fizz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15,30,3000])
def test_fb_threefive_is_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'

@pytest.mark.parametrize('num',['',1.5,[],4+3j])
def test_fb_raises_typerror_on_nonint(num):
    with pytest.raises(TypeError):
        fizzbuzz(num)
