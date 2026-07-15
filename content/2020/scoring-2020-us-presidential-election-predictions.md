Title: Scoring 2020 U.S. Presidential Election Predictions
Date: 2020-11-07 18:23
Status: published
Category: social science
Tags: politics

I was curious to see how various prognosticators—specifically, [_FiveThirtyEight_](https://projects.fivethirtyeight.com/2020-election-forecast/) and [_The Economist_](https://projects.economist.com/us-2020-forecast/president)'s models, and the [PredictIt prediction markets](https://www.predictit.org/markets/13/Prez-Election)—did on predicting the state-by-state [(plus the District of Columbia)](https://twitter.com/zackmdavis/status/1323492262198718464) results of the recent U.S. presidential election.

### Mathematical Sidebar

There are various ways to evaluate probabilistic predictions, but my favorite is to use the _logarithmic score_: the logarithm of the probability assigned to the right answer. (Logs of probabilities are negative numbers, but negating everything to get positive numbers doesn't change anything interesting—you just minimize instead of maximizing—such that I tend to mentally conflate the log and the negative-log.)

The reason I think the logarithmic score is best is because it has one essential property, one cool property, and a meaningful interpretation.

The essential property is that it [incentivizes you to report your actual probabilities](https://en.wikipedia.org/wiki/Scoring_rule#Proper_scoring_rules): if something actually happens 80% of the time, you get the best expected score by giving it probability 0.8.

The cool property is that [it doesn't matter how you chop up your observations](https://www.readthesequences.com/A-Technical-Explanation-Of-Technical-Explanation): because conjunction of probabilities is multiplication and the logarithm maps multiplication to addition, we get the same score whether we consider "A&B" as one event, or separately add up the scores of "A" and "B, given A".

(Although as [David Schneider-Joseph](https://twitter.com/TheDavidSJ/status/1325561155524288514) and [Oscar Cunningham](https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=iibA9SicAbufWE6q5) pointed out in response to the originally published version of this post, my calculations later in this post add up scores of state-by-state predictions as if the state results were independent events, but this independence assumption is not realistic. Sorry.)

The interpretation is that the logarithmic score represents [the length of the message you would need to encode the actual outcome using a code optimized for your model](https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length). (Er, the negation of the score represents the length—there's that conflation.)

### Methodology

So, the election results aren't _really_ final until all the states certify their results—or perhaps, when the Electoral College meets. The Trump campaign [has filed lawsuits disputing results in a number of states](https://archive.is/GhkyS), and at time of writing, [ABC News's map](https://abcnews.go.com/Elections/2020-us-presidential-election-results-live-map/) has no call for Alaska, Arizona, North Carolina, and Georgia. But for the purposes of this blog post, I'm just going to go with the current colors on [Politico's map](https://www.politico.com/2020-election/results/president/), and assume that Biden wins Arizona and Georgia and that Trump wins Alaska and North Carolina.

At around 20:10 Pacific time on 2 November, Election Day Eve, I downloaded the model-output ZIP files from [_FiveThirtyEight_](https://projects.fivethirtyeight.com/data-webpage-data/datasets/election-forecasts-2020.zip) and [_The Economist_](https://cdn.economistdatateam.com/us-2020-forecast/data/president/economist_model_output.zip). Then today, I looked up 2 November prices for the Democrat-wins contracts in the line-graphs on the pages for the PredictIt "Which party will win this-and-such-state in the 2020 presidential election?" markets. (Both _FiveThirtyEight_ and _The Economist_ would later issue final updates on Election Day, but I'm assuming it couldn't have changed much, and it's a fairer comparison to the PredictIt bucketed-by-day line graphs to use the model outputs from Election Day Eve.)

I got _The Economist_'s per-state Biden-victory probabilities from the `projected_win_prob` column in `/output/site_data//state_averages_and_predictions_topline.csv` in _The Economist_'s zipfile, and _FiveThirtyEight_'s per-state Biden-victory probabilities from the `winstate_chal` column in `/election-forecasts-2020/presidential_state_toplines_2020.csv` in _FiveThirtyEight_'s zipfile.

I'm only using the states' at-large results and ignoring the thing where Nebraska and Maine do some of their electoral votes by Congressional district.

I'm using the convention of giving probabilities in terms of the event of interest being "Biden/Democrat wins" rather than "Trump/Republican wins", because that's what _The Economist_ seems to be giving me, but I appreciate that the _FiveThirtyEight_ spreadsheet has separate `winstate_inc` (incumbent), `winstate_chal` (challenger), and `winstate_3rd` (thirty-party) columns. (Although the `winstate_3rd` column is blank!!) Using "incumbent wins" as the event actually seems like a more natural Schelling-point convention to me?—but it doesn't matter.

I wrote a Python script to calculate the scores. The main function looks like this:

```python
def score():
    scores = {"fivethirtyeight": 0, "economist": 0, "predictit": 0}
    swinglike_only_scores = {
        "fivethirtyeight": 0,
        "economist": 0,
        "predictit": 0,
    }
    losses = {}

    swinglikes = [sr for sr in state_results if is_swinglike(sr)]
    print(
        "{} states ({}) are swinglike".format(
            len(swinglikes),
            ','.join(sr.state for sr in swinglikes)
        )
    )

    for state_result in state_results:
        if state_result.actual is None:
            continue

        for predictor in scores.keys():

            if state_result.actual:  # Biden win
                probability = getattr(state_result, predictor)
            else:
                probability = 1 - getattr(state_result, predictor)

            subscore = log2(probability)

            scores[predictor] += subscore

            if is_swinglike(state_result):
                swinglike_only_scores[predictor] += subscore

            losses[(predictor, state_result.state)] = subscore

    return scores, swinglike_only_scores, losses
```

[(Full source code, including inline data.)](https://gist.github.com/zackmdavis/623e15a3cdab66d3eaecf2a6f8b6169a)

Getting the numbers from both spreadsheets and the browser line graphs into my script involved a lot of copy-pasting/Emacs-keyboard-macros/typing, and I didn't exhaustively double-check everything, so __it's possible I made some mistakes, but I hope that I didn't, because that would be embarrassing.__

### Results

Scoring over all the states, _The Economist_ did the best, with a score of about −7.51 bits, followed by _FiveThirtyEight_ at −9.24 bits, followed by PredictIt at −12.14.

But I was worried that this methodology might privilege the statistical models over the markets, because the models (particularly _The Economist_, which was the most confident across the board) might be eking out more points by assigning very low/high probabilities to "safe" states in ways that the PredictIt markets won't: intuitively, I suspect that the fact that someone is willing to scoop up Biden-takes-Alabama contracts at 2¢ each may not be capturing the full power of what the market can do on harder questions. So I also calculated the scores on just the 12 "swing-like" states (Alaska, Arizona, Florida, Georgia, Iowa, Montana, North Carolina, New Hampshire, Nevada, Ohio, Pennsylvania, and Texas) where at least two of our three predictors gave a probability between 0.1 and 0.9.

On just the "swing-like" states, the results are a lot more even, with _The Economist_ at −7.36 bits, PredictIt at −7.40, and _FiveThirtyEight_ at −7.89.

The five largest predictive "misses" were _The Economist_ and _FiveThirtyEight_ on Florida (the models leaned Biden but the voters said Trump, giving the models log scores of −2.22 and −1.66, respectively), _The Economist_ and _FiveThirtyEight_ on North Carolina (same story for scores of −1.60 and −1.46), and PredictIt on Georgia (the market leaned Trump, but we think the voters are saying Biden for a score of −1.32).
