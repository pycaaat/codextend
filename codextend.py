# codextend.py

try:
    import chardet
except ImportError:
    print("Please install 'chardet' package to use this module.")

def binary_file(codepath, numbits=8, numbytes=None, start_line=None, end_line=None):
    """
    Convert file content to binary representation.

    Parameters:
    codepath (str): The path to the file.
    numbits (int): The number of bits to use for each byte (default is 8).
    numbytes (int, optional): The number of bytes to read from the file.
    start_line (int, optional): The starting line number to convert.
    end_line (int, optional): The ending line number to convert.

    Returns:
    str: The binary representation of the file content.
    """
    try:
        with open(codepath, 'rb') as file:
            byte_data = file.read()
        binarydata = ' '.join(format(byte, f'0{numbits}b') for byte in byte_data)
        return binarydata
    except FileNotFoundError:
        return f"The file {codepath} was not found."
    except Exception as e:
        return f"{e}"

def bin_text(oriext, start_line=1, end_line=None, numbytes=None, numbits=8):
    """
    Convert text to binary representation.

    Parameters:
    oriext (str): The original text to convert.
    start_line (int): The starting line number to convert.
    end_line (int, optional): The ending line number to convert.
    numbytes (int, optional): The number of bytes to convert from each line.
    numbits (int): The number of bits to use for each byte.

    Returns:
    str: The binary representation of the text.
    """
    try:
        lines = oriext.splitlines()
        if end_line is not None and (start_line > end_line or start_line < 1):
            return "Invalid line range."
        selected_lines = lines[start_line - 1:end_line]
        bin_lines = []
        for line in selected_lines:
            byte_data = line.encode('utf-8')[:numbytes]
            bin_line = ' '.join(format(byte, f'0{numbits}b') for byte in byte_data)
            bin_lines.append(bin_line)
        return '\n'.join(bin_lines)
    except Exception as e:
        return f"{e}"

def cvet(encet, fenc, tenc):
    """
    Convert text encoding.

    Parameters:
    encet (str): The text to convert.
    fenc (str): The original encoding of the text.
    tenc (str): The target encoding to convert the text to.

    Returns:
    str: The converted text.
    """
    try:
        if fenc.upper() != 'UTF-8':
            encet = encet.encode(fenc).decode('utf-8')
        cenc = encet.encode('utf-8').decode(tenc)
        return cenc
    except UnicodeDecodeError as e:
        return f"{e}"
    except UnicodeEncodeError as e:
        return f"{e}"
    except Exception as e:
        return f"{e}"

def cfen(codepath, tarcode):
    """
    Convert file encoding.

    Parameters:
    codepath (str): The path to the file.
    tarcode (str): The target encoding to convert the file to.

    Returns:
    str: A message indicating success or the error encountered.
    """
    try:
        with open(codepath, 'rb') as file:
            raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
        print(f"Detected file encoding: {detected_encoding}")

        if detected_encoding != 'utf-8':
            content = raw_data.decode(detected_encoding, errors='ignore')
            converted_content = content.encode('utf-8').decode('utf-8')
        else:
            converted_content = raw_data.decode('utf-8', errors='ignore')
        final_content = converted_content.encode(tarcode, errors='ignore').decode(tarcode, errors='ignore')
        with open(codepath, 'w', encoding=tarcode, errors='ignore') as file:
            file.write(final_content)
        return "File encoding converted successfully."
    except FileNotFoundError:
        return f"The file {codepath} was not found."
    except Exception as e:
        return f"{e}"

def hex_file(codepath, numbytes=None, start_line=None, end_line=None):
    """
    Convert file content to hexadecimal representation.

    Parameters:
    codepath (str): The path to the file.
    numbytes (int, optional): The number of bytes to read from the file.
    start_line (int, optional): The starting line number to convert.
    end_line (int, optional): The ending line number to convert.

    Returns:
    str: The hexadecimal representation of the file content.
    """
    try:
        with open(codepath, 'rb') as file:
            if numbytes is not None:
                byte_data = file.read(numbytes)
            else:
                byte_data = file.read()
        hexdata = ' '.join(format(byte, '02x') for byte in byte_data)
        return hexdata
    except FileNotFoundError:
        return f"The file {codepath} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def hex_text(oriext, start_line=1, end_line=None, numbytes=None):
    """
    Convert text to hexadecimal representation.

    Parameters:
    oriext (str): The original text to convert.
    start_line (int): The starting line number to convert.
    end_line (int, optional): The ending line number to convert.
    numbytes (int, optional): The number of bytes to convert from each line.

    Returns:
    str: The hexadecimal representation of the text.
    """
    try:
        lines = oriext.splitlines()
        if end_line is not None and (start_line > end_line or start_line < 1):
            return "Invalid line range."
        selected_lines = lines[start_line - 1:end_line]
        hex_lines = []
        for line in selected_lines:
            byte_data = line.encode('utf-8')[:numbytes]
            hex_line = ' '.join(format(byte, '02x') for byte in byte_data)
            hex_lines.append(hex_line)
        return '\n'.join(hex_lines)
    except Exception as e:
        return f"{e}"
#end        