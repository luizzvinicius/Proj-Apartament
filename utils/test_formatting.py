from datetime import date
from utils import formatting


def test_cpf_formatting_is_ok():
    assert formatting.cpf("78932145874") == "789.321.458-74"


def test_phone_formatting_is_ok():
    assert formatting.phone_number("82988763014") == "(82) 98876-3014"


def test_date_formatting_is_ok():
    assert formatting.date(date(2023,6,9)) == "09/06/2023"


def test_split_num_apt_is_ok():
    assert formatting.split_num_apt("29001") == "Bloco 29 Número 001"
