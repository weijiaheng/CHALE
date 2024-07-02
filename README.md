# CHALE
Controlled HALlucination-Evaluation (CHALE) Dataset

# Key Components (Code)
* ``hallucinated_ans_final_filtered.json``: includes approximately 1000 QA samples. Preprint will come soon!

The dataset is in a dictionary format, which includes the following keys:

**Question**, **Short_ans**, **Long_ans**, **halu**, **mid-halu**, **non-halu**

* ``start_code.py``: a start code to load the data.

# Detailed Generation of CHALE

The Controlled Hallucination-Evaluation (CHALE) dataset is constructed based on the "[Google Natural Questions](https://ai.google.com/research/NaturalQuestions/visualization)" dataset The original dataset comprises approximately 307,000 training samples. For CHALE, we meticulously selected a subset of around 100,000 samples from these training data. Each selected entry in CHALE contains the following essential components, which are integral to our evaluation framework:

* **Question text**: This is the natural question posed in the dataset.

* **Short Answer**: A concise and accurate answer to the natural question. This brief response provides a straightforward answer to the query.

* **Long Answer**: In contrast to the short answer, this is an elongated and more detailed response, offering a comprehensive explanation or context to the natural question.

* **Additional Information**: This includes crucial metadata such as the annotation ID, document resource URL, and example ID. This information is necessary for seamless integration and retrieval of data from the official dataset.

### Dataset Generation Methodology

The construction of the CHALE dataset follows a systematic approach aimed at generating question-answer pairs that exhibit potential hallucinations. Each response in our dataset follows the format: ``Short Answer + Detailed Information/Reasoning``. Within this framework, the accuracy of the short answer is utilized as an indicator of truthfulness. In contrast, the relevance and coherence of the detailed information or reasoning segment are employed to gauge the informativeness of the response. To achieve this structure, we deconstruct each comprehensive answer into its sentences. Then, one sentence is randomly chosen as the detailed information/reasoning component.

In the CHALE dataset, a standard non-hallucinated answer combines the pertinent short answer with concise reasoning or additional information derived from the more extensive corresponding long answer. To generate hallucinated responses, we adopt a strategic mismatch approach. This involves either misaligning the short answer or the informative segment with the original question, instead aligning it with a nearby yet distinct question. 
