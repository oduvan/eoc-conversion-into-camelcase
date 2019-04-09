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
            "input": "my_function_name",
            "answer": "MyFunctionName"
        },
        {
            "input": "i_phone",
            "answer": "IPhone"
        }
    ],
    "Extra": [
        {
            "input": "this_function_is_empty",
            "answer": "ThisFunctionIsEmpty"
        },
        {
            "input": "name",
            "answer": "Name"
        },
	{
            "input": "this_is_really_very_long_string",
            "answer": "ThisIsReallyVeryLongString"
        }
    ]
}
