import logging
import unittest

logging.basicConfig(filename='test_portchannel.log', filemode='w', level=logging.DEBUG,
                    format="[%(asctime)s] [%(module)-14.14s] [%(levelname)-5.5s] %(message)s")

logging.info("Running tests...")

suite = unittest.TestLoader().discover('tests.test_portchannel', 'test_portchannel*.py')
unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)