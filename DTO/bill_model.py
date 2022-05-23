from dataclasses import dataclass


@dataclass
class BillModel:
    __name: str
    __balance: str
    __category: str
    __bank_name: str
    __BIK: str
    __invoice_number: str
    __to: str

    def __init__(
        self,
        name: str = "",
        balance: str = "",
        category: str = "",
        bank_name: str = "",
        BIK: str = "",
        invoice_number: str = "",
        to: str = "",
    ):
        self.__name = name
        self.__balance = balance
        self.__category = category
        self.__bank_name = bank_name
        self.__BIK = BIK
        self.__invoice_number = invoice_number
        self.__to = to

    @property
    def name(self) -> str:
        return self.__name

    @property
    def balance(self) -> str:
        return self.__balance

    @property
    def category(self) -> str:
        return self.__category

    @property
    def bank_name(self) -> str:
        return self.__bank_name

    @property
    def BIK(self) -> str:
        return self.__BIK

    @property
    def invoice_number(self) -> str:
        return self.__invoice_number

    @property
    def to(self) -> str:
        return self.__to
