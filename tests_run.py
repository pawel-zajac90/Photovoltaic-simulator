from tests_class import *

test1 = MainTests()
test1.read_from_rabbitMQ_test()
test1.main_function_test()
test1.w_plus_pv_test()
test1. saving_test()

test2 = MeterTest()
test2.value_test()
test2.meter_test()

test3 = TimerTest()
test3.time_test()