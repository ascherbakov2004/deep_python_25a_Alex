class SomeModel:
    def predict(self, message: str) -> float:
        return 0.9


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    model = SomeModel()

    result = model.predict(message)
    if result < bad_thresholds:
        return "неуд"
    elif result > good_thresholds:
        return "отл"
    else:
        return "норм"
