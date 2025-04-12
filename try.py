class CRC8Calculator:
    def __init__(self, polynomial, initial_value=0x00, final_xor=0x00):
        self.polynomial = polynomial
        self.initial_value = initial_value
        self.final_xor = final_xor
        self.crc_table = self.generate_crc_table()

    def generate_crc_table(self):
        crc_table = []
        for byte in range(256):
            crc = 0
            for bit in range(8):
                if (byte ^ crc) & 0x80:
                    crc = (crc << 1) ^ self.polynomial
                else:
                    crc <<= 1
                byte <<= 1
            crc_table.append(crc & 0xFF)
        return crc_table

    def calculate_crc8(self, data):
        crc = self.initial_value
        for byte in data:
            crc = self.crc_table[(crc ^ byte) & 0xFF]
        return crc ^ self.final_xor


data_list = [
    bytearray(b'\xaaUR\x03\x014\xf4'),
    bytearray(b'\xaaUR\x03\x011\xcb'),
    bytearray(b'\xaaUR\x03\x01-\xf5'),
    bytearray(b'\xaaUR\x03\x01)\x94'),
    bytearray(b'\xaaUR\x03\x01%7'),
    bytearray(b'\xaaUR\x03\x01"\xb4'),
    bytearray(b'\xaaUR\x03\x01\x1e\xa9'),
    bytearray(b'\xaaUR\x03\x01\x1c\x15'),
    bytearray(b'\xaaUR\x03\x01\x1a\xc8'),
    bytearray(b'\xaaUR\x03\x01\x18t'),
    bytearray(b'\xaaUS\x07\x01\x00\x00\x00\x00\x042'),
    bytearray(b'\xaaUR\x03\x01\x175'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x1b\x96'),
    bytearray(b'\xaaUR\x03\x01&\xd5'),
    bytearray(b'\xaaUR\x03\x016H'),
    bytearray(b'\xaaUR\x03\x01I\xf1'),
    bytearray(b'\xaaUR\x03\x01[\xd0'),
    bytearray(b'\xaaUR\x03\x01i\xd2'),
    bytearray(b'\xaaUR\x03\x01p\xd3'),
    bytearray(b'\xaaUR\x03\x01q\x8d'),
    bytearray(b'\xaaUR\x03\x01o\x0f'),
    bytearray(b'\xaaUR\x03\x01j0'),
    bytearray(b'\xaaUR\x03\x01d/'),
    bytearray(b'\xaaUR\x03\x01\xdec'),
    bytearray(b'\xaaUR\x03\x01V-'),
    bytearray(b'\xaaUR\x03\x01O,'),
    bytearray(b'\xaaUR\x03\x01H\xaf'),
    bytearray(b'\xaaUR\x03\x01B\xd1'),
    bytearray(b'\xaaUR\x03\x01=h'),
    bytearray(b'\xaaUR\x03\x01;\xb5'),
    bytearray(b'\xaaUR\x03\x019\t'),
    bytearray(b'\xaaUR\x03\x017\x16'),
    bytearray(b'\xaaUR\x03\x015\xaa'),
    bytearray(b'\xaaUR\x03\x013w'),
    bytearray(b'\xaaUR\x03\x01/I'),
    bytearray(b'\xaaUR\x03\x01+('),
    bytearray(b"\xaaUR\x03\x01\'\x8b"),
    bytearray(b'\xaaUR\x03\x01#\xea'),
    bytearray(b'\xaaUR\x03\x01\x1f\xf7'),
    bytearray(b'\xaaUR\x03\x01\x1b\x96'),
    bytearray(b'\xaaUR\x03\x01\x18t'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x14\xd7'),
    bytearray(b'\xaaUR\x03\x01\x13T'),
    bytearray(b'\xaaUR\x03\x01\x11\xe8'),
    bytearray(b'\xaaUR\x03\x01\x10\xb6'),
    bytearray(b'\xaaUR\x03\x01\x10\xb6'),
    bytearray(b'\xaaUR\x03\x01\x0fj'),
    bytearray(b'\xaaUR\x03\x01\x0fj'),
    bytearray(b'\xaaUR\x03\x01\x0fj'),
    bytearray(b'\xaaUR\x03\x01\x0fj'),
    bytearray(b'\xaaUR\x03\x01\x0e4'),
    bytearray(b'\xaaUR\x03\x01\x0e4'),
    bytearray(b'\xaaUR\x03\x01\r\xd6'),
    bytearray(b'\xaaUR\x03\x01\x0c\x88'),
    bytearray(b'\xaaUS\x07\x01\x00\x00\x00\x00\x042'),
    bytearray(b'\xaaUR\x03\x01\x0e4'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01"\xb4'),
    bytearray(b'\xaaUR\x03\x012)'),
    bytearray(b'\xaaUR\x03\x01ER'),
    bytearray(b'\xaaUR\x03\x01U\xcf'),
    bytearray(b'\xaaUR\x03\x01a\x10'),
    bytearray(b'\xaaUR\x03\x01f\x93'),
    bytearray(b'\xaaUR\x03\x01g\xcd'),
    bytearray(b'\xaaUR\x03\x01eq'),
    bytearray(b'\xaaUR\x03\x01a\x10'),
    bytearray(b'\xaaUR\x03\x01\xdd\x81'),
    bytearray(b'\xaaUR\x03\x01X2'),
    bytearray(b'\xaaUR\x03\x01RL'),
    bytearray(b'\xaaUR\x03\x01L\xce'),
    bytearray(b'\xaaUR\x03\x01F\xb0'),
    bytearray(b'\xaaUR\x03\x01A3'),
    bytearray(b'\xaaUR\x03\x01=h'),
    bytearray(b'\xaaUR\x03\x01;\xb5'),
    bytearray(b'\xaaUR\x03\x019\t'),
    bytearray(b'\xaaUR\x03\x017\x16'),
    bytearray(b'\xaaUR\x03\x015\xaa'),
    bytearray(b'\xaaUR\x03\x013w'),
    bytearray(b'\xaaUR\x03\x010\x95'),
    bytearray(b'\xaaUR\x03\x01-\xf5'),
    bytearray(b'\xaaUR\x03\x01)\x94'),
    bytearray(b'\xaaUR\x03\x01&\xd5'),
    bytearray(b'\xaaUR\x03\x01#\xea'),
    bytearray(b'\xaaUR\x03\x01!V'),
    bytearray(b'\xaaUR\x03\x01\x1f\xf7'),
    bytearray(b'\xaaUR\x03\x01\x1dK'),
    bytearray(b'\xaaUR\x03\x01\x1c\x15'),
    bytearray(b'\xaaUR\x03\x01\x1b\x96'),
    bytearray(b'\xaaUR\x03\x01\x1a\xc8'),
    bytearray(b'\xaaUR\x03\x01\x18t'),
    bytearray(b'\xaaUR\x03\x01\x175'),
    bytearray(b'\xaaUR\x03\x01\x175'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x175'),
    bytearray(b'\xaaUR\x03\x01\x16k'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x15\x89'),
    bytearray(b'\xaaUR\x03\x01\x1a\xc8'),
    bytearray(b'\xaaUR\x03\x01$i'),
    bytearray(b'\xaaUR\x03\x012)'),
    bytearray(b'\xaaUR\x03\x01C\x8f'),
    bytearray(b'\xaaUR\x03\x01S\x12'),
    bytearray(b'\xaaUS\x07\x01bQ\x00\x00\x00\x96'),
    bytearray(b'\xaaUR\x03\x01_\xb1'),
    bytearray(b'\xaaUR\x03\x01eq'),
    bytearray(b'\xaaUR\x03\x01f\x93'),
    bytearray(b'\xaaUR\x03\x01c\xac'),
    bytearray(b'\xaaUR\x03\x01^\xef'),
    bytearray(b'\xaaUR\x03\x01\xd9\xe0'),
    bytearray(b'\xaaUR\x03\x01S\x12'),
    bytearray(b'\xaaUR\x03\x01M\x90'),
    bytearray(b'\xaaUR\x03\x01F\xb0'),
    bytearray(b'\xaaUR\x03\x01A3'),
    bytearray(b'\xaaUR\x03\x01<6'),
    bytearray(b'\xaaUR\x03\x019\t'),
    bytearray(b'\xaaUR\x03\x018W'),
    bytearray(b'\xaaUR\x03\x019\t'),
    bytearray(b'\xaaUR\x03\x019\t'),
    bytearray(b'\xaaUR\x03\x018W'),
    bytearray(b'\xaaUR\x03\x017\x16'),
    bytearray(b'\xaaUR\x03\x015\xaa'),
    bytearray(b'\xaaUR\x03\x012)'),
    bytearray(b'\xaaUR\x03\x01/I'),
    bytearray(b'\xaaUR\x03\x01,\xab'),
    bytearray(b'\xaaUR\x03\x01)\x94'),
    bytearray(b'\xaaUR\x03\x01&\xd5'),
    bytearray(b'\xaaUR\x03\x01#\xea'),
    bytearray(b'\xaaUR\x03\x01!V'),
    bytearray(b'\xaaUR\x03\x01\x1e\xa9'),
    bytearray(b'\xaaUR\x03\x01\x1dK'),
    bytearray(b'\xaaUR\x03\x01\x1b\x96'),
    bytearray(b'\xaaUR\x03\x01\x1a\xc8'),
    bytearray(b'\xaaUR\x03\x01\x1a\xc8'),
    bytearray(b'\xaaUR\x03\x01\x19*')
]

# 暴力枚举多项式、初始值和最终异或值
for polynomial in range(0x01, 0x100):
    for initial_value in range(0x00, 0x100):
        for final_xor in range(0x00, 0x100):
            crc_calculator = CRC8Calculator(polynomial, initial_value, final_xor)
            all_passed = True
            for data in data_list:
                expected_crc = data[-1]
                calculated_crc = crc_calculator.calculate_crc8(data[:-1])
                if calculated_crc != expected_crc:
                    all_passed = False
                    break
            if all_passed:
                print(f"找到合适的参数: 多项式 = 0x{polynomial:02x}, 初始值 = 0x{initial_value:02x}, 最终异或值 = 0x{final_xor:02x}")
                break
            else:
                print('未成功')

if all_passed:
    print("所有数据都通过了CRC校验！")
else:
    print("某些数据未通过CRC校验！")