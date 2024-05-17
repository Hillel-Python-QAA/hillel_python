from abc import ABC, abstractmethod


class TestABC(ABC):
    @abstractmethod
    def setup(self):
        """
        Method for test preparation
        :return:
        """
        pass

    @abstractmethod
    def executor(self):
        """
        Method for test execution
        :return:
        """
        pass

    @abstractmethod
    def teardown(self):
        """
        Method for cleaning after test
        :return:
        """
        pass


class RealTest(TestABC):
    def setup(self):
        print("Preparing for testing")

    def executor(self):
        print("Executing the test")

    def teardown(self):
        print("Cleaning")


RealTest().executor()

