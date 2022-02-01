#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ET import ET
from roboticstoolbox.robot.ERobot import ERobot
from roboticstoolbox.robot.ELink import ELink


class Panda(ERobot):
    """
    Create model of Franka-Emika Panda manipulator

    panda = Panda() creates a robot object representing the Franka-Emika
    Panda robot arm. This robot is represented using the elementary
    transform sequence (ETS).

    ETS taken from [1] based on
    https://frankaemika.github.io/docs/control_parameters.html

    :references:
        - Kinematic Derivatives using the Elementary Transform
          Sequence, J. Haviland and P. Corke

    """

    def __init__(self):

        deg = np.pi / 180
        mm = 1e-3
        tool_offset = (103) * mm

        l0 = ELink(ET.tz(0.333) * ET.Rz(), name="link0", parent=None)

        l1 = ELink(ET.Rx(-90 * deg) * ET.Rz(), name="link1", parent=l0)

        l2 = ELink(ET.Rx(90 * deg) * ET.tz(0.316) * ET.Rz(), name="link2", parent=l1)

        l3 = ELink(ET.tx(0.0825) * ET.Rx(90, "deg") * ET.Rz(), name="link3", parent=l2)

        l4 = ELink(
            ET.tx(-0.0825) * ET.Rx(-90, "deg") * ET.tz(0.384) * ET.Rz(),
            name="link4",
            parent=l3,
        )

        l5 = ELink(ET.Rx(90, "deg") * ET.Rz(), name="link5", parent=l4)

        l6 = ELink(
            ET.tx(0.088) * ET.Rx(90, "deg") * ET.tz(0.107) * ET.Rz(),
            name="link6",
            parent=l5,
        )

        ee = ELink(ET.tz(tool_offset) * ET.Rz(-np.pi / 4), name="ee", parent=l6)

        elinks = [l0, l1, l2, l3, l4, l5, l6, ee]

        super(Panda, self).__init__(elinks, name="Panda", manufacturer="Franka Emika")

        self.qr = np.array([0, -0.3, 0, -2.2, 0, 2.0, np.pi / 4])
        self.qz = np.zeros(7)

        self.logconfiguration("qr", self.qr)
        self.logconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover

    robot = Panda()
    print(robot)
