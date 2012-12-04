import unittest
import subprocess
import os
import pitools
import math


class HAtomTestCase(unittest.TestCase):
    def setUp(self):
        os.chdir("hatom")
        out = file("pi.log", "w")
        process = subprocess.Popen("pi3D", stdout=subprocess.PIPE,
            stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        process.wait()
        self.h5file = pitools.openFile()
        self.kT = 0.0316682 * 27.211

    def tearDown(self):
        self.h5file.close()
        os.chdir("..")

    def test_energy(self):
        energy = self.h5file.getScalar("thermo_energy")
        e, de = energy.getAverage()
        expect = -13.6 + 1.5*self.kT, 0.60
        self.assertAlmostEqual(e, expect[0], delta=1.2, msg=
            'wrong total energy, expected %f but got %f' % (expect[0], e))
        self.assertAlmostEqual(de, expect[1], delta=0.2, msg=
            'wrong error for energy, expected %f but got %f' % (expect[1], de))

    def test_virial_energy(self):
        energy = self.h5file.getScalar("virial_energy")
        e, de = energy.getAverage()
        kT = 0.0316682 * 27.211
        expect = -13.6 + 1.5*self.kT, 0.16
        self.assertAlmostEqual(e, expect[0], delta=0.3, msg=
            'wrong total virial energy, expected %f but got %f'
            % (expect[0], e))
        self.assertAlmostEqual(de, expect[1], delta=0.05, msg=
            'wrong error for virial energy, expected %f but got %f' 
            % (expect[1], de))

