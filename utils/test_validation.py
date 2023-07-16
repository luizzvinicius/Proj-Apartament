from utils import validation


def test_cpf_format_is_ok():
    assert validation.cpf("9192938290") is False  # 10 numbers
    assert validation.cpf("919293829078") is False  # 12 numbers
    assert validation.cpf("-1897548949") is False
    assert validation.cpf("718.975.489.49") is False
    assert validation.cpf(" 718.975.489.49 ") is False
    assert validation.cpf("718.975.489 49") is False
    assert validation.cpf("718.975.489-49") is True

def test_apto_number_is_ok():
    pass


def test_placa_format_is_ok():
    # Padrão
    assert validation.placa("jvm5602") is True
    assert validation.placa("JDK9874") is True
    assert validation.placa("JdK8710") is True
    assert validation.placa("Jvm403p") is False
    assert validation.placa(" JDK9874") is False
    assert validation.placa("JDK 9874") is False
    assert validation.placa("iot1090 ") is False
    # Mercosul
    assert validation.placa("pip1l45") is True
    assert validation.placa("PiP2L45") is True
    assert validation.placa("pip3790") is True


def test_name_is_ok():
    assert validation.name(['Pedro', 'Fernando', 'Silva']) is True
    assert validation.name(['Àlex', 'João', 'Otávio']) is True
    assert validation.name(['Pedro_Fernando']) is False
    assert validation.name(['João08301']) is False
    assert validation.name(['Ana', '', 'Costa']) is False
