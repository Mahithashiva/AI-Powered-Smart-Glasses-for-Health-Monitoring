import tensorflow as tf
import numpy as np

# Load TensorFlow Lite Model
MODEL_PATH = "tinyml_glasses_model.tflite"

interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_vitals(heart_rate, spo2):
    """
    Predict health condition using Heart Rate and SpO2 values.
    """

    # Create input window (50 samples)
    input_data = np.array(
        [[[heart_rate, spo2]] * 50],
        dtype=np.float32
    )

    # Set model input
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get prediction
    prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]

    if prediction > 0.5:
        return "ANOMALY DETECTED", prediction
    else:
        return "NORMAL CONDITION", prediction


# Example
if __name__ == "__main__":

    heart_rate = 82
    spo2 = 98

    result, confidence = predict_vitals(heart_rate, spo2)

    print("--------------------------------")
    print("AI Smart Glasses Health Analysis")
    print("--------------------------------")
    print(f"Heart Rate : {heart_rate} BPM")
    print(f"SpO₂ : {spo2}%")
    print(f"Prediction : {result}")
    print(f"Confidence : {confidence:.2f}")


