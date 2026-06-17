import pytest 

import json

from django.urls import reverse


@pytest.mark.django_db
def test_estoque_view(client):

    url = reverse('estoque-home')
    response = client.get(url)
    assert response.status_code == 200
    
    response_content = response.content 
    assert response_content == b'Estoque funcionando'

