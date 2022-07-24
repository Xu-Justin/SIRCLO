import os
import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app('./test_database.db')
    app.config.update({
        "TESTING": True
    })
    yield app
    os.remove('./test_database.db')
    
    
@pytest.fixture()
def client(app):
    return app.test_client()

##################################################

def get_index(client, status_code):
    response = client.get('/index')
    assert response.status_code == status_code

def get_show(client, tgl, status_code):
    response = client.get(f'/show/{tgl}')
    assert response.status_code == status_code

def get_add(client, status_code):
    response = client.get('/add')
    assert response.status_code == status_code

def add(client, data, status_code, target_path):
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == status_code
    assert response.request.path == target_path

def get_update(client, tgl, status_code):
    response = client.get(f'/update/{tgl}')
    assert response.status_code == status_code

def update(client, tgl, new_data, status_code, target_path):
    response = client.post(f'/update/{tgl}', data=new_data, follow_redirects=True)
    assert response.status_code == status_code
    assert response.request.path == target_path

def delete(client, data, status_code, target_path):
    response = client.post(f'/delete', data=data, follow_redirects=True)
    assert response.status_code == status_code
    assert response.request.path == target_path
    
def create_data(tanggal, berat_min, berat_max):
    return {
        'tanggal' : str(tanggal),
        'berat-min' : str(berat_min),
        'berat-max' : str(berat_max)
    }

##################################################

def test_get_index(client):
    get_index(client, 200)

def test_get_add(client):
    get_add(client, 200)

def test_post_add_1(client):
    data = create_data('2022-12-10', 10, 20)
    add(client, data, 200, '/index')
    
# add data with same tanggal
def test_post_add_2(client):
    data = create_data('2022-12-11', 15, 30)
    add(client, data, 200, '/index')
    
    data = create_data('2022-12-11', 10, 20)
    add(client, data, 200, '/add')
    
# add invalid data
def test_post_add_3(client):
    datas = [
        create_data('2022-13-12', 15, 30),
        create_data('2022-12-12', 30, 15),
        create_data('2022-12-12', '', 30),
        create_data('2022-12-12', 15, '3o'),
        create_data('yyyy-mm-dd', 15, 30),
        create_data('12-13-2022', 15, 30),
    ]
    
    for data in datas:
        add(client, data, 200, '/add')

def test_get_show(client):
    tgl = '2022-10-10'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    get_show(client, tgl, 200)
    
def test_get_update(client):
    tgl = '2022-10-11'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    get_update(client, tgl, 200)

def test_post_update_1(client):
    tgl = '2022-10-12'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    
    new_data = create_data('2022-10-13', 15, 30)
    update(client, tgl, new_data, 200, '/index')

# update data with new_data have same tanggal
def test_post_update_2(client):
    tgl = '2022-10-14'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    
    new_data = create_data(tgl, 15, 30)
    update(client, tgl, new_data, 200, '/index')

# update data with invalid new_data
def test_post_update_3(client):
    tgl = '2022-10-15'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    
    new_datas = [
        create_data('2022-13-16', 15, 30),
        create_data('2022-10-16', 30, 15),
        create_data('2022-10-16', '', 30),
        create_data('2022-10-16', 15, '3o'),
        create_data('yyyy-mm-dd', 15, 30),
        create_data('16-10-2022', 15, 30),
    ]
    
    for new_data in new_datas:
        update(client, tgl, new_data, 200, f'/update/{tgl}')

# update data with new_data tanggal already exists
def test_post_update_4(client):
    tgl_1 = '2022-10-20'
    data = create_data(tgl_1, 10, 20)
    add(client, data, 200, '/index')
    
    tgl_2 = '2022-10-21'
    data = create_data(tgl_2, 10, 20)
    add(client, data, 200, '/index')
    
    new_data = create_data(tgl_2, 15, 30)
    update(client, tgl_1, new_data, 200, f'/update/{tgl_1}')

def test_post_delete(client):
    tgl = '2022-11-1'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    delete(client, data, 200, '/index')
    
def test_mix_1(client):
    tgl_1 = '2022-10-30'
    data = create_data(tgl_1, 10, 20)
    add(client, data, 200, '/index')
    get_show(client, tgl_1, 200)
    get_update(client, tgl_1, 200)
    
    tgl_2 = '2022-10-31'
    new_data = create_data(tgl_2, 15, 30)
    update(client, tgl_1, new_data, 200, '/index')
    get_show(client, tgl_1, 404)
    get_update(client, tgl_1, 404)
    get_show(client, tgl_2, 200)
    get_update(client, tgl_2, 200)
    
def test_mix_2(client):
    tgl = '2022-12-20'
    data = create_data(tgl, 10, 20)
    add(client, data, 200, '/index')
    delete(client, data, 200, '/index')
    
    update(client, tgl, data, 404, f'/update/{tgl}')
    delete(client, data, 404, '/delete')