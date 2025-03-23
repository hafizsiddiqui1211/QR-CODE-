# QR Code Generator

This Python script generates a QR code for a given URL and saves it as an image file.

## Prerequisites

Ensure you have Python installed on your system. You also need the `qrcode` library, which can be installed using:

```sh
pip install qrcode[pil]
```

## Usage

1. Clone this repository or copy the script to your local machine.
2. Run the script using:

```sh
python script.py
```

3. The script will generate a QR code for the provided URL and save it as `Hafiz Siddiqui.png`.

## Code Explanation

- The script uses the `qrcode` library to generate a QR code.
- It encodes the URL `https://www.linkedin.com/in/hafiz-siddiqui-018587295/`.
- The generated QR code is saved as an image file (`Hafiz Siddiqui.png`).

## Output

After running the script, you will see:

```sh
<class 'qrcode.image.pil.PilImage'>
QR code has been generated
```

The QR code image will be saved in the same directory.

## License

This project is open-source and available for use and modification.