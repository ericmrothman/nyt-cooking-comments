<script>
    import Recipe from './lib/Recipe.svelte';
    import Comment from './lib/Comment.svelte';
    import CommentChart from './assets/comment_totals_by_category_001.png';
    import CommentChart2 from './assets/comment_totals_by_category_002.png';
    import AuthorChartTotal from './assets/author_bar_chart_totalComments.png';
    import AuthorChartChanges from './assets/author_bar_chart_positive_user_describing_changes.png';
    import AuthorChartWritten from './assets/author_bar_chart_positive_user_made_as_written.png';
    import RollsImg from './assets/rolls.jpg';

    import SentimentCluster from './lib/SentimentCluster.svelte';
    import RecipeCluster from './lib/RecipeCluster.svelte';
    import AuthorBarChart from './lib/AuthorBarChart.svelte';

    
    const TSGDrecipeAuthors = '<span class="underline">Bert Greene</span> and <span class="underline">Denis Vaughan</span>';
    const TSGDadaptedBy = '<span class="underline">Sam Sifton</span>';
    const TSGDingredients = [
        '1 (2-ounce) can <span class="highlight">flat anchovy fillets</span> packed in oil',
        '½ cup chopped fresh parsley',
        '2 tablespoons red wine vinegar',
        '2 tablespoons chopped fresh chives or shallots',
        '1 tablespoon drained capers, rinsed',
        '1 ½ cups mayonnaise',
        'Freshly ground black pepper, to taste',
        'Chilled sliced vegetables, for serving'
    ];

    const BananarecipeAuthors = '<span class="underline">Sohla El-Waylly</span>';
    const BananaIngredients = [
        '2 ripe medium bananas (about 240 grams peeled)',
        '2 large eggs',
        '6 tablespoons/90 milliliters olive oil, plus more for greasing the pan',
        '¾ cup/187 grams peanut or almond butter',
        '6 tablespoons/120 grams honey',
        '2 teaspoons kosher salt (such as Diamond Crystal), or 1 teaspoon fine salt',
        '2 teaspoons ground cinnamon',
        '2 teaspoons pure vanilla extract',
        '1 cup/100 grams old-fashioned rolled oats',
        '¾ cup/80 grams walnut halves and pieces, roughly chopped',
        'Flaky salt, for topping'
    ];
    
</script>

