# TakeMeter Project Plan

## Community

**r/soccer** — one of the largest sports communities on Reddit (~8.7M members). It acts as a global hub for match highlights, news, live match threads, and daily discussion. Comments range from data-heavy tactical breakdowns to tribal hot takes, emotional venting, and in-joke banter. Quality is regulated by upvotes/downvotes and rules that discourage low-effort shitposting.

**Why r/soccer is a good fit for this task:**
- The discourse is extremely text-heavy and high-volume.
- Posts vary widely in quality within the same thread — the same match can produce tactical analysis, tribal hot takes, and pure venting side by side.
- The community has explicit norms around what counts as a good take: evidence, context, and good faith are valued, while unsupported absolutes and recency bias are criticized.
- The distinction between "analysis" and "hot take" is already part of how regular users talk about the subreddit, so the labels are grounded in community norms rather than imposed from outside.

## Labels

I will use a 3-label taxonomy:

### 1. Evidence-Based Take
A comment that supports its central claim with relevant statistics, tactical concepts, video evidence, or a structured chain of reasoning, where the evidence is proportionate to the claim and not cherry-picked.

**Decision rule:** If the evidence would still support the claim even if the emotional or evaluative framing were removed, label it Evidence-Based Take. If the conclusion is far stronger than the evidence provided, or if the evidence is a single cherry-picked stat used to support a sweeping claim, downgrade to Bold Opinion / Hot Take.

### 2. Bold Opinion / Hot Take
A strong evaluative judgment asserted without substantial evidence or careful reasoning, or evidence that is thin, cherry-picked, or disproportionate to the conclusion. Often designed to provoke.

**Decision rule:** If the comment contains a substantive football claim but the reasoning is vague, hyperbolic, or one-sided, label it Bold Opinion / Hot Take. This includes sweeping superlatives ("greatest ever," "has to go") unless they are supported by transparent criteria or sustained reasoning.

### 3. Emotional Reaction
A comment whose primary purpose is expressing feeling — joy, anger, heartbreak, disbelief, pride — rather than analyzing or arguing. Removing the emotional language would leave little or no substantive football claim.

**Decision rule:** Ask: *"If I removed the emotional language, would a substantive football claim remain?"* If yes → Bold Opinion / Hot Take. If no, or if the claim is just a restatement of the emotion → Emotional Reaction.

## Why These Labels Matter in r/soccer

These distinctions reflect how regular r/soccer users actually talk about discourse quality. The community tends to value data (xG, PPDA, pass networks), tactical context, and good-faith sourcing. It criticizes unsupported absolutes, recency bias, tribalism, and pure venting outside match threads. The labels capture this divide between evidence-backed argument, provocative assertion, and emotional expression.

## Examples

### Evidence-Based Take

**Example A:**
> “A good metric that can correlate this intensity is PPDA. It is basically a measure of how intense and high up the pitch the press is. Bournemouth are 1st in PPDA and 5th in OPPDA. They're certainly very heavy on the press and quite direct… OPPDA is the more concerning thing imo.”

**Example B:**
> “xG is a pre-shot metric, it is taken as the quality of the chance. The goalkeeper has nothing to do with it, it is the defenders or the midfielders that have to prevent shots with high quality.”

### Bold Opinion / Hot Take

**Example A:**
> “R9 is overrated overall is my hot take, people put him in the GOAT conversation when he's had neither the peak or longevity.”

**Example B:**
> “Lamine Yamal is an overrated dribble and banger merchant.”

### Emotional Reaction

**Example A:**
> “I'm heartbroken. This season is so hard to swallow in all kinds of ways. Textor just can't be allowed to ruin our club like that.”

**Example B:**
> “I CANT BELIEVE THIS IS MY CLUB.”

## Hard Edge Cases

These are real examples from my labeled dataset where the correct label was genuinely unclear. I include them here to show how I applied the decision rules in practice.

### Difficult example 1: Bold Opinion / Hot Take vs. Emotional Reaction

**Post:**
> “I don't know, I feel like Messi would have cured Rodrygo right there and then. Poor show from Ronaldo really.”

**Possible labels:** Emotional Reaction or Bold Opinion / Hot Take.

**Decision:** I labeled it **Bold Opinion / Hot Take**. The comment contains emotional framing ("Poor show"), but if you remove the emotional language, a substantive evaluative claim remains: Messi would have handled the situation better than Ronaldo. That is a football judgment, not pure feeling.

### Difficult example 2: Evidence-Based Take vs. Emotional Reaction

**Post:**
> “‘Could have achieved incredible things’ I mean…most of his goals were scored after that, he may have scored fewer if the injury had never happened and he never played striker. We’re talking about one of the all time greats here.”

**Possible labels:** Emotional Reaction or Evidence-Based Take.

**Decision:** I labeled it **Evidence-Based Take**. The comment defends Ronaldo's post-injury career with a structured counterargument — it engages with the hypothetical, references his goal output, and reasons through the claim. The emotional attachment to R9 is present but does not dominate the comment.

### Difficult example 3: Evidence-Based Take vs. Emotional Reaction

**Post:**
> “I've been a devout fan and supporter of Klose all my life (coming from an Upper Silesian family, he has been an inspiration, almost a hero, for us) and although I am of course sad right now, I am glad for the past 12 years and how they kept him in international conversation. Records are broken, but the legend remains.”

**Possible labels:** Evidence-Based Take or Emotional Reaction.

**Decision:** I labeled it **Emotional Reaction**. The comment references a record being broken, but the dominant thrust is personal reflection, devotion, and sadness. Removing the emotional language would leave almost nothing substantive.

