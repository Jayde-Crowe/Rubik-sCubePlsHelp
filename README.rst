============
Rubik's Cube
============

A Rubik's Cube is a 3-dimensional puzzle invented in 1974 by Ernő Rubik. The
cube comprises 26 miniature cubes (also known as "cubies" or "cubelets") where
the visible face(s) of each miniature cube is a different color and each face
of the cube may be rotated independently of the others. When solved, each face
of the cube must have only a single color.

Learning Objectives
===================

Implement software by following a *specification*

* Analyze requirements for a software system
* Develop code that adheres to a specified design
* Use *test-driven development (TDD)* to emphasize simple design and software
  quality

Help Policy
===========

Authorized Resources
  Any, except others' code

Notes
  Never copy another person's work and submit it as your own

  Do not jointly work on this assignment, but you may ask classmates syntax
  questions

  You must document all help received from all sources, including the
  instructor and instructor-provided material (including the textbook),
  *except* for the following:

  * Resources related to syntax *unless* the resource is a classmate (i.e.,
    document any interactions you have with classmates)

Instructions
============

Implement the specification_ for representing and visualizing a Rubik's cube.
Template code is provided to ease the implementation of classes in Python.

.. _specification: docs/specification.md

Test code is provided to facilitate automated testing. Do **not** modify the
test code! A correct implementation of the specification should pass all the
automated tests.

Testing
-------

To test your implementation locally, install all the Python packages listed in
``test-requirements.txt``. Installation and testing instructions vary depending
on your environment.

Thonny configuration (tested with Thonny 3.3.13):

1. Install each package using Thonny's package manager: Tools > Manage
   packages...
2. Click the run button when viewing ``test_rubik.py`` to execute the unit
   *and* integration tests
3. Install the `thonny-flake` plugin using Thonny's package manager: Tools >
   Manage plug-ins...
4. Run Flake8_ by entering `!flake8` in Thonny's shell

.. _Flake8: https://flake8.pycqa.org/

Submission
==========

Create an archive of your Git repository (you can use GitHub's "Clone or
download" button when viewing your repository for this purpose) and submit that
archive. Be sure to include your documentation statement as part of the
submission.

GitHub Classroom also tags the latest commit at the due date for the
assignment.

Grading
-------

The following grading rubric will be used for this assignment:

+---------------------------------------+-----------------+
|                                       |     Points      |
+---------------------------------------+--------+--------+
| Description                           |  Total | Earned |
+=======================================+========+========+
| Unit Tests (16 @ 2 points each)       |     32 |        |
+---------------------------------------+--------+--------+
| Integration Tests (6 @ 6 points each) |     36 |        |
+---------------------------------------+--------+--------+
| PEP 8 compliance                      |      7 |        |
+---------------------------------------+--------+--------+

No partial credit will be awarded for individual tests, including PEP 8
compliance, unless you can prove that a test case is invalid (e.g., violates
the specification).

.. hint::
    Many of the unit tests can be passed by doing nothing more than defining
    the method being tested. Although receiving full credit requires
    implementing each method correctly, you should start by guaranteeing
    partial credit (i.e., defining all the methods) and then work on
    implementing each correctly.

Automated Tests
---------------

GitHub Actions tests your code *when you push your changes to GitHub (i.e.,
continuous integration (CI))*. The entire class shares the resources provided
for auto-grading; more specifically, there is a maximum number of minutes per
month for GitHub Actions, and each job counts toward that maximum. You should
test locally *before* pushing to GitHub.

To encourage judicious use of shared resources, a penalty may be applied to
deter running an excessive number of jobs that don't pass the tests. You may
check the number of workflow runs by clicking on the "Actions" tab of your
repository.
