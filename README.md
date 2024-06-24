# Introduction
In modern communication systems, encoding techniques are crucial for accurately representing digital information during data transfer. This project focuses on implementing various encoding schemes: NRZ-L, NRZ-I, Bipolar AMI, Manchester, and Differential Manchester.

# Project Overview
This project features a Python script that encodes input data using different schemes. The implemented functions convert binary data into corresponding electrical signals, each with distinctive voltage patterns characteristic of the respective encoding scheme.

# Implemented Encoding Schemes
### NRZ-L (Non-Return to Zero-Level)
- Encodes binary data by maintaining a constant voltage level for each bit.
- '0' is represented by a low voltage level and '1' by a high voltage level.
![NRZ-L](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/88432700-b082-4cd0-95c4-5ffc7200ec4e)

### NRZ-I (Non-Return to Zero-Inverted)
- Toggles the voltage level whenever a '1' bit is encountered.
- Maintains the current voltage level for '0' bits.
![NRZ-I](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c3f5d222-b10c-438f-b788-eb0094edd93c)

### Bipolar AMI (Alternate Mark Inversion)
- '0' bits are represented by zero voltage.
- '1' bits are alternately represented by positive and negative voltages, aiding synchronization and error detection.
![Bipolar AMI](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/ab7aa4ff-0f00-4a7d-addd-a2bc85e9f009)

### Manchester Encoding
- Divides each bit period into two halves.
- '0' bits have a high-to-low voltage transition.
- '1' bits have a low-to-high voltage transition, ensuring frequent level changes for clock synchronization.
![Manchester](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/49c9fd33-33d5-429a-9d73-47be52291ff9)

### Differential Manchester Encoding
- Ensures synchronization with transitions in the middle of each bit period.
- '0' bits are represented by a transition at the beginning of the period.
- '1' bits have no transition at the beginning but a transition in the middle.
![Differential Manchester](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c567ef07-ec51-4935-9327-d569dfd1d9f4)

# Project Execution
### NRZ-L
![NRZ-L Execution](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/321aa883-3454-49f0-b4d4-3f02b7893d59)
![NRZ-L Example 2](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/7e0c4fa3-a260-4b43-9f39-5b17a85ab671)
![NRZ-L Example 3](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/7cb14305-285c-4f9d-9927-2d1e2fca3c14)

### NRZ-I
![NRZ-I Execution](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/1259f0e7-cbe3-4f66-ad55-d65bcd5685c3)
![NRZ-I Example 2](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/1189eabf-52ea-460e-a474-c589b5ae33f5)
![NRZ-I Example 3](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/88898ca1-f7d7-491b-941d-baa6e7976508)

### Bipolar AMI
![Bipolar AMI Execution](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/3e4aa0c0-1ddd-4e48-be85-1c0c028a2e76)
![Bipolar AMI Example 2](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/9316219d-52d2-41ec-a464-c48a6bf12a0d)
![Bipolar AMI Example 3](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/6af21e6b-a5f2-4073-8e06-513af74a5228)

### Manchester
![Manchester Execution](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/d012f118-ca8a-46ff-9c5a-e68e1f49cca2)
![Manchester Example 2](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/f8665b95-22b4-4685-b514-40279f6322ed)
![Manchester Example 3](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/cfa91801-bc68-416f-b38d-b9de59c94cd2)

### Differential Manchester
![Differential Manchester Execution](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/e1a222e6-8de0-446d-9fd3-bb7d5f0e1d2a)
![Differential Manchester Example 2](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/24a451da-8177-4fe1-81bb-b0adafe07735)
![Differential Manchester Example 3](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c8e8e653-56e3-4869-8e9e-c4b7a6472a7d)

# Conclusion
The project successfully implements and simulates various encoding schemes: NRZ-L, NRZ-I, Bipolar AMI, Manchester, and Differential Manchester. Using Python, the distinctive characteristics of each scheme in converting binary data into electrical signals are demonstrated. This project enhances the understanding of signal encoding techniques and lays a foundation for further exploration in modern communication systems.
