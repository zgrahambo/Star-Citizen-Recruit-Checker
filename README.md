# Star-Citizen-Recruit-Checker
Just a little project I worked on to create a small webcrawler that fetches data from Star Citizen website profile page by logging you in.  

Specifically, it asks you to login to robertsspaceindustries.com and then it retrieves your prospects and recruits for you, if you have any..

Makes use of the requests library (found at http://docs.python-requests.org/) and regular expressions to search through HTML code to find
certain code that holds the name of your recruits.

Note: Star Citizen/Robert Space Industries has no public API so I was forced to do it this way.
