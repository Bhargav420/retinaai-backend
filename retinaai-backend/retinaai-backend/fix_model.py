import tensorflow as tf

print("Loading original model...")

model = tf.keras.models.load_model(
    "services/best_retina_model.keras",
    compile=False,
    safe_mode=False
)

print("Model loaded")

# rebuild model cleanly
clean_model = tf.keras.models.clone_model(model)
clean_model.set_weights(model.get_weights())

print("Saving fixed model...")

clean_model.save("services/best_retina_model_fixed.keras")

print("Done. Model repaired.")