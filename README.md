# logfile-analyzer

A simple Python log analyzer that reads log files and generates useful statistics like:
- Email frequency by sender
- Most frequent sender

This project is built using only Python fundamentals (files, strings, lists, dictionaries, loops, and error handling).


The analyzer looks for lines that start with:

From someone@example.com Sat Jan 5 09:14:16 2008

Output example:

Email: stephen.marquard@uct.ac.za
Freq: 5

The most frequent email:
Email address: stephen.marquard@uct.ac.za Freq: 5