<main>
    <header class="hero">
        <h1>
            <span>Active</span><br/>
            <span>Ingredients</span>
        </h1>
        <h2 class="subtitle">Exploring The Secret World<br>of Recipe Comments</h2>
        
        <div class="byline">
            <p>by: eric rothman</p>
            <p>july, 2026</p>
        </div>
    </header>
    
    <section class="quote-section">
        <blockquote>
            <p>"There is no recipe for living that suits all cases."</p>
            <cite>-Carl Jung</cite>
        </blockquote>
    </section>
    
    <section class="transition-section">
        <p>If you've ever prepared a dish from New York Times Cooking, you'll know the ingredients and instructions are only part of the story.</p>
    </section>

    <section class="recipe-section">
        <Recipe 
            title="THE STORE'S GREEN DIP"
            authors={TSGDrecipeAuthors}
            adaptedBy={TSGDadaptedBy}
            date="August 31, 2019"
            yieldAmount="2 cups"
            ingredients={TSGDingredients}
        />
    </section>
    
    <section class="transition-section">
        <p>The rest of the story gets told in the comments:</p>
    </section>
    
    <section class="comments-section">
        <h2 class="comments-header">COMMENTS <span class="count">(168)</span></h2>
        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="25021825"
                    text="To all the cooks who want to substitute or eliminate the anchovies: DO NOT make this dip. The anchovies in this recipe don't taste fishy. They are the secret Unami bomb that makes this dip so incredibly tangy and delicious."
                    upvotes="268"
                    colorVariant="green"
                    rotation={-5}
                />
            </div>
            
            <div class="comment-wrapper pos-2">
                <Comment 
                    userId="189864493"
                    text="2/3 guests i had literally spat out and one threw up at the intense anchovy taste. Whoever said you can't taste it has to be lying. It might be the worst recipe I made in the NYT."
                    upvotes="7"
                    colorVariant="red"
                    rotation={12}
                />
            </div>
        </div>
    </section>

    <section class="transition-section">
        <p>By leaving comments, readers share personal thoughts, feelings, and experiences with preparing a dish. They detail clever modifications to accommodate ingredients on hand, allergies, or picky eaters. They ask questions, debate authenticity. If a recipe is a hit, they will tell you so. If not, they will tell you that too.</p>

        <p>Taken as a whole, comments provide a kind of amorphous community consciousness about a recipe. The comments for <a href="https://cooking.nytimes.com/recipes/1020427-the-stores-green-dip">The Store's Green Dip</a> recipe, for example, ask you to think long and hard about your personal feelings for anchovies.</p>

    </section>

    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="53727906"
                    text="I firmly believe that the use of higher quality anchovies is key here. There is a huge difference in taste. One of the best brands is &quot;Anchovies de L'Escala&quot; in olive oil, from Spain. They’re hand-packed in jars, with excellent, meaty, filets, not at all fishy tasting. Overall, excellent recipe."
                    upvotes="3"
                    colorVariant="green"
                    rotation={-5}
                />
            </div>
            
            <div class="comment-wrapper pos-2">
                <Comment 
                    userId="45777496"
                    text="Mayonnaise repulses me. Is avocado fat enough to be a sub? Avocado and yogurt?"
                    upvotes="1"
                    colorVariant="blue"
                    rotation={12}
                />
            </div>
        </div>
    </section>

    <section class="transition-section">
        <p>I wanted to see what we might uncover by studying these comments. What sorts of fun stories might be lurking? What can we learn about recipe authors? The community? The nature of recipes themselves?</p>

        <p>To get a representative sample of comments to analyze, I looked at the Times' 23 cooking writers listed on their "About Us" page. For each author, I downloaded comments from up to 48 of their most recent recipes, building a dataset of 76,721 individual comments. Then, I used an LLM to classify each comment according to a handful of categories. Here's what I found:</p>
    </section>

    <h3>1. Most comments are positive and constructive</h3>

    <section class="transition-section">
        <p>Despite comments sections having a reputation for harboring squabblers and haters, 59% of all NYT recipe comments are positive. Sentiment-neutral comments, which include clarifying questions and off-topic discussions, took second place, representing 22% of the total. Comments that were critical or found the recipe flawed in some significant way made up a mere 19%:</p>
    </section>

    <section class="chart-img">
        <img src={CommentChart} alt="collections of hundreds of little bubbles representing comments from the nyt cooking recipe readers.">
    </section>

    <section class="transition-section">
        <p>The single largest blob of comments came from users who had made the recipe, liked it, and wanted to share how they tweaked it to suit their personal tastes:</p>
    </section>
    
    <section class="chart-img">
        <img src={CommentChart2} alt="collections of hundreds of little bubbles representing comments from the nyt cooking recipe readers.">
    </section> 

    <section class="transition-section">        
        <p>Here’s one such comment detailing how a reader adapted <a href="https://cooking.nytimes.com/recipes/1025325-creamy-spicy-tomato-beans-and-greens">Creamy, Spicy Tomato Beans and Greens by Alexa Weibel</a> to be vegan:</p>
    </section>

    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="87430575"
                    text="To make this vegan: I used a can of coconut cream instead of cow cream & added about a teaspoon of whole grain mustard and a tablespoon of nutritional yeast to the beans. I added about a teaspoon each of nutritional yeast & paprika to the bread crumbs & mixed the arugula with a good glug of the sundried tomato’s oil. Devine! Bright! Rich! Will be a staple!"
                    upvotes="2023"
                    colorVariant="green"
                    rotation={-5}
                />
            </div>
        </div>
    </section>

    <section class="transition-section">
        <p>Another tells the story of a slight tweak to <a href="https://cooking.nytimes.com/recipes/1017724-cheesy-hasselback-potato-gratin">Cheesy Hasselback Potato Gratin</a>, from J. Kenji López-Alt and adapted by Emily Weinstein—which scored serious points:</p>
    </section>

    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="9272719"
                    text="I made this dish for Thanksgiving with sweet potatoes (not yams) to wild success. My family practically hoisted me upon their shoulders. When I called my mother a week later, she answered the phone without a hello: &quot;Those sweet potatoes were the best thing I've ever eaten.&quot; I said, &quot;Hi, Mom. How's everything?&quot; She said, &quot;God, those sweet potatoes were good.&quot; I give my full throated endorsement for this recipe. It can make you feel like a conquering hero."
                    upvotes="1311"
                    colorVariant="green"
                    rotation={5}
                />
            </div>
        </div>
    </section>

    <h3>2. Constructive comments have the most upvotes</h3>

    <section class="transition-section">
        <p>Not only are positive tweaks to recipes the most numerous type of comment, they are also deemed the most helpful by fellow readers. Of the 100 most-upvoted comments across all the recipes I gathered, 58 came from users who liked the recipe but tweaked it. Only 3 of the top 100 comments indicated they prepared the recipe exactly as written.</p>
    </section>

    <section class="transition-section">
        <p>Explore the most upvoted 100 comments from the dataset below:</p>
    </section>

    <section class="chart-section">
        <SentimentCluster />
    </section>

    <section class="transition-section">
        <p>Oddly enough, the single most upvoted comment in the dataset (2,513 upvotes!) came from a user who seemingly prepared the recipe to a tee:</p>
    </section>

    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="77885759"
                    text="I got drunk and made this when my fiancee wasn't home and got all these stains on my undershirt when I ate it (I spilled on myself) and it was so good and I don't even care."
                    upvotes="2513"
                    colorVariant="green"
                    rotation={-3}
                />
            </div>
        </div>
    </section>

    <h3>3. Serial haters are relatively rare</h3>

    <section class="transition-section">
        <p>Of the 54,886 unique commenters in the dataset, about 17% (9,667 users) had a comment history containing more negative comments than positive ones. 17% might sound like a large proportion of haters, but as it turns out, most of this subset have only commented once.</p>

        <p>If you look at the core community–the 16,500 active users who left at least two comments–persistent complainers are rare. Only 1,380 active commenters are predominantly negative. That means true haters make up just 2.5% of the total community.</p>

        <p>User #193908654 is one such hater. A specimen:</p>
    </section>

    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="193908654"
                    text="The sauce seriously overpowers the flavor of the asparagus and is much too heavy for this delicate and wonderful vegetable. The dill is optional, fortunately; dill does not complement asparagus at all. Nothing is better than asparagus, butter, and a bit of salt."
                    upvotes="103"
                    colorVariant="red"
                    rotation={4}
                />
            </div>
        </div>
    </section>

    <section class="transition-section">
        <p>Despite disliking almost every recipe they review, this user ranks in the top 0.03% of most-upvoted commenters. The community clearly craves their specific flavor of constructive criticism.</p>
    </section>

    <h3>4. Authors get different amounts and kinds of comments</h3>

    
    <section class="chart-section" style="margin-top: 2rem;">
        <h4 class="chartTopper">Which author gets the most comments?</h4>
        <p class="chart-subtitle">Total number of comments per 48 recipes, broken down by author</p>
        <img src={AuthorChartTotal} alt="Author Bar Chart Total Comments">

    </section>

    <section class="transition-section" style="margin-top: 4rem;">
        <p>Sam Sifton is known for his <a href="https://cooking.nytimes.com/68861692-nyt-cooking/14326423-no-recipe-recipes">no-recipe recipes</a>, which encourage cooks to improvise. Perhaps as a result, his recipes generate the most discussion.</p>
    </section>

    
    <section class="chart-section" style="margin-top: 2rem;">
        <h4 class="chartTopper">Which author gets the most tweaks?</h4>
        <p class="chart-subtitle">Percentage of positive comments suggesting tweaks, grouped by recipe author</p>
        <img src={AuthorChartChanges} alt="Author Bar Chart Positive User Describing Changes">

    </section>

    <section class="transition-section" style="margin-top: 4rem;">
        <p>Claire Saffitz finds herself at the bottom of this chart and the top of the one below. She's known for her complex and technical desserts and baking recipes. Perhaps this recipe genre encourages strict adherence.</p>
    </section>

    
    <section class="chart-section" style="margin-top: 2rem;">
        <h4 class="chartTopper">Which authors have the most rule followers?</h4>
        <p class="chart-subtitle">Percentage of comments indicating prep as-written, grouped by recipe author</p>
        <img src={AuthorChartWritten} alt="Author Bar Chart Positive User Made As Written">
    </section>
    
    <h3>5. Every recipe is a story</h3>
    
    <section class="transition-section" style="margin-top: 4rem;">
        <p>It's fun to look at the community as a whole, but every recipe has its own story. This banana nut bar recipe seems innocent enough...</p>
    </section>
    
    <section class="recipe-section">
        <Recipe 
            title="Banana Nut Breakfast Bars"
            authors={BananarecipeAuthors}
            adaptedBy=""
            date="January 16, 2024"
            yieldAmount="9 bars"
            ingredients={BananaIngredients}
        />
    </section>

    <section class="transition-section" style="margin-top: 4rem;">
        <p>...but it has commenters wildly divided!</p>
    </section>

    <section class="chart-section">
        <h4 class="chartTopper">Comments For Banana Nut Breakfast Bars</h4>
        <p class="chart-subtitle">By: Sohla El-Waylly</p>
        <SentimentCluster csvUrl="./csv/df_recipe_bars.csv" defaultGrouped={true}/>
    </section>

    <section class="transition-section" style="margin-top: 4rem;">
        <p>Recipes for technically challenging foods like pie doughs and souffles seem to generate an outsized proportion of questions and commenters who struggle to prepare them adequately:</p>
    </section>
        
    
    <section class="chart-section">
        <h4 class="chartTopper">Comments For Laminated Pie Dough</h4>
        <p class="chart-subtitle">By: Vaughn Vreeland</p>
        <SentimentCluster csvUrl="./csv/df_recipe_laminated_pie_dough_comments.csv" defaultGrouped={true}/>
    </section>

    <section class="transition-section" style="margin-top: 4rem;">
        <p>Salads don't typically elicit unbridaled excitement, but this recipe for <a href="https://cooking.nytimes.com/recipes/1024570-green-salad-with-warm-goat-cheese-salade-de-chevre-chaud">Green Salad With Warm Goat Cheese</a> has the highest ratio of positive to negative comments of any recipe in the data, showing that some recipes are just inexplicably beloved:</p>
    </section>

    <section class="chart-section">
        <h4 class="chartTopper">Comments For Green Salad With Warm Goat Cheese</h4>
        <p class="chart-subtitle">By: Ligaya Mishan</p>
        <SentimentCluster csvUrl="./csv/df_recipe_salad.csv" defaultGrouped={true}/>
    </section>


    <h3>6. Recipes are never complete</h3>



    <section class="transition-section" style="margin-top: 4rem;">
        <p>Comments sections are a relatively new addition to the internet recipe format. For as long as recipes have been around though, people have been leaving comments:</p>

        <img src={RollsImg} alt="Rolls">
            
        
        <p>This examination reminds us: food is deeply personal. Recipes were never meant to be gospel, set in stone, finished, perfect. We let them guide us, but we bring ourselves to them as well. </p>
        
        <p> </p>

        <p>The data reveal a community of people eager to share their successes, problem solve together, and elevate each other's cooking. We might say commenters simply annotate at scale, collectively writing in the margins for all to see.</p>

        <p>Luckily, they often keep us entertained while doing it:</p>
        
    </section>
    <section class="comments-section">        
        <div class="comments-container">
            <div class="comment-wrapper pos-1">
                <Comment 
                    userId="98099363"
                    text="the hardest part of this recipe is getting the batter off my forehead after licking the bowl clean. BEST COOKIE EVER."
                    upvotes="1198"
                    colorVariant="green"
                    rotation={4}               
                    />
            </div>
        </div>
    </section>

