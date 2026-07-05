# AI-Powered Smart Glasses for Health Monitoring

## Overview
AI-Powered Smart Glasses for Health Monitoring is an IoT-based wearable system designed to monitor a user's health in real time. The system uses ESP32 and ESP32-CAM to collect physiological and environmental data, estimate stress levels, and perform human/non-human detection using OpenCV. The processed information is displayed on an OLED screen, providing instant feedback while maintaining user privacy through offline processing.

---

## Features
- Real-time heart rate monitoring
- Temperature and pressure monitoring
- Stress level estimation
- Human/Non-Human object detection using OpenCV
- OLED display for real-time results
- Touch-based mode switching
- Low-power wearable design
- Offline processing for enhanced privacy

---

## Hardware Components
- ESP32
- ESP32-CAM
- MAX30102 Heart Rate Sensor
- BME280 Temperature & Pressure Sensor
- OLED Display
- Touch Sensor
- IR Sensor
- Li-ion Battery

---

## Software & Tools
- Arduino IDE
- Embedded C/C++
- Python
- OpenCV
- ThingSpeak
- TensorFlow Lite (TinyML)

---

## Working
1. ESP32 collects data from the MAX30102 and BME280 sensors.
2. Heart rate, temperature, and pressure are measured in real time.
3. Stress level is estimated using sensor data.
4. ESP32-CAM captures live images.
5. OpenCV classifies objects as Human or Non-Human.
6. Results are displayed on the OLED screen.
7. The touch sensor allows users to switch between display modes.

---

## Project Structure

```
AI-Powered-Smart-Glasses/
│── Arduino_Code/
│── OpenCV_Code/
│── Images/
│── Circuit_Diagram/
│── Block_Diagram/
│── Report/
└── README.md
```

---

## Results
- Successfully monitored heart rate, temperature, and pressure.
- Estimated stress levels in real time.
- Detected Human and Non-Human objects using OpenCV.
- Displayed live sensor data on an OLED screen.
- Achieved reliable performance with low power consumption.

---

## Future Enhancements
- Mobile application integration
- Bluetooth/Wi-Fi connectivity
- Advanced AI models for health prediction
- Cloud-based health monitoring
- Additional biomedical sensors

---

## Technologies
`ESP32` `ESP32-CAM` `IoT` `Arduino` `Python` `OpenCV` `ThingSpeak` `Embedded Systems` `Health Monitoring` `Wearable Technology`

---

## Author

**Mahitha B S**

Electronics and Communication Engineering

East Point College of Engineering and Technology

LinkedIn: *(https://www.linkedin.com/in/mahitha-b-s-45a255261)*

GitHub: *(https://github.com/Mahithashiva/)*
