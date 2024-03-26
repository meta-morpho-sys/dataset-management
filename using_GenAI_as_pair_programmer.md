# Pair programming with ChatGPT and GitHub Copilot

## This is a blog post about how I used GenAI tools as pair programmers to write a Data Transformation utility in Python. 
### I had a great experience and fun using ChatGPT and GitHub Copilot to help me write the code, and I'm excited to share my process and results with you.

### Introduction
Pair programming is a software development technique where two programmers work together on the same codebase. It's a great way to improve code quality, catch mistakes early, share knowledge, and learn from each other. 

Recently, I went through a GenAI tools training: https://www.linkedin.com/learning/paths/globallogic-generative-ai-assisted-programming-basics and I wanted to try out the tools I learned about in the courses.


### The Problem
It was a personal project, based on a real-life problem, where I was working with a dataset from the finance sector. 
The dataset needed some preprocessing before it could be used for forecasting. 
It contained dirty data - missing values, inconsistencies, columns that needed to be transformed as well as rows that needed to be deduplicated after the data had been cleaned and transformed. 
The data cleaning and transformation process was time-consuming and error-prone, and I wanted to automate it to save time and reduce the risk of mistakes.
To automate this process I used Python and the Python Pandas - a powerful data manipulation library, which I had a rough idea of how to use and some previous experience. 


### Pair Programming with ChatGPT
I started by creating a new Python script and opening ChatGPT in my browser. 
I explained the problem to ChatGPT and asked for help writing the code. 
ChatGPT generated some initial code snippets for me, which I used as a starting point. I iterated on these snippets, refining them and adding more functionality as needed.
The more complex the problem, the more explanation I had to provide to ChatGPT. As ChatGPT was providing solutions, I was able to ask it to explain the code to me, which helped me understand the logic behind it.
I then used my knowledge of Python and my experience in programming to refine the code and, most importantly, to catch any errors that ChatGPT introduced.


### Pair Programming with GitHub Copilot
While ChatGPT was helpful, it was a bit uncomfortable to switch back and forth between the browser and my IDE. I wanted a more integrated experience. Here is where GitHub Copilot came in.
I installed the Copilot extension in my JetBrains IDE and started writing code. 
Copilot provided helpful suggestions and completed my code as I typed. It was like having an AI pair programmer sitting next to me, ready to help at any time.
Github Copilot could read the context of the entire codebase, which had grown by this time, and provide more accurate suggestions.
I used Copilot to refactor some of the code. It suggested more efficient ways to write certain functions however they became more complex and harder to understand.

### Learning while Pair Programming
Another useful feature of Copilot, as well as that of ChatGPT, was that I could use them to explain the most difficult and complex parts of the code to me. 
This helped me understand the code better and learn more about Pandas and Python in the process.

### The Result
After about 3 days of pair programming with ChatGPT and GitHub Copilot, I had a fully functional data transformation utility written in Python with some tests. 
The script cleaned up the dataset, filled in missing values, transformed the columns and compacted the rows as needed. 
I was impressed by how quickly I was able to write the code with the help of these AI tools.
I must highlight, though, that my intervention as a human programmer was crucial. GenAI tools can't replace a reasoning human mind, they can only assist it. 

You can find the code in my GitHub repository [here](https://github.com/meta-morpho-sys/dataset-management).
I would love my more experienced in Python and Pandas colleagues to review the code and give me their feedback.
This brings me to the next point.

### Caveats and things to consider
- The tools are trained on a large dataset of code, but there is a time cutoff for the training data (up to April 2023 for GPT-4), so they may not always generate the most up-to-date or idiomatic code.
- GitHub Copilot is built on top of OpenAI Codex which is trained on a selection of the English language, public GitHub repositories, and other publicly available source code. The Copilot Chat experience was recently upgraded bringing more accurate and useful code suggestions with OpenAI's GPT–4. 
- While pair programming with AI tools was a great experience overall, there were some limitations:
  - ChatGPT sometimes generated code that didn't work as expected, and Copilot occasionally suggested inefficient solutions.
  - It's important to review the code carefully and test it thoroughly before using it in production.
  - The tools will only give you what you ask for, no more. You need to keep refining your questions to get the desired output, but it may get messy.
- Besides the above points it is worth to notice that both tools are paid for services and require a subscription.

### Tips for Pair Programming with AI
If you're thinking about trying pair programming with AI tools, here are a few tips from my experience:
- DON'T give real data to the AI tool, it is important to preserve the privacy of your data.
- DO Clearly explain the problem to the AI tool and provide as much context and detail as possible.
- DO Give it as much context as possible or bring the tool into the context of the codebase, like you can do with GitHub Copilot.
- DO Review and make sure you fully understand the code that the GenAI tool has produced for you, iterate on the code and make changes as needed. 
- DO Remember, the GenAI tools are Large Language Models(LLMs), they work by predicting the next word based on the context of the input, so they may not always generate the most efficient or optimal code.
- And finally, the AI tools are there to help you, not replace you.

### Conclusion
These are useful tools that can help to speed up the coding process. Their strength lies in their ability to read and interpret the context.
However, they are not "thinking" tools. They can't replace human reasoning and intuition.