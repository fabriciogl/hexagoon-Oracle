#  Copyright (c) 2021. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.
from config import settings


def test_config_env():
    assert settings.root_user
    assert settings.root_email
    assert settings.root_senha
    assert settings.jwt_hash
    assert settings.jwt_token
