class SomeModel:
    def predict(self, message: str) -> float:
        pass


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:

    if not (
        isinstance(bad_thresholds, (float, int))
        and isinstance(good_thresholds, (float, int))
    ):
        return None

    if not isinstance(message, str):
        return None

    if good_thresholds < bad_thresholds:
        return None

    prediction = model.predict(message)
    if prediction > good_thresholds:
        return "отл"
    if prediction < bad_thresholds:
        return "неуд"

    return "норм"