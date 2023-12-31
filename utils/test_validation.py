from utils import validation


def test_apto_number_is_ok():
    assert validation.apt("001") is True
    assert validation.apt("304") is True
    assert validation.apt("203") is True
    assert validation.apt("314") is False
    assert validation.apt("32") is False
    assert validation.apt("000") is False
    assert validation.apt("100") is False
    assert validation.apt("501") is False
    assert validation.apt("0402") is False


# def test_placa_format_is_ok():
#     # Padrão
#     assert validation.placa("jvm5602") is True
#     assert validation.placa("JDK9874") is True
#     assert validation.placa("JdK8710") is True
#     assert validation.placa("Jvm403p") is False
#     assert validation.placa(" JDK9874") is False
#     assert validation.placa("JDK 9874") is False
#     assert validation.placa("iot1090 ") is False
#     # Mercosul
#     assert validation.placa("pip1l45") is True
#     assert validation.placa("PiP2L45") is True
#     assert validation.placa("pip3790") is True


def test_name_is_ok():
    assert validation.name(['Pedro', 'Fernando', 'Silva']) is True
    assert validation.name(['Àlex', 'João', 'Otávio']) is True
    assert validation.name(['Pedro_Fernando']) is False
    assert validation.name(['João08301']) is False
    assert validation.name(['Ana', '', 'Costa']) is False
