# roscpp vs python benchmarks

Tests done on a:
Intel® Core™ i7-6700HQ CPU @ 2.60GHz × 8 

16GB RAM, GeForce GTX 1070/PCIe/SSE2
Ubuntu 18.04.5
ROS Melodic

# Rate of publication

Checking rate with `rostopic hz`.

## Simple message (std_msgs/String)`

### Max rate of publication

Publisher Python: 33513~ Hz

Publisher C++: 50505~ Hz

Publisher Python ROSCPP: 45000~ Hz

## Big message (sensor_msgs/Image)

Image size: 512x512

## Max rate of publication

Publisher Python: 1870~ Hz

Publisher C++: 1600~ Hz

(Weird?)

# CPU usage & Memory usage

## Publisher

### Simple message (std_msgs/String)

#### 10 Hz

Python: 1% CPU, 43MB RAM
C++: 0.3% CPU, 8.9MB RAM

#### 30 Hz

Python: 2.3% CPU, 43MB RAM
C++: 1% CPU, 8.9MB RAM

#### 50 Hz

Python: 3.3% CPU, 43MB RAM
C++: 1.7% CPU, 8.9MB RAM


#### 100 Hz

Python: 6.7% CPU, 43MB RAM
C++: 3.0% CPU, 8.9MB RAM

Python ROSCPP: 5.6% CPU, 47.7MB RAM

### Complex message (sensor_msgs/Image)


#### 10 Hz

Python: 2% CPU, 71MB RAM
C++:  1%CPU, MB RAM

#### 30 Hz

Python: 6% CPU, 71MB RAM
C++:  3.3%CPU, 24MB RAM

#### 50 Hz
Python: 10% CPU, 71MB RAM
C++:  5.3%CPU, 24MB RAM

#### 100 Hz

Python: 19% CPU, 71MB RAM
C++:  10.0%CPU, 24MB RAM


# Delay of messages

Using `rostopic delay`.

##  Images only

Python: 0.001s
C++: 0.001s



# Subscribers

Subscribing to std_msgs/String

## CPU usage

### 30Hz 

Python: 1%
C++: 1%

### 50Hz 

Python: 1.3%
C++: 1.3%


### 100Hz 

Python: 2.7%
C++: 2.7%

### 1000Hz 

Python: 14%
C++: 16%

(Weird)



# Current conclusions:

For tiny messages:

Having publishers in C++ may be a bit more efficient.

Having subscribers, not really.

For big messages:

If the data needs to be processed, it will for sure be faster in C++.
