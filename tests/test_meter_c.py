import random
from unittest.mock import Mock, patch
from photovoltanic_simulator.meter_c import Meter


class TestMeter:
    def test_generate_value(self):
        with patch ('random.randint') as mock_randint:
            mock_randint.return_value = 1234
            mock_parameters = Mock()
            result = Meter(mock_parameters).generate_value()
            assert result == 1234


    def test_connect(self):
        with patch('connection') as mock_block_connect:
            mock_queue = Mock()
            mock_block_connect = Mock()
            mock_parameters = Mock()
            mock_block_connect.channel().side_effect = True
            mock_block_connect.channel().queue_declare(queue=mock_queue).side_effect = True
            connection = Meter(mock_parameters).connect()
            assert connection == True


    def test_send(self):
        mock_message = Mock()
        mock_parameters = Mock()
        result = Meter(mock_parameters).send(mock_message)
        self.channel.basic_publish.assert_called

test = TestMeter()
test.test_send()
