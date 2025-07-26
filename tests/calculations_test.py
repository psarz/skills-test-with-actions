# System Modules
import sys
import os
import pytest

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

# System Modules

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

def test_area_of_circle_negative_radius():
    """Test with a negative radius."""
    # Arrange
    radius = -1

    # Act & Assert 
    with pytest.raises(ValueError) as exc_info:
        area_of_circle(radius)
    assert str(exc_info.value) == "Radius cannot be negative"

def test_area_of_circle_zero():
    """Test with radius=0."""
    # Arrange
    radius = 0
    
    # Act
    result = area_of_circle(radius)
    
    # Assert
    assert result == 0

def test_area_of_circle_positive():
    """Test with positive radius."""
    # Arrange
    radius = 2
    
    # Act
    result = area_of_circle(radius)
    
    # Assert
    assert result == pytest.approx(12.566370614359172)

def test_get_nth_fibonacci_negative():
    """Test with negative n."""
    # Arrange
    n = -1

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        get_nth_fibonacci(n)
    assert str(exc_info.value) == "n cannot be negative"

def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0
    
    # Act
    result = get_nth_fibonacci(n)
    
    # Assert
    assert result == 0

def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1
    
    # Act
    result = get_nth_fibonacci(n)
    
    # Assert
    assert result == 1

def test_get_nth_fibonacci_two():
    """Test with n=2."""
    # Arrange
    n = 2
    
    # Act
    result = get_nth_fibonacci(n)
    
    # Assert
    assert result == 1

def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10
    
    # Act
    result = get_nth_fibonacci(n)
    
    # Assert
    assert result == 55
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
 """Test with n=10."""
 # Arrange
 n = 10

 # Act
 result = get_nth_fibonacci(n)

 # Assert
 assert result == 55