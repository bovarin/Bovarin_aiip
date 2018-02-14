from __future__ import print_function
import time  # for delaying in second
import random  # to simulate 16 float readings between 0 and 1
import datetime



# Dummy dataset for 32 sensors with 16 float readings each.
Sensors = []
sensor1 = {'ID':'sensor1', 'readings1': 'r1'} # data stream for sensor 1 referenced to pipeline region 1
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r1 = random.random()  # generates random number between 0 and 1
    Sensors.append( sensor1)


sensor2 = {'ID':'sensor2', 'readings2': 'r2'} # data stream for sensor 1 referenced to pipeline region 1
Sensors.append(sensor2)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r2 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor2)


sensor3 = {'ID':'sensor3', 'readings3': 'r3'} # data stream for sensor 3 referenced to pipeline region 3
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r3 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor3)


sensor4 = {'ID':'sensor4', 'readings4': 'r4'} # data stream for sensor 4 referenced to pipeline region 4
Sensors.append(sensor4)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r4 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor4)


sensor5 = {'ID':'sensor5', 'readings5': 'r5'} # data stream for sensor 5 referenced to pipeline region 5
Sensors.append(sensor5)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r5 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor5)


sensor6 = {'ID':'sensor6', 'readings6': 'r6'} # data stream for sensor 6 referenced to pipeline region 6
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r6 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor6)


sensor7 = {'ID':'sensor7', 'readings7': 'r7'} # data stream for sensor 7 referenced to pipeline region 7
Sensors.append(sensor7)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r7 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor7)


sensor8 = {'ID':'sensor8', 'readings8': 'r8'} # data stream for sensor 8 referenced to pipeline region 8
Sensors.append(sensor8)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r8 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor8)


sensor9 = {'ID':'sensor9', 'readings9': 'r9'} # data stream for sensor 9 referenced to pipeline region 9
Sensors.append(sensor9)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r9 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor9)


sensor10 = {'ID':'sensor10', 'readings10': 'r10'} # data stream for sensor 10 referenced to pipeline region 10
Sensors.append(sensor10)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r10 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor10)


sensor11 = {'ID':'sensor11', 'readings11': 'r11'} # data stream for sensor 11 referenced to pipeline region 11
Sensors.append(sensor11)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r11 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor11)


sensor12 = {'ID':'sensor12', 'readings12': 'r12'} # data stream for sensor 12 referenced to pipeline region 12
Sensors.append(sensor12)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r12 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor12)


sensor13 = {'ID':'sensor13', 'readings13': 'r13'} # data stream for sensor 13 referenced to pipeline region 13
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r13 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor13)


sensor14 = {'ID':'sensor14', 'readings14': 'r14'} # data stream for sensor 14 referenced to pipeline region 14
Sensors.append(sensor14)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r14 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor14)


sensor15 = {'ID':'sensor15', 'readings15': 'r15'} # data stream for sensor 15 referenced to pipeline region 15
Sensors.append(sensor15)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r15 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor15)


sensor16 = {'ID':'sensor16', 'readings16': 'r16'} # data stream for sensor 16 referenced to pipeline region 16
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r16 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor16)


sensor17 = {'ID':'sensor17', 'readings17': 'r17'} # data stream for sensor 17 referenced to pipeline region 17
Sensors.append(sensor17)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r17 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor17)


sensor18 = {'ID':'sensor18', 'readings18': 'r18'} # data stream for sensor 18 referenced to pipeline region 18
Sensors.append(sensor18)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r18 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor18)


sensor19 = {'ID':'sensor19', 'readings19': 'r19'} # data stream for sensor 19 referenced to pipeline region 19
Sensors.append(sensor19)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r19 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor19)


sensor20 = {'ID':'sensor20', 'readings20': 'r20'} # data stream for sensor 20 referenced to pipeline region 20
Sensors.append(sensor20)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r20 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor20)


sensor21 = {'ID':'sensor21', 'readings21': 'r21'} # data stream for sensor 21 referenced to pipeline region 21
Sensors.append(sensor21)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r21 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor21)


