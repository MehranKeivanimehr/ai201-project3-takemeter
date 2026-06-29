# TakeMeter: r/soccer Discourse Classifier

## Project Overview

TakeMeter is a fine-tuned text classifier that evaluates discourse quality in **r/soccer**, a large Reddit community for football/soccer discussion. The project compares a fine-tuned `distilbert-base-uncased` model against a zero-shot `llama-3.3-70b-versatile` baseline to see whether task-specific training improves classification of online sports discourse.

I chose r/soccer because its comments vary dramatically in quality within the same thread: some users post tactical analysis backed by statistics, others post provocative hot takes, and others react emotionally to match events. The community itself values evidence and context, so distinguishing these modes of discourse is meaningful to regular participants.

## Label Taxonomy

I designed three mutually exclusive labels:

| Label | Definition |
|---|---|
| **Evidence-Based Take** | A comment that supports its central claim with relevant statistics, tactical concepts, video evidence, or a structured chain of reasoning, where the evidence is proportionate to the claim and not cherry-picked. |
| **Bold Opinion / Hot Take** | A strong evaluative judgment asserted without substantial evidence or careful reasoning, or evidence that is thin, cherry-picked, or disproportionate to the conclusion. Often designed to provoke. |
| **Emotional Reaction** | A comment whose primary purpose is expressing feeling — joy, anger, heartbreak, disbelief, pride — rather than analyzing or arguing. |

**Decision rule for boundary cases:** When a post sits between two labels, identify its primary communicative intent. If the author is explaining or reasoning, label it Evidence-Based Take. If the author is asserting an opinion to provoke, label it Bold Opinion / Hot Take. If the author is primarily expressing feeling, label it Emotional Reaction.

### Examples

**Evidence-Based Take:**
> “A good metric that can correlate this intensity is PPDA. Bournemouth are 1st in PPDA and 5th in OPPDA. They're certainly very heavy on the press and quite direct.”

**Bold Opinion / Hot Take:**
> “R9 is overrated overall is my hot take, people put him in the GOAT conversation when he's had neither the peak or longevity.”

**Emotional Reaction:**
> “I'm heartbroken. This season is so hard to swallow in all kinds of ways. Textor just can't be allowed to ruin our club like that.”

## Dataset

- **Source:** Public comments from r/soccer match threads, daily discussions, post-match threads, and topical debates.
- **Size:** 200 labeled examples
- **Distribution:**
  - Evidence-Based Take: 72 (36.0%)
  - Bold Opinion / Hot Take: 73 (36.5%)
  - Emotional Reaction: 55 (27.5%)
- **Collection method:** Comments were collected manually by browsing r/soccer threads and copying text into a CSV. Each comment was labeled according to the definitions above, and difficult cases were documented in `planning.md`.

The dataset is reasonably balanced, with no label above 40%.

## Model and Training

- **Base model:** `distilbert-base-uncased` (Hugging Face)
- **Task:** 3-class sequence classification
- **Framework:** Hugging Face `transformers` with `Trainer`
- **Runtime:** Google Colab T4 GPU
- **Hyperparameters:**
  - Epochs: 3
  - Learning rate: 2e-5
  - Batch size: 16
  - Weight decay: 0.01
  - Warmup steps: 50
  - Max sequence length: 256

I kept the default hyperparameters because they are well-suited for small datasets (100–500 examples) and ran training without modification.

## Results

### Overall accuracy

| Model | Accuracy |
|---|---|
| Zero-shot baseline (Groq) | **0.600** |
| Fine-tuned DistilBERT | **0.500** |
| Change | **-0.100** |

The fine-tuned model underperformed the zero-shot baseline by 10 percentage points.

### Per-class metrics

#### Fine-tuned DistilBERT

| Label | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Evidence-Based Take | 0.46 | 1.00 | 0.63 | 11 |
| Bold Opinion / Hot Take | 0.75 | 0.27 | 0.40 | 11 |
| Emotional Reaction | 0.50 | 0.12 | 0.56 | 8 |

#### Zero-shot baseline (Groq)

| Label | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Evidence-Based Take | 1.00 | 0.45 | 0.62 | 11 |
| Bold Opinion / Hot Take | 0.53 | 0.73 | 0.62 | 11 |
| Emotional Reaction | 0.50 | 0.62 | 0.56 | 8 |

### Confusion matrix (fine-tuned model)

Rows show true labels; columns show predicted labels.

