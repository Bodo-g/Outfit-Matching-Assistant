"""Transfer learning model definition."""


def build_transfer_model(base_model_name: str = "MobileNetV2"):
    """Build a transfer learning model with a configurable backbone."""
    try:
        from tensorflow.keras import Model
        from tensorflow.keras.applications import MobileNetV2, ResNet50
        from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input
    except ImportError as exc:
        raise ImportError("TensorFlow is required to build the transfer learning model.") from exc

    input_tensor = Input(shape=(224, 224, 3))
    if base_model_name == "ResNet50":
        base_model = ResNet50(include_top=False, weights="imagenet", input_tensor=input_tensor)
    else:
        base_model = MobileNetV2(include_top=False, weights="imagenet", input_tensor=input_tensor)

    base_model.trainable = False
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dense(128, activation="relu")(x)
    output_tensor = Dense(1, activation="sigmoid")(x)
    model = Model(inputs=input_tensor, outputs=output_tensor)
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model
