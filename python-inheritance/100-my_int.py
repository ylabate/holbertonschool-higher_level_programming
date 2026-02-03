class MyInt(int):
    def __ne__(self, value: object) -> bool:
        return not super().__ne__(value)

    def __eq__(self, value: object) -> bool:
        return not super().__eq__(value)
