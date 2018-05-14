"""
Pytoshop
---
Paint-like/photoshop-like tool, allowing people to draw, add
filters and do all kinds of modifications to their images.

This project was developed as part of a California State University of
Monterey Bay project for the CST205 course.
"""

__author__ = "Pernille Dahl, Joey Thomas, Marc Villain, Sam Westigard"
__copyright__ = "Copyright 2018, Pytoshop Team"
__date__ = "05-14-2018"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Production"

from pytoshop import pytoshop
from pytoshop.pytoshop import Pytoshop

if __name__ == "__main__":
    app = Pytoshop()
    app.new()
