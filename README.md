Markov Baby Name Generator
--------------------------

Writeup at http://alexeymk.com/2012/07/15/weekend-hack--a-markov-baby-name-generator.html

Looking for a baby name? Want something unique but sounding 'about right'? Let [http://en.wikipedia.org/wiki/Markov_chain](Uncle Markov) help.

Credit where due: Zach's PulakYelling for the heroku worker/twitter intergration
https://github.com/zwass/PULAK-YELLING

Ideas for what to do
--------------------
(Chris Wiggins:) 

1) combine with stats on name popularity if name turns out to be real

data available via

http://www.ssa.gov/oact/babynames/limits.html

among other places

2) use that set to compute how often (if ever) a markov name is observed. i assume for small ones its more common.

census would give a lot more data. plus you could generate markov data from differnet years.

also could use realistic distribution(s) of name lengths. just an idea
