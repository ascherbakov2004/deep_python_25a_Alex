class CustomMeta(type):
    def __new__(cls, clsname, bases, attrs):
        new_attrs = {cls._process_word(key): value for key, value in attrs.items()}

        new_attrs["__setattr__"] = cls.__setattr__
        return super().__new__(cls, clsname, bases, new_attrs)

    @staticmethod
    def _process_word(key):
        word_to_insert = "custom_"
        if (
            key.startswith(f"{word_to_insert}")
            or key.startswith(f"_{word_to_insert}")
            or (key.startswith("__") and key.endswith("__"))
        ):
            return key

        if key.startswith("_"):
            return f"_{word_to_insert}" + key[1:]

        return f"{word_to_insert}" + key

    def __setattr__(self, name, value):
        super(self.__class__, self).__setattr__(CustomMeta._process_word(name), value)