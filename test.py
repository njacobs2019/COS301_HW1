import io
import sys
import calc

def test_input(sentence):
    # Create an in-memory file object to capture standard output
    output = io.StringIO()

    # Redirect standard output to the in-memory file object
    sys.stdout = output

    # Call the function with the desired input
    calc.yacc.parse(sentence)

    # Restore standard output
    sys.stdout = sys.__stdout__

    # Get the captured output as a string
    output_str = output.getvalue()
    return output_str.strip()

with open('test_cases.txt') as f:
    tests = f.readlines()

# Remove newlines in the file
for i in range(len(tests)):
    tests[i] = tests[i].strip()

i=0  # index into sample_out
while(i < len(tests)):
    case = tests[i]
    if case[0]=="#":
        # This is a comment in the input file
        case = case.replace("#","")
        case = case.strip()
        print(f"***{case}***")
        i+=1
    else:
        # This is a test case
        if(i+2>=len(tests)):
            break
        
        question = tests[i+1]
        answer = tests[i+2]

        print("-"*20)
        print(f"Running case: {question}")
        print(f"Expected output: {answer}")
        output = test_input(question)
        print(f"Actual output:  {output}")
        if output==answer:
            print("Status:  Passed")
        else:
            print("Status:  FAILED")
            exit(1)
        i+=3

print("All tests passed!!")