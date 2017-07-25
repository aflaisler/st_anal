# Preliminary Proposal Specifications
## Purpose: Organize initial ideas and allow us to provide feedback!

## Format: Markdown, Text File, anything that can be opened and read in vim.


# Universal sizing

1. High level description of project <br/>
Create an application that returns the universal sizing of the clothe depending on the brand and the taxonomy

2. What question or problem are you trying to solve? <br/>
Fashion e-commerce website are more and more becoming marketplaces (with many brands).
Or, the sizing of fashion products from a brand to another can be very different.
In fact the same brand can use many different ones.
J-Crew for example, for a top, can use universal size (xs, s, etc.), US sizes (000, 00, etc.),
and inches (oh and sometimes 'Regular', 'Petite', 'Tall', etc.)

Also, sizing are not linear (US sizes grow faster than UK sizes for example) and
they vary between brands (J-Crew's XS <> RL's XS)

The solution: Create a classifier that would take the brand and taxonomy as argument
and return the sizes for the product in any type of sizing. This will allow the websites
to uniformize all his products onto one unique scale.
(This is an actual business problem that I tried to fix with Amazon ML with 50% accuracy)

3. How are you presenting work? <br/>
Slides and (ideally) an API.

4. What’s your next step towards making this your project. <br/>
Create a high level map of how it would work

5. What are your data sources? <br/>
Ex-employer (~10k observations)

##############

# RSS feed 3.0

1. High level description of project <br/>
The web 3.0 is supposed to bring custom websites for each user.
However rss feeds still aggregate the 'hot' articles depending on the crowd behavior.
The project will try to solve this.

2. What question or problem are you trying to solve? <br/>
Create a rss feed that is unique to each users depending on their behavior / on topics (inferred)

3. How are you presenting work? <br/>
Slides and web app (cf. http://skimfeed.com/)

4. What’s your next step towards making this your project. <br/>
Create a high level map of how it would work / wireframe

5. What are your data sources? <br/>
RSS feeds

##############

# Stock recovery predictor

1. High level description of project <br/>
Evaluate the regularization of a positive / negative technical comment of investors
in the tech industry

2. What question or problem are you trying to solve? <br/>
Is the recovery from a technical (wide spread) article predictable in the tech industry

3. How are you presenting work? <br/>
Ideally simple web app to tell the daily overall sentiment / company
+
Presentation - slides

4. What’s your next step towards making this your project. <br/>
I need to extract positive and negative articles about IBM (which I have
intraday data for the past 15yrs) and validate the hypothesis
=> If, interesting results (potentially needing features engineering to qualify
'healthiness' of the company)

5. What are your data sources? <br/>
http://www.kibot.com/buy.aspx
https://www.quantopian.com/
https://www.quotemedia.com/portal/quote?qm_symbol=GOOG

6. Libraries <br/>
TextBlob,
word_tokenize, wordpunct_tokenize, RegexpTokenizer (from nltk.tokenize)
CountVectorizer, TfidfVectorizer (from sklearn.feature_extraction.text)
Lemmatizers / Stemmers
preprocessing (from sklearn)
