# Introduction
In modern communication systems, transferring data from one point to another requires encoding techniques to represent digital information accurately. This project focuses on implementing various encoding schemes: NRZ-L, NRZ-I, Bipolar AMI, Manchester, and Differential Manchester.

# Project overview
This project consists of a Python script capable of encoding input data using different encoding schemes. The Implemented encoding functions ensure the conversion of binary data to corresponding electrical signals, reflecting distinctive voltage patterns characteristics for each scheme.

# Implemented Encoding Schemes
•	NRZ-L: This scheme encodes binary data by maintaining a constant voltage level for each bit, representing '0' as a low voltage level and '1' as a high voltage level.
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/88432700-b082-4cd0-95c4-5ffc7200ec4e)

•	NRZ-I: This scheme encodes data by toggling the voltage level whenever a '1' bit is encountered, while maintaining the voltage level for '0' bits.
 ![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c3f5d222-b10c-438f-b788-eb0094edd93c)

•	Bipolar AMI: In this scheme, '0' bits are represented by zero voltage, while '1' bits are alternately represented by positive and negative voltages, ensuring synchronization and error detection capabilities.
 ![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/ab7aa4ff-0f00-4a7d-addd-a2bc85e9f009)

•	Manchester Encoding: Manchester encoding involves dividing each bit period into two halves and representing '0' bits with a high-to-low voltage transition and '1' bits with a low-to-high transition, ensuring frequent level changes for clock synchronization.
 ![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/49c9fd33-33d5-429a-9d73-47be52291ff9)

•	Differential Manchester Encoding: This scheme ensures synchronization by using transitions in the middle of each bit period. '0' bits are represented by a transition at the beginning of the period, while '1' bits are indicated by no transition at the beginning but a transition in the middle.
 ![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c567ef07-ec51-4935-9327-d569dfd1d9f4)

# Project Execution
NRZ-L:
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/321aa883-3454-49f0-b4d4-3f02b7893d59)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/7e0c4fa3-a260-4b43-9f39-5b17a85ab671)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/7cb14305-285c-4f9d-9927-2d1e2fca3c14)

NRZ-I:
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/1259f0e7-cbe3-4f66-ad55-d65bcd5685c3)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/1189eabf-52ea-460e-a474-c589b5ae33f5)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/88898ca1-f7d7-491b-941d-baa6e7976508)

B-AMI:
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/3e4aa0c0-1ddd-4e48-be85-1c0c028a2e76)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/9316219d-52d2-41ec-a464-c48a6bf12a0d)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/6af21e6b-a5f2-4073-8e06-513af74a5228)

Manchester:
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/d012f118-ca8a-46ff-9c5a-e68e1f49cca2)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/f8665b95-22b4-4685-b514-40279f6322ed)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/cfa91801-bc68-416f-b38d-b9de59c94cd2)

D-Manchester:
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/e1a222e6-8de0-446d-9fd3-bb7d5f0e1d2a)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/24a451da-8177-4fe1-81bb-b0adafe07735)
![image](https://github.com/JuanCantu1/SignalEncodingSchemes/assets/109363196/c8e8e653-56e3-4869-8e9e-c4b7a6472a7d)

# Conclusion
In conclusion, the successful implementation and simulation of various encoding schemes, including NRZ-L, NRZ-I, Bipolar AMI, Manchester, and Differential Manchester, have been achieved in this project. Through Python scripting, each scheme's distinctive characteristics in converting binary data into electrical signals have been demonstrated. This project not only enhances understanding of signal encoding techniques but also lays a foundation for further exploration and application in modern communication systems.
