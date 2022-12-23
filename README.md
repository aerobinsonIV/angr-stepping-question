### This is a minimum reproducable example for a StackOverflow question I asked about angr.

https://stackoverflow.com/questions/74896469/step-to-a-specific-address-in-angr

Walkthrough of the program:
- Binary asks user to enter "abcd"
- If user enters "abcd", binary continues running
- Binary asks user to enter "efgh"
- If user gets it right, they win

- User can optionally specify an input file to use for the first entry by providing an argument to the binary: `./binary ./input.txt`. So if input.txt contains "abcd", it will skip to the second prompt.

Imagine this is a CTF challenge where we already know the answer to the first prompt, and we're trying to use angr to figure out the "efgh" string for the second prompt. We want to run it with the input file, and start exploring with symbolic execution only *after* we've passed the code for the first prompt.