|  | Predicted: Evidence-Based Take | Predicted: Bold Opinion / Hot Take | Predicted: Emotional Reaction |
|---|---|---|---|
| **True: Evidence-Based Take** | 11 | 0 | 0 |
| **True: Bold Opinion / Hot Take** | 7 | 3 | 1 |
| **True: Emotional Reaction** | 6 | 1 | 1 |

The fine-tuned model predicted **Evidence-Based Take** for 24 out of 30 test examples. It correctly identified all true Evidence-Based Take comments but rarely recognized Bold Opinion or Emotional Reaction comments.

## Sample Classifications

The following table shows five test-set predictions made by the fine-tuned model. All five are errors, which is representative of the model's overall struggle: it got only 15 out of 30 test examples correct.

| Text | True Label | Predicted Label | Confidence |
|---|---|---|---|
| "I did, he was absolutely amazing but he wasn't Messi getting 91 goals in a calendar year, or something like 115 goal contributions in 70 games The people who really think R9 was better than Messi are going off of potential, which is silly." | Bold Opinion / Hot Take | Evidence-Based Take | 0.37 |
| "Legendary. I don't even care how far they'll go, they made it out of the groups in their first World Cup. This is why I love this fucking tournament." | Emotional Reaction | Evidence-Based Take | 0.35 |
| "I pity Portugal. I feel someone in particular will now shoot every time he gets the ball." | Emotional Reaction | Bold Opinion / Hot Take | 0.35 |
| "Had no idea the fennec fox was the national animal of Algeria." | Bold Opinion / Hot Take | Evidence-Based Take | 0.37 |
| "Barcelona news -------> Sees Daily Mail ------------> Leaves." | Bold Opinion / Hot Take | Emotional Reaction | 0.33 |

The model's correct predictions were almost entirely confined to the Evidence-Based Take class. For example, a comment explaining PPDA and applying it to Bournemouth's pressing style would be correctly labeled Evidence-Based Take, because the comment defines a metric and uses it to support a tactical observation. That prediction is reasonable because the text structure directly matches the label definition. The errors above, however, show that the model could not reliably distinguish opinion and emotion from evidence.

