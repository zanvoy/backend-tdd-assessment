# Assessment: Test Driven Command Line Tool Creation

For this assessment, you'll be creating a souped up version of the "echo"
command line tool:

![example output](screenshots/result.gif)

In doing so, you'll be demonstrating a basic understanding of the following:

- converting acceptance criteria into unit tests using
  [unittest](https://docs.python.org/2.7/library/unittest.html)
- employing [Test Driven Development (TDD)](https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe) to write a program that conforms to those criteria
- parsing command line argumens with [argparse](https://docs.python.org/2.7/howto/argparse.html#id1)
- commonly used [string methods](https://docs.python.org/2/library/stdtypes.html#string-methods)

## Getting Started
To get started, _fork_ this repository into your own GitHub account then clone
this repository to your local machine:

```console
foo@bar:~ $ git clone git@github.com:github-username/backend-tdd-assessment
foo@bar:~ $ cd backend-tdd-assessment
foo@bar:~/backend-tdd-assessment $
```

Note `github-username` above. In other words, __don't__ simply copy-paste the
code above blindly into a terminal. 

Next, you'll need to create a directory named `tests` with an empty
`__init__.py` file in it. You'll finally want to write a series of test modules
that include test cases for the application you're building. For a project a small as this,
it's probably sufficient to have a single test case, perhaps named `test_echo.py`.

Finally, you should create an empty python file named `echo.py` that you'll
use to write your program.

When done, you should have a project directory that looks something like this:

        .
        ├── README.md
        ├── echo.py
        ├── screenshots
        │   └── result.gif
        └── tests
            ├── __init__.py
            └── test_echo.py

Even before you write a single test, you might find it useful to start your test harness:

```bash
foo@bar:~ $ rerun "python -m unittest discover"
```

## Acceptance Criteria

### Step 1: Display Help (1 point(s))
When the user provides invalid options or supplies the `-h/--help` flag, the
program should print the following usage message:

    usage: echo.py [-h] [-u] [-l] [-t] text

    Perform transformation on input text.

    positional arguments:
        text         text to be manipulated

    optional arguments:
        -h, --help   show this help message and exit
        -u, --upper  convert text to uppercase
        -l, --lower  convert text to lowercase
        -t, --title  convert text to titlecase

The following unit test can be used to check that your program prints a properly formatted help message:

```python
def test_help(self):
    """ Running the program without arguments should show usage. """

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
    process = subprocess.Popen(
        ["python", "./echo.py", "-h"],
        stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    usage = open("./USAGE", "r").read()

    self.assertEquals(stdout, usage)
```

### Step 2: Test the `-u/--upper option` (2 point(s))
Write a unit test that asserts that `upper` get stored inside of the
namespace returned from `parser.parse_args` when either `"-u"` or `"--upper"`
arguments are passed.

It should also test that `"hello"` gets turned into `"HELLO"` when the
program is run.

### Step 3: Test the `-l/--lower option` (2 point(s))
Write a unit test that asserts that `lower` get stored inside of the
namespace returned from `parser.parse_args` when either `"-l"` or `"--lower"`
arguments are passed.

It should also test that `"Hello"` gets turned into `"hello"` when the
program is run.

### Step 4: Test the `-t/--title option` (2 point(s))
Write a unit test that asserts that `title` get stored inside of the
namespace returned from `parser.parse_args` when either `"-t"` or `"--title"`
arguments are passed.

It should also test that `"hello"` gets turned into `"Hello"` when the
program is run.

### Step 5: Test for no arguments (2 point(s))
Write a unit test that asserts that when no arguments are given, the program
returns the input text unscathed.

### Step 6: Implement he program (2 points)
Now that your tests are complete, implement the program so that the above
tests pass.

## Submission

Submit a link to your GitHub repository to Canvas.