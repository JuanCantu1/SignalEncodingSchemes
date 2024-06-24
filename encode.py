import sys

# Function to encode data using NRZ-L encoding scheme
def encode_NRZ_L(data):
    encoded_signal = ""
    for bit in data:
        if bit == '0':
            encoded_signal += '|-V'
        else:
            encoded_signal += '|+V'
    return encoded_signal + '|'

# Function to encode data using NRZ-I encoding scheme
def encode_NRZ_I(data):
    encoded_signal = ""
    prev_voltage = '-V'
    for bit in data:
        if bit == '0':
            encoded_signal += '|' + prev_voltage
        else:
            prev_voltage = '-V' if prev_voltage == '+V' else '+V'
            encoded_signal += '|' + prev_voltage
    return encoded_signal + '|'

# Function to encode data using Bipolar AMI encoding scheme
def encode_Bipolar_AMI(data):
    encoded_signal = ""
    voltage = '+V'
    for bit in data:
        if bit == '0':
            encoded_signal += '|0V'
        else:
            encoded_signal += '|' + voltage
            voltage = '-V' if voltage == '+V' else '+V'
    return encoded_signal + '|'

# Function to encode data using Manchester encoding scheme
def encode_Manchester(data):
    encoded_signal = ""
    for bit in data:
        if bit == '0':
            encoded_signal += '|+V|-V'
        else:
            encoded_signal += '|-V|+V'
    return encoded_signal

# Function to encode data using Differential Manchester encoding scheme
def encode_Differential_Manchester(data):
  encoded_signal = ""
  prev_state = '+V'
  for bit in data:
    if bit == '0':
      encoded_signal += prev_state + '|' 
      prev_state = '-V' if prev_state == '+V' else '+V'
    else:
      encoded_signal += '|' + prev_state  
  return encoded_signal

# Main function
def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python encode.py <input_file> <encoding_scheme_code>")
        return
    
    # Get the input file name and encoding scheme code from command-line arguments
    input_file = sys.argv[1]
    encoding_scheme_code = int(sys.argv[2])

    # Read the data from the input file
    with open(input_file, 'r') as file:
        data = file.read().strip()

    # Encode the data using the specified encoding scheme
    if encoding_scheme_code == 0:
        encoded_signal = encode_NRZ_L(data)
    elif encoding_scheme_code == 1:
        encoded_signal = encode_NRZ_I(data)
    elif encoding_scheme_code == 2:
        encoded_signal = encode_Bipolar_AMI(data)
    elif encoding_scheme_code == 3:
        encoded_signal = encode_Manchester(data)
    elif encoding_scheme_code == 4:
        encoded_signal = encode_Differential_Manchester(data)
    else:
        print("Invalid encoding scheme code")
        return

    # Write the encoded signal to an output file
    with open("OUTPUT.SIGNAL", 'w') as file:
        file.write(encoded_signal)

    print("Encoded signal saved to OUTPUT.SIGNAL")

if __name__ == "__main__":
    main()
