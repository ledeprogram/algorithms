# Algorithms in the newsroom

Ever since Phillip Meyer published [Precision Journalism](http://www.unc.edu/~pmeyer/book/) in the 1970s (and probably even a bit before), journalists have been using algorithms in some form in order to tell new and different kinds of stories. Below we've included several examples from different eras of what you'd now call data journalism:

### Classic examples

Computer-assisted reporting specialists have been a fixture in newsroom for decades, applying data analysis and social science methods to the news report. Some of the most sophisticated of those techniques are based in part on algorithms we'll learn in this class:

- **School Scandals, Children Left Behind: Cheating in Texas Schools and Also [Faking the Grade](http://clipfile.org/?p=892)**: Two powerful series of stories by the Dallas Morning News in the mid-2000s that showed rampant cheating by students and teachers on Texas standardized exams. Not the first story to use regression models but one of the most powerful early examples.

- **[Speed Trap: Who Gets a Ticket, Who Gets a Break?](http://www.boston.com/globe/metro/packages/tickets/)**: Another early example of using logistic regression to explain a newsworthy phenomenon -- in this case the many factors that go into whether a person is given a speeding ticket or let off the hook. Just as interesting as the story is its [detailed methodology](http://www.boston.com/globe/metro/packages/tickets/study.pdf), which is worth a read.

- **[Cluster analysis in CAR](https://www.ire.org/publications/search-uplink-archives/167/)** Simple cluster analysis has been used for years in newsrooms to find everything from [crime hotspots](http://www.icpsr.umich.edu/CrimeStat/) to [cancer clusters on Long Island](http://www.ij-healthgeographics.com/content/2/1/3).

### Algorithmic journalism catches 

Although reporters and computer-assisted reporting specialists had been doing some form of it for years the idea of "data journalism" as its is now known was popularized during the 2012 presidential elections, in large part thanks to the predictive modeling of Nate Silver.

- **[FiveThirtyEight](http://fivethirtyeight.blogs.nytimes.com/fivethirtyeights-2012-forecast/)**: Nate Silver's prediction models were the first example of data/algorithmic journalism reaching the mainstream. Since then, election predictions have become a bit old hat. The Times' new model, [Leo](http://www.nytimes.com/newsgraphics/2014/senate-model/), was exceedingly accurate in 2014 (its [source code](https://github.com/TheUpshot/leo-senate-model) is online). The Times also ran a series of [live predictions](http://elections.nytimes.com/2014/senate-model) on key 2014 races on Election Night.

- **[ProPublica's Message Machine](https://projects.propublica.org/emails/)**: Also during the 2012 elections, ProPublica launched its Message Machine project, which used hashing algorithms to reverse-engineer targeted e-mail messages from political campaigns.

- **[L.A. Times crime alerts](http://maps.latimes.com/crime/)**: The Los Angeles Times has for years been calculating and publicizing alerts when crime spikes in certain neighborhoods.

### Modern examples

These days, sophisticated algorithms are used to solve all sorts of journalistic problems, both exciting and mundane.

- **[Campaign finance data deduplication](https://github.com/cjdd3b/fec-standardizer/wiki)**: Most campaign finance data is organized by contribution, not donor. Joe Smith might give three different contributions and be listed in the data in three different ways. Connecting those records into a single canonical Joe Smith is often the first step to doing sophisticated campaign finance analysis. Over the last few years, people have developed highly accurate methods to do this using both supervised and unsupervised machine learning.

- **[NYT Cooking](http://cooking.nytimes.com/)**: The new Cooking website and app has been one of the Times' most successful new products, but it was initially based largely on recipes stored in free-text articles. The Times extracted many of those recipes using an algorithmic technique known as [conditional random fields](http://open.blogs.nytimes.com/2015/04/09/extracting-structured-data-from-recipes-using-conditional-random-fields/). The L.A. Times did something [similar](https://source.opennews.org/en-US/articles/how-we-made-new-california-cookbook/) in 2013.

- **[The Echo Chamber](http://www.reuters.com/investigates/special-report/scotus/)**: A team from Reuters were finalists for the Pulitzer this year after using (among other things) sophisticated topic modeling techniques to help document how a small group of lawyers have disproportionate influence over the U.S. Supreme Court.