import pytest

from algo_lab.stack import Stack


def test_stack_empty():
    stack = Stack()
    assert len(stack) == 0
    assert bool(stack) is False

def test_stack_push():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert len(stack) == 2

def test_stack_peek():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2

def test_stack_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.pop() == 20
    assert len(stack) == 1

def test_stack_lifo():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert len(stack) == 0

def test_stack_bool():
    stack = Stack()
    stack.push(10)
    assert bool(stack) is True
    stack.pop()
    assert bool(stack) is False

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()

def test_stack_different_types():
    stack = Stack()
    stack.push("10")
    stack.push(1.5)
    stack.push(-100)
    stack.push(True)
    stack.push([1, 2])
    assert stack.pop() == [1, 2]
    assert stack.pop() is True
    assert stack.pop() == -100
    assert stack.pop() == 1.5
    assert stack.pop() == "10"




    