sensor22 = {'ID':'sensor22', 'readings22': 'r22'} # data stream for sensor 22 referenced to pipeline region 22
Sensors.append(sensor22)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r22 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor22)


sensor23 = {'ID':'sensor23', 'readings23': 'r23'} # data stream for sensor 23 referenced to pipeline region 23
Sensors.append(sensor23)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r23 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor23)


sensor24 = {'ID':'sensor24', 'readings24': 'r24'} # data stream for sensor 24 referenced to pipeline region 24
Sensors.append(sensor24)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r24 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor24)


sensor25 = {'ID':'sensor25', 'readings25': 'r25'} # data stream for sensor 1 referenced to pipeline region 1
Sensors.append(sensor25)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r25 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor25)


sensor26 = {'ID':'sensor26', 'readings26': 'r26'} # data stream for sensor 26 referenced to pipeline region 26
Sensors.append(sensor26)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r26 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor26)


sensor27 = {'ID':'sensor27', 'readings27': 'r27'} # data stream for sensor 27 referenced to pipeline region 27
Sensors.append(sensor27)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r27 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor27)


sensor28 = {'ID':'sensor28', 'readings28': 'r28'} # data stream for sensor 28 referenced to pipeline region 28
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r28 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor28)


sensor29 = {'ID':'sensor29', 'readings29': 'r29'} # data stream for sensor 29 referenced to pipeline region 29
Sensors.append(sensor29)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r29 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor29)


sensor30 = {'ID':'sensor30', 'readings30': 'r30'} # data stream for sensor 30 referenced to pipeline region 30
Sensors.append(sensor30)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r30 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor30)


sensor31 = {'ID':'sensor31', 'readings31': 'r31'} # data stream for sensor 31 referenced to pipeline region 31
Sensors.append(sensor1)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r31 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor31)


sensor32 = {'ID':'sensor32', 'readings32': 'r32'} # data stream for sensor 32 referenced to pipeline region 32
Sensors.append(sensor32)
count = 16  # represents 16 float readings
for i in range( 0, count ):
    r32 = random.random()  # generates random number between 0 and 1
    Sensors.append(sensor32)


# Storing data to avoid averwriting data


