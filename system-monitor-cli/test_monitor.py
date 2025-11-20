import unittest
from unittest.mock import patch,MagicMock

from monitor import display_processes

MOCK_PROCESS_DATA =[
     {'pid': 103, 'name': 'Process_C', 'cpu_percent': 8.0, 'memory_percent': 2.0},
    # A: Mid-CPU (5.5), Mid-Memory (10.0)
    {'pid': 101, 'name': 'Process_A', 'cpu_percent': 5.5, 'memory_percent': 10.0},
    # D: Low-CPU (2.5), Mid-High Memory (25.0)
    {'pid': 104, 'name': 'Process_D', 'cpu_percent': 2.5, 'memory_percent': 25.0},
    # B: Worst CPU (1.0), Best Memory (50.0)
    {'pid': 102, 'name': 'Process_B', 'cpu_percent': 1.0, 'memory_percent': 50.0},
    # Idle/Filtered process (should be ignored by the function)
    {'pid': 105, 'name': 'Process_Idle', 'cpu_percent': 0.0, 'memory_percent': 0.0},

]

class TestProcessSorting(unittest.TestCase):

    @patch('monitor.psutil.process_iter')
    @patch('monitor.print')
    def test_cpu_sort(self,mock_print,mock_process_iter):

        mock_process_iter.return_value = [MagicMock(info=data) for data in MOCK_PROCESS_DATA]

        sorted_list=display_processes(sort_key='cpu', limit=4)

        self.assertEqual(sorted_list[0]['name'], 'Process_C', "Highest CPU process not first")
        self.assertEqual(sorted_list[3]['name'], 'Process_B', "Lowest CPU process not last")

    @patch('monitor.psutil.process_iter')
    @patch('monitor.print')
    def test_memory_sort(self,mock_print,mock_process_iter):

        mock_process_iter.return_value = [MagicMock(info=data) for data in MOCK_PROCESS_DATA]

        sorted_list = display_processes(sort_key='memory', limit =4)
        
        self.assertEqual(sorted_list[0]['name'], 'Process_B', "Highest Memory process not first")
        self.assertEqual(sorted_list[3]['name'], 'Process_C', "Lowest Memory process not last")

    @patch('monitor.psutil.process_iter')
    @patch('monitor.print')
    def test_idle_processing_filtering(self,mock_print,mock_process_iter):

        test_data = [
            {'pid': 200, 'name': 'Active', 'cpu_percent':1.0, 'memory_percent':1.0},
            {'pid': 201, 'name': 'Idle', 'cpu_percent':0.0, 'memory_percent':0.0},
        ]        

        mock_process_iter.return_value = [MagicMock(info=data) for data in test_data]

        sorted_list = display_processes(sort_key='cpu', limit=2)

        self.assertEqual(len(sorted_list),1,"Idle process was not correctly filtered out")
        self.assertEqual(sorted_list[0]['name'],'Active')

if __name__ == '__main__':

    unittest.main(argv=['first-arg-is-ignored'], exit=False)        