# New York Times Cooking Comments Analysis

## Concept
This project started with a curiosity about the comments section on New York Times Cooking. I noticed a funny duality in the commenters: on one hand, they can be **"snobby" cooks who want to show off on the internet**, but on the other hand, they form a **highly helpful "community consciousness"**. They often point out when a recipe is flawed or offer useful adaptations for different tastes. I wanted to explore this data to see if certain authors were regarded more highly than others, and if the comments could reveal anything about the community itself.

## Data Collection & Methodology
Since recipes aren't inherently tagged with categories or cuisines, I decided to pull my data based on the authors. Here is how the scraping process worked:
*   **Author Pages:** I used the NYT "About" page to find all **23 listed authors**.
*   **Recipe Links:** I scraped links for up to the **48 most recent recipes from each author's page** to get a representative sample size. 
*   **HTML Metadata:** I wrote a scraper to grab relevant metadata for each of those recipes, such as the **title, rating, and number of ratings**.
*   **The Comments API:** I found an **undocumented New York Times API** that allowed me to grab all of the comments for each recipe.

Ultimately, I merged everything into CSV files, resulting in **close to 80,000 rows of comments**, with each row containing the comment and its associated recipe metadata.

## AI Categorization
To categorize the comments, I ran the data through an LLM. Surprisingly, **defining the categories was the hardest part of the project**. 

I spent a couple of days reading comments and running tests before landing on **10 distinct categories**. The LLM struggled when I tried to add more than 10, so it was a constant **dance between accuracy and precision**. 

*Pro Tip:* Because I kept the data separated into individual CSVs by author rather than one giant file, I realized I could **run the classification simultaneously**. The whole LLM process parsed all 80,000 rows in just **about two hours and cost only $35**.

## What I Found
Honestly, the findings were a bit obvious: **the community is overwhelmingly positive and constructive**. Even when people complain or critique, it's generally because they are tweaking an already good recipe to their own liking. It turns out the New York Times writes pretty good recipes, and people genuinely like them.

## Technology
*   **Data Processing:** Python (Jupyter Notebooks) for scraping, merging CSVs, and LLM classification.
*   **Visualizations (D3.js):** I'm not a D3 expert, so I used an **LLM inside VS Code** to generate the charts based on a quick design mock-up, followed by some manual tweaking to get it just right.
*   **Site Build (Svelte):** The final site was built with Svelte so I could efficiently build and reuse components while passing in different text and data.

## Reflections & Future Ideas
A big takeaway for me was **the importance of focus**. I had a lot of ideas and ended up "hodgepodging" them all into one giant story, which made each analysis feel a bit shallow. 

If I could do it again, I would spend less time trying to cover everything and more time **digging into the individual authors**. I'd love to look closer at what comment categories each of the 23 authors gets most often, what they specialize in, and what the relationship is like between their specific style and their commenters.
