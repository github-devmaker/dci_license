# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial as serial
import serial
import serial.tools.list_ports
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()
    # ser = serial.Serial(
    #     port='COM5',
    #     baudrate=9600,
    #     parity=serial.PARITY_ODD,
    #     stopbits=serial.STOPBITS_TWO,
    #     bytesize=serial.SEVENBITS,
    #     timeout=1
    # )
    portList = []

    for itemPort in ports:
        portList.append(str(itemPort))
        print(str(portList))

    ser.baudrate = 9600
    ser.port = str('COM5')
    # ser.write_timeout = 1000
    # ser.timeout = 1000
    if not ser.isOpen():
        ser.open()

    brf = bytearray(22)
    brf2 = bytearray(22)
    brf3 = bytearray(22)
    brf4 = bytearray(22)
    ArrBrf = bytearray(brf)
    delay = 0.3

    bf = bytearray(15)
    bf[0] = 0x01
    bf[1] = 0x30
    bf[2] = 0x30
    bf[3] = 0xBA
    bf[4] = 0x30
    bf[5] = 0x37
    bf[6] = 0x01
    bf[7] = 0x00
    bf[8] = 0xBC
    bf[9] = 0x03
    ser.write(bf)
    time.sleep(delay)
    brf = bytearray(ser.read_all())

    ArrBrf[0] = 0x04
    ser.write(ArrBrf)
    time.sleep(delay)
    brf2 = bytearray(ser.read_all())

    bf2 = bytearray(15)
    bf2[0] = 0x04
    bf2[1] = 0x04
    bf2[2] = 0x01
    bf2[3] = 0x30
    bf2[4] = 0x30
    bf2[5] = 0xB9
    bf2[6] = 0x02
    bf2[7] = 0x02
    bf2[8] = 0x01
    bf2[9] = 0x01
    bf2[10] = 0xB9
    bf2[11] = 0x03
    ser.write(bf2)
    time.sleep(delay)
    brf3 = bytearray(ser.read_all())

    ArrBrf[0] = 0x06
    aa = ser.write(ArrBrf)
    time.sleep(delay)
    brf4 = bytearray(ser.read_all())

    brf5 = bytearray(22)
    brf5 = bytearray(brf4)
    tempText = ''
    tempText2 = ''
    if brf5[3] >= 48 & brf5[3] <= 57 | brf5[3] >= 73 & brf5[3] <= 90:
        # print(list(brf5))

        tempText2 = chr(brf5[3])+chr(brf5[4])+chr(brf5[5])+chr(brf5[6])+chr(brf5[7])

        idx = 0
        for item in brf5:

            # tempText += str(item)
            if idx >= 3 & idx <= 7:
                tempText += '|[' + str(idx) + ']' + chr(item) + '|,'
                idx += 1
            else:
                tempText += str(idx) + ','
                idx += 1

    print(tempText)
    print(tempText2)

    ser.close()

