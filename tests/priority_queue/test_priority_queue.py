# from ting_file_management.priority_queue import PriorityQueue
import pytest
from ting_file_management.priority_queue import PriorityQueue

def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    pq = PriorityQueue()
    pq.enqueue({"qtd_linhas": 10})
    pq.enqueue({"qtd_linhas": 1})
    assert len(pq) == 2

    assert pq.search(0) == {"qtd_linhas": 1}
    assert pq.search(1) == {"qtd_linhas": 10}

    assert pq.dequeue() == {"qtd_linhas": 10}
    assert len(pq) == 1

    with pytest.raises(IndexError):
        pq.search(1)