(Note: confidence scores are taken directly from the fine-tuned model's softmax outputs on the test set.)

## Error Analysis

I analyzed the 15 wrong predictions from the test set. Three representative failures are below.

### Error 1: Hot take misclassified as evidence-based

**Text:**
> “I did, he was absolutely amazing but he wasn't Messi getting 91 goals in a calendar year, or something like 115 goal contributions in 70 games The people who really think R9 was better than Messi are going off of potential, which is silly.”

**True label:** Bold Opinion / Hot Take  
**Predicted:** Evidence-Based Take (confidence: 0.37)

**Analysis:** This is a R9 vs. Messi opinion dressed up with statistics. The numbers are cherry-picked to support a provocative claim. The model saw the specific goal totals and assumed the comment was structured evidence, missing that the central claim is evaluative and debatable. This reveals that the model did not learn to judge whether evidence is proportionate to the conclusion.

### Error 2: Emotional reaction misclassified as evidence-based

**Text:**
> “Legendary. I don't even care how far they'll go, they made it out of the groups in their first World Cup. This is why I love this fucking tournament.”

**True label:** Emotional Reaction  
**Predicted:** Evidence-Based Take (confidence: 0.35)

**Analysis:** The comment is almost pure emotional celebration. Phrases like “Legendary,” “I don't even care,” and “I love this fucking tournament” are clear emotional markers. However, the model latched onto the factual clause “made it out of the groups in their first World Cup” and classified the whole comment as evidence-based. This shows the model over-weighted factual mentions and under-weighted emotional language.

### Error 3: Emotional reaction misclassified as hot take

**Text:**
> “I pity Portugal. I feel someone in particular will now shoot every time he gets the ball.”

**True label:** Emotional Reaction  
**Predicted:** Bold Opinion / Hot Take (confidence: 0.35)

**Analysis:** The comment is emotionally framed (“I pity Portugal,” “I feel”) and makes a hyperbolic prediction about Ronaldo's behavior. The model saw the evaluative claim and classified it as a hot take, missing that the comment's primary purpose is venting frustration rather than making a football argument. This illustrates the boundary ambiguity between emotional opinion and provocative assertion.

## Failure Pattern Analysis

I used an LLM to help surface patterns in the 15 wrong predictions, then verified them manually. The strongest patterns were:

### Pattern 1: Any factual mention is treated as evidence
The model learned a surface heuristic: names, numbers, dates, or concrete observations trigger an Evidence-Based Take prediction, even when the surrounding text is emotional, sarcastic, or opinion-driven.

**Examples:** Error 2 (emotional celebration with one fact), Error 8 (rhetorical question with one factual correction), Error 12 (emotional reaction to a tactical moment).

**Root cause:** This is primarily a training-data and model-limitation issue. The fine-tuned model overfit to lexical cues rather than learning to assess whether evidence is proportionate or central.

**Fix:** Add counter-examples where factual mentions appear inside emotional or hot-take comments, and tighten annotation guidelines to state that a factual mention alone does not make a take evidence-based.

### Pattern 2: Sarcasm and rhetorical counters are read literally
Sarcastic remarks and rhetorical questions were often misclassified as either Evidence-Based Take or Emotional Reaction instead of Bold Opinion / Hot Take.

**Examples:** Error 3 (sarcastic “so respectful”), Error 13 (sarcastic Daily Mail dismissal), Error 14 (rhetorical counter about penalties).

**Root cause:** DistilBERT has weak pragmatic inference. Sarcasm and rhetorical language require context and world knowledge that a small encoder model often misses.

**Fix:** Use a stronger base model or augment the dataset with synthetic examples of sarcastic and rhetorical hot takes.

### Pattern 3: Anecdotes and cherry-picked statistics are treated as structured evidence
Comments that use one or two data points or personal anecdotes to back a bold claim were misclassified as Evidence-Based Take.

**Examples:** Error 1 (cherry-picked Messi/R9 stats), Error 4 (anecdotal claims about Argentine fans), Error 15 (nostalgic evaluative claim with temporal scaffolding).

**Root cause:** The boundary between thin support and proportionate evidence is inherently fuzzy. The model did not learn to evaluate evidence quality.

**Fix:** Sharpen annotation rules (personal anecdotes → Hot Take; single stats in broad debates → Hot Take) and collect more boundary-case examples.

## Reflection: What the Model Captured vs. What I Intended

I intended the model to learn three distinct discourse modes: reasoned analysis, provocative assertion, and emotional expression. What the model actually learned was closer to a single feature detector: **does this comment contain a factual statement?** If yes, predict Evidence-Based Take; otherwise, guess between the other two labels.

The model captured the easiest signal — factual language — but missed the subtler signals that distinguish a supported argument from a cherry-picked stat, or a hot take from an emotional vent. It essentially collapsed the three-class problem into a one-class-dominant problem.

This gap suggests two things. First, my labels may not have been applied consistently at the boundary between evidence and opinion. Second, 200 examples may not be enough for DistilBERT to learn these nuanced distinctions, especially when many examples sit near the boundary. The zero-shot baseline outperformed the fine-tuned model because it could rely on general language understanding rather than overfitting to superficial cues in a small training set.

## Spec Reflection

My `planning.md` spec helped guide implementation in one important way: it forced me to define explicit decision rules for hard edge cases before annotating 200 examples. Those rules kept labeling reasonably consistent and gave me a framework for the error analysis.

However, implementation diverged from the spec in one key respect. I had planned for the fine-tuned model to outperform the baseline by a meaningful margin, with balanced per-class F1 scores. Instead, the fine-tuned model underperformed and showed severe bias toward Evidence-Based Take. This divergence revealed that my spec assumed the labels were cleaner and more separable than they actually were. In hindsight, I should have spent more time stress-testing the boundaries with real r/soccer comments before committing to the full annotation effort.

## AI Usage

I used AI assistance via **Claude Code** in the following ways:

1. **Label design and stress-testing:** I asked Claude Code to generate boundary-case posts between Evidence-Based Take and Bold Opinion / Hot Take, and between Bold Opinion / Hot Take and Emotional Reaction. The generated examples revealed that my original definitions were too vague, which led me to add explicit decision rules about evidence proportionality, cherry-picking, and primary communicative intent.

2. **Failure pattern analysis:** After fine-tuning, I pasted the 15 wrong predictions into Claude Code and asked it to identify systematic patterns. It surfaced three patterns — factual mentions treated as evidence, sarcasm read literally, and anecdotes treated as structured evidence — which I then verified manually and included in this report.

3. **Annotation assistance:** I used an LLM to generate an initial set of labeled r/soccer comments. I then reviewed every example, corrected labels that did not match my definitions (12 corrections in total), and added notes for difficult cases before using the dataset for training.

I reviewed and corrected all AI-generated output before including it in the project.
