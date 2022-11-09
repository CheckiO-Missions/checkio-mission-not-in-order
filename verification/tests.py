"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 1, 4, 2, 1, 3]],
            "answer": 3,
        },
        {
            "input": [[]],
            "answer": 0,
        },
        {
            "input": [[1, 1, 1, 1, 1]],
            "answer": 0,
        },
        {
            "input": [[1, 2, 3, 4, 5]],
            "answer": 0,
        },
    ],
    "Extra": [
        {
            "input": [[6, 5, 4, 3, 2, 1]],
            "answer": 6,
        },
        {
            "input": [[5, 4, 3, 2, 1]],
            "answer": 4,
        }, 
        {
            "input": [[1, 3, 2, 4, 3, 5, 4, 6]],
            "answer": 6,
        }, 
        {
            "input": [[1, 2, 3, 2, 1]],
            "answer": 3,
        }, 
        {
            "input": [[1, 1, 1, 100, 1, 1, 1]],
            "answer": 2,
        },
        {
            "input": [[1, 3, 2]],
            "answer": 2,
        },
    ]
}
