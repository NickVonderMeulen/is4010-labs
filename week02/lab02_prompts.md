# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI. I verified that it was installed with version 1.0.82.

### Antigravity CLI

I installed and authenticated Antigravity CLI. I verified that it was installed with version 1.1.25 and used Gemini 3.8 Flash.

## Shared task

### Shared prompt

```text
Implement the count_vowels(text: str) -> int function according to this contract: Count a, e, i, o, and u without regard to case; do not count y. Explain your approach and provide the code. Do not modify any files yet.
```

### Copilot CLI observations

After pasting the prompt into the Copilot terminal, it gave me a short explanation of its approach and provided code. Its approach was simple and focused on counting the five vowels while ignoring whether the letters were uppercase or lowercase. The response did not overcomplicate the answer, and the code looked correct. I would verify that uppercase vowels are counted correctly and that the letter y is not counted.

### Antigravity CLI observations

After pasting the prompt into the Antigravity terminal, it gave me a three-step process that it used. First, it targeted the vowels without counting y. Then it normalized the cases by changing uppercase letters into lowercase for the function. Finally, it counted the total number of vowels. The code looked fairly simple and followed the required behavior. I would test it with uppercase vowels and text containing y to make sure it works correctly.

### Comparison

Both AI tools followed the same prompt and produced correct-looking approaches, but they explained their reasoning in somewhat different ways. Antigravity took a three-step approach, whereas Copilot used a much simpler explanation. Copilot basically focused on converting the text to lowercase and counting the vowels, while Antigravity explained the process of normalizing the letters before counting them. The actual code from the two tools was similar in its overall idea but different in the way the counting was written. Copilot's answer was easier for me to follow and understand because it was shorter and more direct. However, Antigravity's step-by-step explanation was also useful because it showed how the solution worked. Both approaches looked correct, so I selected the Copilot approach because it was simple and easy to understand.

## Test-guided implementation

I used browser chat to help me come up with the appropriate implementations for the make_greeting and is_even functions. For the make_greeting function, I made it return the exact required format, "Hello, NAME!", using the supplied name. For the is_even function, I used the remainder from dividing the number by 2 to determine whether it is even. For the count_vowels function, I used the result from the Copilot CLI comparison because that was the function specifically used for the CLI comparison portion of the lab. I then created all three functions in lab02.py and ran the provided tests. All of the function tests passed, which confirmed that the implementations matched the required behavior. I also checked the journal content and corrected the shared prompt formatting so that the required prompt was inside the text code block.

## Preferred tool combination

It is nice to have all of these different tools available because each one is useful for a different reason. Browser chat is good for understanding how everything works, getting a detailed explanation, or learning a new programming concept. GitHub Copilot in VS Code is useful because it is convenient and already inside the coding environment where I write code. Copilot CLI is helpful when I want an AI assistant to work with me inside the terminal and understand the project I am working on. Antigravity CLI is useful when I want another AI approach to compare with Copilot. My preferred combination is browser chat for learning and explanations, VS Code Copilot for help while writing code, and the CLI tools when I want to compare different AI solutions. My preference could change depending on the project and which tool provides the clearest or most useful solution.
