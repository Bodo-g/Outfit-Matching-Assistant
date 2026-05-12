"""CNN model built from scratch."""


def build_cnn_scratch():
    """Build a simple CNN model."""
    try:
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
    except ImportError as exc:
        raise ImportError("TensorFlow is required to build the scratch CNN model.") from exc

    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model
