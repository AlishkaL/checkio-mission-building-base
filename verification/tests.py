init_code = """
if not "Building" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Building'?")

Building = USER_GLOBAL['Building']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=0, middle_code="\n", show_code=None):
    if show_code is None:
        show_code = middle_code + test
    if not test:
        return_code = run_test.format(answer)
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code,
                          "python-27": init_code + middle_code + return_code},
            "show": {"python-3": show_code,
                     "python-27": show_code},
            "answer": answer}

TESTS = {
    "1. Init": [
        prepare_test(middle_code="Building(1, 1, 2, 2)"),
        prepare_test(middle_code="Building(1, 1, 2, 2, 10)"),
        prepare_test(middle_code="Building(0.54345, 1.12313, 2./6, 3.3 * 5, 1./2)")
    ],
    "2. Str": [
        prepare_test("str(Building(1, 1, 2, 2))",
                     "Building at [1, 1]. Size 2 by 2. Height 10.",),
        prepare_test("str(Building(0.2, 1, 2, 2.2, 3.5))",
                     "Building at [0.2, 1]. Size 2 by 2.2. Height 3.5.",),
    ]

}