### Ambiguous type 1: Evidence-Based Take vs. Bold Opinion / Hot Take
A post cites real stats but uses them to support a sweeping or provocative conclusion that the evidence does not justify.

**Example:**
> “Haaland has 7 touches in the box this season against top-half sides and his xG per shot has dropped from 0.21 to 0.14. He’s not a big-game player anymore and City should bench him in the CL knockouts.”

**Handling rule:** Label as **Bold Opinion / Hot Take**. The stats are real, but the sample is tiny and the conclusion (“not a big-game player anymore,” “should bench him”) is far stronger than the evidence. Evidence must be relevant to the central claim and proportionate to it. If the conclusion is an extreme overreaction supported by cherry-picked data, it is a hot take, not analysis.

### Ambiguous type 2: Bold Opinion / Hot Take vs. Emotional Reaction
A post is emotionally loaded and also contains an evaluative claim about a player, manager, or team.

**Example:**
> “Ten Hag has to go. He’s clueless, the players don’t respect him, and I’m tired of watching this boring garbage every weekend. Enough is enough.”

**Handling rule:** Label as **Emotional Reaction**. Although it contains a managerial-change opinion, the comment is overwhelmingly a vent: repeated expressions of exhaustion, no evidence, and no reasoning. The claim is essentially a vehicle for frustration. Apply the test: if you remove the emotional language, does a substantive football claim remain? Here, little remains beyond "Ten Hag should be fired," which is itself an emotional reaction rather than an argued position.

### General decision rule for all edge cases
When a post sits between two labels, identify the **primary communicative intent**:
- Is the author trying to explain or reason? → Evidence-Based Take.
- Is the author trying to provoke or assert an opinion? → Bold Opinion / Hot Take.
- Is the author trying to express feeling? → Emotional Reaction.

## Data Collection Plan

**Source:** Public comments from r/soccer match threads, daily discussion threads, and post-match threads.

**Target size:** At least 200 examples.

**Target distribution:**
- Evidence-Based Take: ~70 examples (35%)
- Bold Opinion / Hot Take: ~70 examples (35%)
- Emotional Reaction: ~60 examples (30%)

This keeps every label above the 20% minimum and avoids a majority-class problem.

**Procedure:**
1. Browse r/soccer threads and copy comment text into a spreadsheet.
2. Assign a label based on the definitions and decision rules above.
3. After every 50 examples, check the label distribution.
4. If any label falls below 20% after 200 examples, return to r/soccer and intentionally sample more comments likely to fit that label (e.g., look for match-thread venting for Emotional Reaction, or tactical breakdowns for Evidence-Based Take) until balance is restored.

**Exclusions:**
- Memes, jokes, and one-word reactions ("lmao," "bottlers") will be skipped because they do not fit any label meaningfully.
- Comments that reference inside jokes without substantive content will be skipped.

## Evaluation Metrics

I will evaluate both the fine-tuned DistilBERT model and the Groq zero-shot baseline using:

1. **Overall accuracy** — simple headline metric for comparison between models.
2. **Per-class precision, recall, and F1** — necessary because a 3-class problem can hide class-specific failures behind overall accuracy. For example, a model could achieve high accuracy by never predicting Emotional Reaction.
3. **Confusion matrix** — to visualize systematic misclassifications (e.g., whether Evidence-Based Take is frequently confused with Bold Opinion / Hot Take).
4. **Error analysis on at least 3 wrong predictions** — to understand what the model actually learned versus what I intended.

**Why these metrics:** Accuracy alone is insufficient for an imbalanced subjective task. Precision, recall, and F1 reveal whether the model performs equally across labels or simply learns to predict the majority class. The confusion matrix helps identify whether the model systematically confuses two specific labels, which would indicate a definition or data problem.

## Definition of Success

The classifier will be considered successful if:

1. The fine-tuned model outperforms the zero-shot Groq baseline on overall accuracy.
2. Overall accuracy is above the majority-class baseline (which would be ~35% if labels are evenly distributed).
3. At least one per-class F1 score is ≥ 0.60, and no label has an F1 below 0.40.
4. The failure analysis identifies at least one clear pattern in the model's mistakes (e.g., "confuses short emotional posts with hot takes").

**"Good enough" for deployment:** A real community tool would need the fine-tuned model to consistently beat the baseline by at least 10 percentage points and to have balanced per-class performance. If the model only works on one label, it is not useful for moderating or summarizing discourse across the community.

## AI Tool Plan

### Label Stress-Testing
I used an LLM to generate 10 boundary-case posts (5 between Evidence-Based Take and Bold Opinion / Hot Take, 5 between Bold Opinion / Hot Take and Emotional Reaction). The stress test revealed that the original definitions were intuitive but underdetermined three common r/soccer patterns:
- Cherry-picked stats used to justify provocative claims.
- Evaluative superlatives backed by real but insufficient evidence.
- Emotionally loaded comments that still contain an opinion-shaped structure.

Based on this, I tightened the definitions by adding explicit rules about evidence sufficiency, proportionality, and primary communicative intent.

### Annotation Assistance
I will **not** use an LLM to pre-label examples. All 200+ labels will be assigned manually to avoid bias and ensure consistent application of the decision rules. This choice will be disclosed in the README.

### Failure Analysis
After training, I will give the list of wrong predictions to an LLM and ask it to identify systematic patterns (e.g., "the model consistently misclassifies short emotional posts as Bold Opinion / Hot Take"). I will verify each proposed pattern manually against the actual text before including it in the evaluation report.