n = 1
for x in range( 3 ):
    print( 'sequence', n )
    print( time.ctime() )

    sensor1 = [ ]  # data stream for sensor 1 which is referenced to pipeline region 1
    print( 'sensor1 \npipeline region 1' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r1 = random.random()  # generates random number between 0 and 1
        sensor1.append( r1 )

    print( sensor1 )

    sensor2 = [ ]  # data stream for sensor 2 which is referenced to pipeline region 2
    print( 'sensor2 \npipeline region 2' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r2 = random.random()  # generates random number between 0 and 1
        sensor2.append( r2 )

    print( sensor2 )

    sensor3 = [ ]  # data stream for sensor 3 which is referenced to pipeline region 3
    print( 'sensor 3 \npipeline region 3' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r3 = random.random()  # generates random number between 0 and 1
        sensor3.append( r3 )

    print( sensor3 )

    sensor4 = [ ]  # data stream for sensor 4 which is referenced to pipeline region 4
    print( 'sensor 4 \npipeline region 4' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r4 = random.random()  # generates random number between 0 and 1
        sensor4.append( r4 )

    print( sensor4 )

    sensor5 = [ ]  # data stream for sensor 5 which is referenced to pipeline region 5
    print( 'sensor 5 \npipeline region 5' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r5 = random.random()  # generates random number between 0 and 1
        sensor5.append( r5 )

    print( sensor5 )

    sensor6 = [ ]  # data stream for sensor 6 which is referenced to pipeline region 6
    print( 'sensor 6 \npipeline region 6' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r6 = random.random()  # generates random number between 0 and 1
        sensor6.append( r6 )

    print( sensor6 )

    sensor7 = [ ]  # data stream for sensor 7 which is referenced to pipeline region 7
    print( 'sensor 7 \npipeline region 7' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r7 = random.random()  # generates random number between 0 and 1
        sensor7.append( r7 )

    print( sensor7 )

    sensor8 = [ ]  # data stream for sensor 8 which is referenced to pipeline region 8
    print( 'sensor 8 \npipeline region 8' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r8 = random.random()  # generates random number between 0 and 1
        sensor8.append( r8 )

    print( sensor8 )

    sensor9 = [ ]  # data stream for sensor 9 which is referenced to pipeline region 9
    print( 'sensor 9 \npipeline region 9' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r9 = random.random()  # generates random number between 0 and 1
        sensor9.append( r9 )

    print( sensor9 )

    sensor10 = [ ]  # data stream for sensor 10 which is referenced to pipeline region 10
    print( 'sensor 10 \npipeline region 10' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r10 = random.random()  # generates random number between 0 and 1
        sensor10.append( r10 )

    print( sensor10 )

    sensor11 = [ ]  # data stream for sensor 11 which is referenced to pipeline region 11
    print( 'sensor 11 \npipeline region 11' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r11 = random.random()  # generates random number between 0 and 1
        sensor11.append( r11 )

    print( sensor11 )

    sensor12 = [ ]  # data stream for sensor 12 which is referenced to pipeline region 12
    print( 'sensor 12 \npipeline region 12' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r12 = random.random()  # generates random number between 0 and 1
        sensor12.append( r12 )

    print( sensor12 )

    sensor13 = [ ]  # data stream for sensor 13 which is referenced to pipeline region 13
    print( 'sensor 13 \npipeline region 13' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r13 = random.random()  # generates random number between 0 and 1
        sensor13.append( r13 )

    print( sensor13 )

    sensor14 = [ ]  # data stream for sensor 14 which is referenced to pipeline region 14
    print( 'sensor 14 \npipeline region 14' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r14 = random.random()  # generates random number between 0 and 1
        sensor14.append( r14 )

    print( sensor14 )

    sensor15 = [ ]  # data stream for sensor 15 which is referenced to pipeline region 15
    print( 'sensor 15 \npipeline region 15' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r15 = random.random()  # generates random number between 0 and 1
        sensor15.append( r15 )

    print( sensor15 )

    sensor16 = [ ]  # data stream for sensor 16 which is referenced to pipeline region 16
    print( 'sensor 16 \npipeline region 16' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r16 = random.random()  # generates random number between 0 and 1
        sensor16.append( r16 )

    print( sensor16 )

    sensor17 = [ ]  # data stream for sensor 17 which is referenced to pipeline region 17
    print( 'sensor 17 \npipeline region 17' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r17 = random.random()  # generates random number between 0 and 1
        sensor17.append( r17 )

    print( sensor17 )

    sensor18 = [ ]  # data stream for sensor 18 which is referenced to pipeline region 18
    print( 'sensor 18 \npipeline region 18' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r18 = random.random()  # generates random number between 0 and 1
        sensor18.append( r18 )

    print( sensor18 )

    sensor19 = [ ]  # data stream for sensor 19 which is referenced to pipeline region 19
    print( 'sensor 19 \npipeline region 19' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r19 = random.random()  # generates random number between 0 and 1
        sensor19.append( r19 )

    print( sensor19 )

    sensor20 = [ ]  # data stream for sensor 20 which is referenced to pipeline region 20
    print( 'sensor 20 \npipeline region 20' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r20 = random.random()  # generates random number between 0 and 1
        sensor20.append( r20 )

    print( sensor20 )

    sensor21 = [ ]  # data stream for sensor 21 which is referenced to pipeline region 21
    print( 'sensor 21 \npipeline region 21' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r21 = random.random()  # generates random number between 0 and 1
        sensor21.append( r21 )

    print( sensor21 )

    sensor22 = [ ]  # data stream for sensor 22 which is referenced to pipeline region 22
    print( 'sensor 22 \npipeline region 22' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r22 = random.random()  # generates random number between 0 and 1
        sensor22.append( r22 )

    print( sensor22 )

    sensor23 = [ ]  # data stream for sensor 23 which is referenced to pipeline region 23
    print( 'sensor 23 \npipeline region 23' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r23 = random.random()  # generates random number between 0 and 1
        sensor23.append( r23 )

    print( sensor23 )

    sensor24 = [ ]  # data stream for sensor 24 which is referenced to pipeline region 24
    print( 'sensor 24 \npipeline region 24' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r24 = random.random()  # generates random number between 0 and 1
        sensor24.append( r24 )

    print( sensor24 )

    sensor25 = [ ]  # data stream for sensor 25 which is referenced to pipeline region 25
    print( 'sensor 25 \npipeline region 25' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r25 = random.random()  # generates random number between 0 and 1
        sensor25.append( r25 )

    print( sensor25 )

    sensor26 = [ ]  # data stream for sensor 26 which is referenced to pipeline region 26
    print( 'sensor 26 \npipeline region 26' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r26 = random.random()  # generates random number between 0 and 1
        sensor26.append( r26 )

    print( sensor26 )

    sensor27 = [ ]  # data stream for sensor 27 which is referenced to pipeline region 27
    print( 'sensor 27 \npipeline region 27' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r27 = random.random()  # generates random number between 0 and 1
        sensor27.append( r27 )

    print( sensor27 )

    sensor28 = [ ]  # data stream for sensor 28 which is referenced to pipeline region 28
    print( 'sensor 28 \npipeline region 28' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r28 = random.random()  # generates random number between 0 and 1
        sensor28.append( r28 )

    print( sensor28 )

    sensor29 = [ ]  # data stream for sensor 29 which is referenced to pipeline region 29
    print( 'sensor 29 \npipeline region 29' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r29 = random.random()  # generates random number between 0 and 1
        sensor29.append( r29 )

    print( sensor29 )

    sensor30 = [ ]  # data stream for sensor 30 which is referenced to pipeline region 30
    print( 'sensor 30 \npipeline region 30' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r30 = random.random()  # generates random number between 0 and 1
        sensor30.append( r30 )

    print( sensor30 )

    sensor31 = [ ]  # data stream for sensor 31 which is referenced to pipeline region 31
    print( 'sensor 31 \npipeline region 31' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r31 = random.random()  # generates random number between 0 and 1
        sensor31.append( r31 )

    print( sensor31 )

    sensor32 = [ ]  # data stream for sensor 32 which is referenced to pipeline region 32
    print( 'sensor 32 \npipeline region 32' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r32 = random.random()  # generates random number between 0 and 1
        sensor32.append( r32 )

    print( sensor32 )
    time.sleep( 4 )
    n = n + 1

# let storage data in data_storage file
f = open( 'Data_storage.txt', 'w' )
print( f )

_print = print  # reference to original print function
outfile = open( 'Data_storage.txt', 'w' )  # file to write output to, mode is 'w' for writing


def print(*args, **kwargs):
    """new print function always writing to file
    """
    _print( *args, file=outfile, **kwargs )


print( 'Data storage file for 32 sensors\nEach number references a different pipeline region'
       '\nValues in each sensor represent 16 readings floats between 0 and 1' )
print( '' )
print( '' )

print(Sensors)
print('')
print('')

n = 1

for x in range( 3 ):
    print( 'sequence', n )
    print( 'Date and Time' )
    print( time.ctime() )

    sensor1 = [ ]  # data stream for sensor 1 which is referenced to pipeline region 1
    print( 'sensor1 \npipeline region 1' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r1 = random.random()  # generates random number between 0 and 1
        sensor1.append( r1 )

    print( sensor1 )
    print( '' )

    sensor2 = [ ]  # data stream for sensor 2 which is referenced to pipeline region 2
    print( 'sensor2 \npipeline region 2' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r2 = random.random()  # generates random number between 0 and 1
        sensor2.append( r2 )

    print( sensor2 )
    print( '' )

    sensor3 = [ ]  # data stream for sensor 3 which is referenced to pipeline region 3
    print( 'sensor 3 \npipeline region 3' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r3 = random.random()  # generates random number between 0 and 1
        sensor3.append( r3 )

    print( sensor3 )
    print( '' )

    sensor4 = [ ]  # data stream for sensor 4 which is referenced to pipeline region 4
    print( 'sensor 4 \npipeline region 4' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r4 = random.random()  # generates random number between 0 and 1
        sensor4.append( r4 )

    print( sensor4 )
    print( '' )
    sensor5 = [ ]  # data stream for sensor 5 which is referenced to pipeline region 5
    print( 'sensor 5 \npipeline region 5' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r5 = random.random()  # generates random number between 0 and 1
        sensor5.append( r5 )

    print( sensor5 )
    print( '' )

    sensor6 = [ ]  # data stream for sensor 6 which is referenced to pipeline region 6
    print( 'sensor 6 \npipeline region 6' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r6 = random.random()  # generates random number between 0 and 1
        sensor6.append( r6 )

    print( sensor6 )
    print( '' )

    sensor7 = [ ]  # data stream for sensor 7 which is referenced to pipeline region 7
    print( 'sensor 7 \npipeline region 7' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r7 = random.random()  # generates random number between 0 and 1
        sensor7.append( r7 )

    print( sensor7 )
    print( '' )

    sensor8 = [ ]  # data stream for sensor 8 which is referenced to pipeline region 8
    print( 'sensor 8 \npipeline region 8' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r8 = random.random()  # generates random number between 0 and 1
        sensor8.append( r8 )

    print( sensor8 )
    print( '' )

    sensor9 = [ ]  # data stream for sensor 9 which is referenced to pipeline region 9
    print( 'sensor 9 \npipeline region 9' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r9 = random.random()  # generates random number between 0 and 1
        sensor9.append( r9 )

    print( sensor9 )
    print( '' )

    sensor10 = [ ]  # data stream for sensor 10 which is referenced to pipeline region 10
    print( 'sensor 10 \npipeline region 10' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r10 = random.random()  # generates random number between 0 and 1
        sensor10.append( r10 )

    print( sensor10 )
    print( '' )

    sensor11 = [ ]  # data stream for sensor 11 which is referenced to pipeline region 11
    print( 'sensor 11 \npipeline region 11' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r11 = random.random()  # generates random number between 0 and 1
        sensor11.append( r11 )

    print( sensor11 )
    print( '' )

    sensor12 = [ ]  # data stream for sensor 12 which is referenced to pipeline region 12
    print( 'sensor 12 \npipeline region 12' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r12 = random.random()  # generates random number between 0 and 1
        sensor12.append( r12 )

    print( sensor12 )
    print( '' )

    sensor13 = [ ]  # data stream for sensor 13 which is referenced to pipeline region 13
    print( 'sensor 13 \npipeline region 13' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r13 = random.random()  # generates random number between 0 and 1
        sensor13.append( r13 )

    print( sensor13 )
    print( '' )

    sensor14 = [ ]  # data stream for sensor 14 which is referenced to pipeline region 14
    print( 'sensor 14 \npipeline region 14' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r14 = random.random()  # generates random number between 0 and 1
        sensor14.append( r14 )

    print( sensor14 )
    print( '' )

    sensor15 = [ ]  # data stream for sensor 15 which is referenced to pipeline region 15
    print( 'sensor 15 \npipeline region 15' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r15 = random.random()  # generates random number between 0 and 1
        sensor15.append( r15 )

    print( sensor15 )
    print( '' )

    sensor16 = [ ]  # data stream for sensor 16 which is referenced to pipeline region 16
    print( 'sensor 16 \npipeline region 16' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r16 = random.random()  # generates random number between 0 and 1
        sensor16.append( r16 )

    print( sensor16 )
    print( '' )

    sensor17 = [ ]  # data stream for sensor 17 which is referenced to pipeline region 17
    print( 'sensor 17 \npipeline region 17' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r17 = random.random()  # generates random number between 0 and 1
        sensor17.append( r17 )

    print( sensor17 )
    print( '' )

    sensor18 = [ ]  # data stream for sensor 18 which is referenced to pipeline region 18
    print( 'sensor 18 \npipeline region 18' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r18 = random.random()  # generates random number between 0 and 1
        sensor18.append( r18 )

    print( sensor18 )
    print( '' )

    sensor19 = [ ]  # data stream for sensor 19 which is referenced to pipeline region 19
    print( 'sensor 19 \npipeline region 19' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r19 = random.random()  # generates random number between 0 and 1
        sensor19.append( r19 )

    print( sensor19 )
    print( '' )

    sensor20 = [ ]  # data stream for sensor 20 which is referenced to pipeline region 20
    print( 'sensor 20 \npipeline region 20' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r20 = random.random()  # generates random number between 0 and 1
        sensor20.append( r20 )

    print( sensor20 )
    print( '' )

    sensor21 = [ ]  # data stream for sensor 21 which is referenced to pipeline region 21
    print( 'sensor 21 \npipeline region 21' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r21 = random.random()  # generates random number between 0 and 1
        sensor21.append( r21 )

    print( sensor21 )
    print( '' )

    sensor22 = [ ]  # data stream for sensor 22 which is referenced to pipeline region 22
    print( 'sensor 22 \npipeline region 22' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r22 = random.random()  # generates random number between 0 and 1
        sensor22.append( r22 )

    print( sensor22 )
    print( '' )

    sensor23 = [ ]  # data stream for sensor 23 which is referenced to pipeline region 23
    print( 'sensor 23 \npipeline region 23' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r23 = random.random()  # generates random number between 0 and 1
        sensor23.append( r23 )

    print( sensor23 )
    print( '' )

    sensor24 = [ ]  # data stream for sensor 24 which is referenced to pipeline region 24
    print( 'sensor 24 \npipeline region 24' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r24 = random.random()  # generates random number between 0 and 1
        sensor24.append( r24 )

    print( sensor24 )
    print( '' )

    sensor25 = [ ]  # data stream for sensor 25 which is referenced to pipeline region 25
    print( 'sensor 25 \npipeline region 25' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r25 = random.random()  # generates random number between 0 and 1
        sensor25.append( r25 )

    print( sensor25 )
    print( '' )

    sensor26 = [ ]  # data stream for sensor 26 which is referenced to pipeline region 26
    print( 'sensor 26 \npipeline region 26' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r26 = random.random()  # generates random number between 0 and 1
        sensor26.append( r26 )

    print( sensor26 )
    print( '' )

    sensor27 = [ ]  # data stream for sensor 27 which is referenced to pipeline region 27
    print( 'sensor 27 \npipeline region 27' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r27 = random.random()  # generates random number between 0 and 1
        sensor27.append( r27 )

    print( sensor27 )
    print( '' )

    sensor28 = [ ]  # data stream for sensor 28 which is referenced to pipeline region 28
    print( 'sensor 28 \npipeline region 28' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r28 = random.random()  # generates random number between 0 and 1
        sensor28.append( r28 )

    print( sensor28 )
    print( '' )

    sensor29 = [ ]  # data stream for sensor 29 which is referenced to pipeline region 29
    print( 'sensor 29 \npipeline region 29' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r29 = random.random()  # generates random number between 0 and 1
        sensor29.append( r29 )

    print( sensor29 )
    print( '' )

    sensor30 = [ ]  # data stream for sensor 30 which is referenced to pipeline region 30
    print( 'sensor 30 \npipeline region 30' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r30 = random.random()  # generates random number between 0 and 1
        sensor30.append( r30 )

    print( sensor30 )
    print( '' )

    sensor31 = [ ]  # data stream for sensor 31 which is referenced to pipeline region 31
    print( 'sensor 31 \npipeline region 31' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r31 = random.random()  # generates random number between 0 and 1
        sensor31.append( r31 )

    print( sensor31 )
    print( '' )

    sensor32 = [ ]  # data stream for sensor 32 which is referenced to pipeline region 32
    print( 'sensor 32 \npipeline region 32' )
    count = 16  # represents 16 float readings
    for i in range( 0, count ):
        r32 = random.random()  # generates random number between 0 and 1
        sensor32.append( r32 )

    print( sensor32 )
    print( '' )
    print( '' )
    time.sleep( 4 )
    n = n + 1
outfile.close()

# Corrupted data file logs
f = open( 'Error_storage.txt', 'w' )