</main>
<style>
    main {
        max-width: 600px;
        margin: 0 auto;
        padding: 60px 20px;
    }
    
    .hero {
        margin-bottom: 120px;
    }

    .chart-img, .chart-section {
        width: 80vw;
        max-width: 800px; /* overrides any global image constraints */
        margin-left: calc(50% - min(40vw, 400px)); 
    }

    img {
        max-width: 100%;
        margin: 2rem 0;
    }
    
    h1 {
        font-family: 'Alfa Slab One', serif;
        font-size: 6rem;
        color: var(--red);
        line-height: 1;
        margin: 0 0 30px 0;
        text-transform: capitalize;
        letter-spacing: 0px;
    }

    h2 {
        font-family: 'Alfa Slab One', serif;
        font-size: 3rem;
        color: var(--red);
        line-height: 1;
        margin: 4rem 0 2rem 0;
        letter-spacing: 0px;
        text-align: left;
    }

        h3 {
        font-family: 'Intel One Mono', 'Courier New', monospace;
        font-size: 2rem;
        color: var(--red);
        line-height: 1;
        margin: 4rem 0 4rem 0;
        text-transform: capitalize;
        letter-spacing: 0px;
        text-align: left;
    }

    h4 {
        font-family: 'Intel One Mono', 'Courier New', monospace;
        font-size: 1.4rem;
        font-weight: 600;
        color: var(--black);
        line-height: 1;
        margin: 0;
        text-transform: uppercase;
        text-align: left;
    }

    .chartTopper {
        align-items: baseline;
        margin: 4rem 0 0 0;
    }

    a {
        color: var(--blue);
        text-decoration: none;
        }

    a:hover {
    color: var(--red);
    }

    a:active {
    background-color: black;
    }

    a:visited {
    background-color: #ccc;
    }
    
    .subtitle {
        font-family: 'Intel One Mono', 'Courier New', monospace;
        font-size: 1.25rem;
        line-height: 1.5;
        margin-bottom: 2rem;
        color: var(--text-dark);
    }
    
    .byline {
        font-family: 'Intel One Mono', 'Courier New', monospace;
        font-size: 1rem;
        font-style: italic;
        margin: 0;
    }
    
    .byline p {
        margin: 5px 0;
    }

    .chart-subtitle {
    font-family: 'Intel One Mono', 'Courier New', monospace;
    font-size: .8rem;
    line-height: 1.5;
    color: var(--text-dark)
}
    
    .quote-section {
        margin-bottom: 150px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    blockquote {
        font-family: 'EB Garamond', serif;
        font-size: 1.4rem;
        line-height: 1.6;
        margin: 30rem auto 30rem auto;
        text-align: center;
        color: #555;
    }
    
    blockquote p {
        margin-bottom: 20px;
    }
    
    cite {
        font-size: 1.5rem;
    }
    
    .recipe-section {
        display: flex;
        justify-content: center;
        margin: 80px 0 80px 0;
    }
    
    .transition-section {
        font-family: 'EB Garamond', serif;
        font-size: 1.4rem;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto 0 auto;
        color: #444;
    }
    
    .comments-section {
        margin-top: 80px;
    }
    
    .comments-header {
        font-family: 'Alfa Slab One', serif;
        font-size: 3rem;
        color: var(--red);
        margin: 0 0 40px 0;
        border-bottom: 3px solid var(--red);
        padding-bottom: 10px;
    }
    
    .comments-header .count {
        font-family: 'Intel One Mono', 'Courier New', monospace;
        font-weight: 100;
        font-size: 2rem;
    }
    
    .comments-container {
        display: flex;
        flex-direction: column;
        gap: 40px;
        margin-top: 60px;
        margin-bottom: 7rem;
    }
    
    .pos-1 {
        align-self: flex-start;
        z-index: 1;
    }
    
    .pos-2 {
        align-self: flex-start;
        margin-left: 220px;
        z-index: 2;
    }



    @media (width < 600px) {
        h1 {
            font-size: 4rem;
        }

        h2 {
            padding: 0 .5rem;
        }

      .comments-container {
        align-items: center;
        gap: 30px;
      }

      .pos-1, .pos-2 {
        align-self: center;
        margin-left: 0;
      }

        .chart-img, .chart-section {
        width: 100vw;
        max-width: 800px; /* overrides any global image constraints */
        margin-left: calc(50% - min(50vw, 400px)); 
        }
    }
</style>