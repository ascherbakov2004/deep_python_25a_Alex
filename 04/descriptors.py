class CardReader:
    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if obj is None:
            return None
        if not isinstance(value, str) or not value.isdigit() or len(value) != 16:
            raise ValueError("Invalid card number")
        val_splited = " ".join(value[i : i + 4] for i in range(0, len(value), 4))
        return setattr(obj, self.name, val_splited)

    def __set_name__(self, obj, name):
        self.name = f"cardreader_descr_{name}"


class TransactionAmount:
    def __set__(self, obj, value):
        if obj is None:
            return None
        if not isinstance(value, (int, float)):
            raise ValueError(f"{self.name} must be number")
        return setattr(obj, self.name, value)

    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set_name__(self, obj, name):
        self.name = f"transaction_descr_{name}"


class OperationName:
    def __set__(self, obj, value):
        if obj is None:
            return None

        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be string")

        return setattr(obj, self.name, value)

    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set_name__(self, obj, name):
        self.name = f"opername_descr_{name}"