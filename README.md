# Structurally Configurable Mobile Robot - Wheeldog_rev001
<p align="center">
  <table>
    <tr>
      <td><img src="https://github.com/jakubsarata/wheeldog-rev001/blob/main/Wheeldog_proto_1.png" width="400"></td>
      <td><img src="https://github.com/jakubsarata/wheeldog-rev001/blob/main/Wheeldog_proto_2.png" width="400"></td>
    </tr>
  </table>
</p>

## Overview
This project presents an open-source **structurally configurable mobile robot**, which combines the benefits of wheeled and legged locomotion. The robot is inspired by designs such as ANYmal, but with enhanced flexibility and mobility due to additional degrees of freedom and omnidirectional wheels.

Originally developed as part of a master's thesis at the **AGH University of Science and Technology**, this project is now available to the open-source community for further development and application.

## Features
- **Hybrid Locomotion**: Utilizes both wheels for speed and efficiency on smooth surfaces, and legs for traversing rough terrains and obstacles.
- **Adaptive Configuration**: The body features three degrees of freedom, allowing for movement akin to natural creatures like lizards.
- **Omnidirectional Wheels**: Enables maneuverability in tight spaces and precise movement control.
- **Simulation and Real-World Testing**: Verified through MATLAB simulations and physical prototyping.
- **Expandable and Modular**: Designed with 3D printing and modular assembly in mind, allowing for modifications and improvements.

## System Components
### Hardware
- **Actuators**: 15 Feetech FT6325M servomotors
- **Motors**: 4 Pololu 2373 DC motors
- **Main Controller**: Raspberry Pi 4B
- **Motor Drivers**: PCA9685 for servos, M2T256 for DC motors
- **Sensors**:
  - Adafruit 4754 IMU for motion tracking
  - Pololu 4761 encoders for wheel speed measurement
  - Raspberry Pi Camera HD v2 for future vision applications
- **Power Supply**: Laboratory power supply (for prototyping phase)
- **Chassis**: 3D-printed components

### Software
- **Programming Language**: Python & C++
- **Communication Protocols**: I2C for sensor and actuator control

## Getting Started
### Hardware Setup
1. **Assemble the chassis**: 3D print and attach all components as per the provided CAD files.
2. **Connect actuators and sensors**: Follow the wiring diagram.
3. **Power the system**: Use a stable power source for testing.

### Software Setup
To start using the robot, follow the steps outlined in the master’s thesis and the official guides provided by the manufacturers of the respective controllers and sensors. These documents include detailed instructions on setup, wiring, and configuration.

## Contribution
Contributions are welcome, but to ensure proper coordination, all changes must be reviewed before being merged. If you wish to improve or extend functionality:
1.**Fork the repository**
2.**Implement changes or bug fixes**
3.**Submit a pull request for review**

For major changes, please open an issue first to discuss your ideas. No changes will be merged without prior review and approval.

## License
This project is licensed under the **MIT License**, allowing for open collaboration and modifications.

## Acknowledgments
This project was initially developed as a **Master’s Thesis** at AGH University of Science and Technology.

## Contact
For inquiries, contributions, or discussions, feel free to reach out via GitHub Issues or email at **jakub.sarata@gmail.com**.

