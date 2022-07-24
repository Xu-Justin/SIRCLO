from controllers.BeratController import *

def test_validate_tanggal_valid():
    tanggals = [
        '2022-1-1',
        '2022-10-1',
        '2022-1-10',
        '2022-1-31',
    ]
    
    for tanggal in tanggals:
        _, status = validate_tanggal(tanggal)
        assert status == True
        
def test_validate_tanggal_invalid():
    tanggals = [
        '2022-13-1',
        '2022-0-1',
        '2022-1-0',
        '2022-1-32',
        '2022-2-31',
        '1-2-2022',
    ]
    
    for tanggal in tanggals:
        _, status = validate_tanggal(tanggal)
        assert status == False
        
def test_validate_berat_valid():
    berats = [
        0,
        1,
        10,
        12345,
        876575469089767,
        '0',
        '1'
        '12345 ',
        '   12345 ',
    ]
    
    for berat in berats:
        _, status = validate_berat(berat)
        assert status == True
    
def test_validate_berat_invalid():
    berats = [
        -1,
        'abc',
        '',
        '12345o',
    ]
    
    for berat in berats:
        _, status = validate_berat(berat)
        assert status == False
        
def test_validate_form_valid():
    datas = [
        ('2022-1-1', 0, 5),
        ('2022-1-31', 0, 5),
        ('2022-1-1', 0, 0),
        ('2022-12-31', 5, 5),
    ]
    
    for tanggal, berat_min, berat_max in datas:
        _, _, status = validate_form(tanggal, berat_min, berat_max)
        assert status == True
        
def test_validate_form_invalid():
    datas = [
        ('2020-1-1', -1, 5),
        ('2020-1-32', 0, 5),
        ('2020-1-1', 1, 0),
        ('2020-11-31', 5, 5),
    ]
    
    for tanggal, berat_min, berat_max in datas:
        _, _, status = validate_form(tanggal, berat_min, berat_max)
        assert status == False