import pytest
import ast
import importlib
from memory import Memory
from disk_space import DiskSpace

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to create a Computer object and check get_info output
def test_computer_get_info():
    from assignment import Computer
    from memory import Memory
    from disk_space import DiskSpace
    import re

    mem_obj = Memory()
    disk_space_obj = DiskSpace()
    computer = Computer("TestMachine", mem_obj, disk_space_obj)
    
    info = computer.get_info()
    pattern = r"\[\w+.\w+\]: computer name: TestMachine, available memory: \w+.\w+, available storage: \w+.\w+"
    assert re.match(pattern, info), "DMACC Student, the get_info method does not return the expected string format."

# Test to run main and check for 3 printed outputs
def test_main_output(monkeypatch, capsys):
    from assignment import main

    def mock_memory():
        return Memory()

    def mock_disk_space():
        return DiskSpace()

    monkeypatch.setattr('assignment.Memory', mock_memory)
    monkeypatch.setattr('assignment.DiskSpace', mock_disk_space)

    main()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert len(output_lines) == 3, "DMACC Student, the main function does not print 3 outputs."

if __name__ == "__main__":
    pytest.main()