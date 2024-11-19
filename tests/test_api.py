from fastapi import status


async def test_api(client, app):
    # Тест проверяет работу api
    response = await client.get('/api/users/')
    assert response.status_code == status.HTTP_200_OK 
    assert response.json() == {'status': 'ok', 'data': []}

    response = await client.post(
        '/api/users/',
        json={
            'name': 'test@example.com',
            'fullname': 'Full Name Test',
            }
    )
    assert response.status_code == status.HTTP_201_CREATED
    new_user_id = response.json()['data']['id']

    response = await client.get(f'/api/users/{new_user_id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'status': 'ok',
        'data': {
            'id': new_user_id,
            'name': 'test@example.com',
            'fullname': 'Full Name Test',
        }
    }

    response = await client.get('/api/users/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()['data']) == 1