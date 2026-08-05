# Cost optimization — Generative AI Lens best practices

Source: *AWS Well-Architected Framework — Generative AI Lens* (2026). 9 best practices in this pillar.

## Contents

- [GENCOST01-BP01]( #gencost01-bp01 ) Right-size model selection to optimize inference costs — risk if absent: **Medium**
- [GENCOST02-BP01]( #gencost02-bp01 ) Balance cost and performance when selecting inference paradigms — risk if absent: **Medium**
- [GENCOST02-BP02]( #gencost02-bp02 ) Optimize resource consumption to minimize hosting costs — risk if absent: **Medium**
- [GENCOST03-BP01]( #gencost03-bp01 ) Optimize prompt token length — risk if absent: **Medium**
- [GENCOST03-BP02]( #gencost03-bp02 ) Control model response length — risk if absent: **Medium**
- [GENCOST03-BP03]( #gencost03-bp03 ) Implement prompt caching to reduce token costs — risk if absent: **Medium**
- [GENCOST03-BP04]( #gencost03-bp04 ) Annotate user input to enable cost-aware content filtering — risk if absent: **Medium**
- [GENCOST04-BP01]( #gencost04-bp01 ) Reduce vector length on embedded tokens — risk if absent: **Medium**
- [GENCOST05-BP01]( #gencost05-bp01 ) Create stopping conditions to control long-running workflows — risk if absent: **High**

---

## GENCOST01-BP01 Right-size model selection to optimize inference costs

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice helps you manage spend on foundation model inference without guessing at the capacity requirements for a foundation model.

### Implementation guidance

Foundation models have several cost-dimensions, some of which change depending on the hosting paradigm (managed or self-hosted). Traditionally, managed models charge for consumption measured in token input and token output. Self-hosted models charge using traditional infrastructure costs.

For managed models hosted on Amazon Bedrock, different models charge differently for the number of tokens input and output. Oftentimes, newer and larger models may have higher cost compared to older or smaller models. Self-hosted models on Amazon EC2 or Amazon SageMaker AI inference endpoints charge based on uptime, as well as additional costs storage and network costs.

When optimizing for cost, consider testing with a smaller model first, and gradually increase model size and capabilities until an acceptable model is selected. The criteria for an acceptable

model will change based on the use case of the workload. By starting with the smallest model, you improve the chances of selecting a model with the most cost-effective token input and output cost. Alternatively, optimize self-hosted model infrastructure based on the model used and the workload's usage pattern. Consult the model card or technical documentation for recommendations on instance size and capacity, right-sizing based on usage patterns.

Deploy multiple models to a single, multi-model endpoint where appropriate. Right-size as an ongoing activity. As newer models become available, the workload needs change, and as prompting and orchestration are refined, smaller, more cost-effective models should be evaluated against your workload's needs to continually optimize.

Consider decomposing your workload and routing to different sized models based on the specific needs of each inference request. Route less complicated inferences to smaller, more cost-effective models while assessing quality to maintain high quality across variably complicated inference requests. For managed models hosted on Amazon Bedrock, consider intelligent prompt routing for dynamic routing between models in the same model family. Alternatively, weight the benefits of developing a custom prompt routing layer. In some cases, real-time inference may not be required. In those instances, elect for a less expensive inference paradigm such as batch inference.

### Implementation steps

1. Identify the minimum performance requirements for a foundation model.
2. Determine the models available which meet that minimum performance bar.
3. Select the most cost-efficient model based on the prioritized cost dimensions (like hosting paradigm, model size, or token cost).
4. Continuously evaluate model selection to validate the highest performance is being achieved at the lowest possible price-point.

### Further reading

- Tagging Amazon Bedrock resources
- Track, allocate and manage your generative AI cost and usage with Amazon Bedrock
- Optimizing costs of generative AI applications on AWS
- GENCOST02-BP01 Balance cost and performance when selecting inference paradigms
- GENCOST02-BP02 Optimize resource consumption to minimize hosting costs

---

## GENCOST02-BP01 Balance cost and performance when selecting inference paradigms

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice describes a relationship between cost and performance contextualized against model hosting and inference paradigms. This relationship helps you evaluate cost-benefit choices associated with the selection of an inference paradigm.

### Implementation guidance

Throughput sensitive workloads often require additional resources to service inference requests at the rate they are being submitted. Provisioned throughput, available through Amazon Bedrock, provides increased throughput capability for large language models supporting generative AI workloads. If your workload requires provisioned throughput to meet its performance requirements, consider preferring longer commitment terms for better unit costs. Validate your scaling requirements with shorter duration commitments to avoid over-provisioning your workload. Provisioned throughput is available for purchase in Amazon Bedrock. If the model you are using has throughput performance needs or continuous model inference scale supports provisioned throughput, consider purchasing a short-term. Test the improvement and determine if the provisioned throughput improves your application's performance. If there is a strong case for provisioned throughput, consider purchasing a six-month plan, as the unit cost for six months is usually lower than purchasing month-over-month.

Consider a scenario where you want to serve inference capabilities for a single model for small, periodic workloads. Evaluate the cost of hosting this model on an Amazon SageMaker AI inference endpoint. Compare these costs against the cost of importing the model to Amazon Bedrock using Amazon Bedrock's Custom Model Import feature and using API-based inference. Evaluate the cost to deploy this model using either paradigm and compare them with respect to the total cost of ownership. Where performance trade-offs are negligible, deploy to the most cost-effective inference paradigm.

### Implementation steps

1. Identify the nature of the demand for this workload.
2. Compare the demand to the available hosting options, and remove the high-cost options that do not satisfy the workloads hosting requirements.
3. Select and test the available optinos that satisfy the workload requirements for latency, throughput, and response quality.
4. Implement the most appropriate, lower-cost hosting option for your model serving paradigm (for example, managed or self-hosted).

### Further reading

- Tagging Amazon Bedrock resources
- Inference cost optimization best practices
- Track, allocate and manage your generative AI cost and usage with Amazon Bedrock
- Optimizing costs of generative AI applications on AWS
- Analyze Amazon SageMaker AI spend and determine cost optimization opportunities based on

---

## GENCOST02-BP02 Optimize resource consumption to minimize hosting costs

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice describes a relationship between cost and performance contextualized in self-hosted foundation model hosting.

### Implementation guidance

Self-hosted model infrastructure should be optimized based on the model used and the workload's usage pattern. Customers self-hosting models should also consider optimizing the model's hosting infrastructure. Consider right-sizing the inference endpoint to the smallest instance available that allows you to meet performance goals. In some scenarios, it may be appropriate to shut down the hosting instance and restart it during relevant hours. This is particularly useful for workloads with predictable usage patterns. You may also consider purchasing Amazon EC2 Reserved Instances or Savings Plans to further reduce the cost of a hosted model endpoint. Before committing to compute reservation, consider Amazon SageMaker AI Inference Recommender to evaluate if you are using the ideal inference endpoint type, generation, and size.

In SageMaker AI HyperPod with both Amazon EKS and Slurm orchestration, use the system's advanced task governance capabilities and flexible training plans to dynamically allocate compute resources based on priority and demand, reducing costs through improved utilization.

For EKS-based HyperPod, implement the managed Kubernetes orchestration with Hyperpod Task Governance. Configure automated scaling policies, priority classes, and node selectors to verify that your production workloads use cost-effective committed capacity while development tasks use On-Demand or Spot Instances when appropriate. Use the usage reporting feature to provide granular visibility into GPU, CPU, and Neuron Core consumption at both team and task levels, enabling transparent cost attribution and reducing guesswork in resource allocation.

For Slurm-based HyperPod, use Slurm's native job scheduling and resource management features combined with HyperPod's auto-resume functionality to minimize wasted compute cycles during hardware failures, potentially reducing total training time in large clusters. Both systems benefit from implementing right-sizing strategies through SageMaker AI HyperPod Recipes that provide pre-configured, benchmarked training stacks optimized for specific model architectures like Llama and Mistral, providing optimized performance while minimizing resource waste.

Additionally, establish flexible training plans that can set timeline and budget constraints, and allow HyperPod to automatically find the best combination of capacity blocks and create cost- optimized execution plans that avoid overspending by overprovisioning servers for training jobs.

Inference workloads can be optimized using advanced techniques such as quantization or LoRA adaptation. These advanced capabilities are available for certain models in Amazon Bedrock or on self-hosted models on Amazon SageMaker AI. These advanced inference techniques can further optimize resource consumption for inference, thus reducing hosting and inference serving costs.

### Implementation steps

1. Identify the nature of the demand for this workload.
2. Deploy selected foundation model on acceptable infrastructure, even if it may be over- provisioned.
3. Establish an inference or demand profile for the hosted workload.
4. Optimize the hosting infrastructure in accordance with the workload's demands, and select the most cost optimized infrastructure that meets performance requirements.

### Further reading

- Tagging Amazon Bedrock resources
- Inference cost optimization best practices
- Get Started with Amazon SageMaker AI HyperPod Flexible Training Plans
- Easily deploy and manage hundreds of LoRA adapters with SageMaker AI efficient multi-adapter
- Track, allocate and manage your generative AI cost and usage with Amazon Bedrock
- Optimizing costs of generative AI applications on AWS
- SageMaker AI Inference Recommender for HuggingFace BERT Sentiment Analysis
- Analyze Amazon SageMaker AI spend and determine cost optimization opportunities based on
- Maximize Accelerator Utilization for Model Development with New Amazon SageMaker AI
- Introducing Amazon SageMaker AI HyperPod to train foundation models at scale

---

## GENCOST03-BP01 Optimize prompt token length

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practices encourages prompts to be as short as possible while meeting performance requirements.

### Implementation guidance

Whether your foundation model charges by tokens processed or not, prompt length can directly or indirectly contribute to the cost of inference. For self-hosted model infrastructure or provisioned throughput, longer prompts require increased computation time and increase the scale of infrastructure required to host your workload. For managed model infrastructure, the increased token count of longer prompts results in higher per-inference costs. Consider shortening prompts through rigorous testing. You may even use a separate large language model to shorten a prompt without reduction in performance. Reducing even a few tokens off the prompt contributes to cost optimization in the long-run.

### Implementation steps

1. Identify a verbose prompt which could be optimized.
2. Engineer the prompt to reduce the token count, trimming as many unnecessary words as possible.
3. Consider using a separate LLM to offer a shortened prompt that satisfies the end goal.
   - Amazon Bedrock Prompt Optimization can typically optimize prompt language to help provide consistent results.
4. Continue testing and optimizing the prompt to validate it meets the workload requirements.
   - Experiment with zero-shot prompting techniques for common knowledge tasks.
   - Consider chain-of-thought or tree-of-thought for logical reasoning.
   - Evaluate the benefits of least-to-most prompting for complex problems with nuanced solutions.
   - Research prompt engineering techniques to find the most cost-effective approach to your problem.

### Further reading

- AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on Amazon Bedrock (AIM377)
- Improve the performance of your Generative AI applications with Prompt Optimization on
- Amazon Bedrock Prompt Optimization Drives LLM Applications Innovation for Yuewen Group
- Amazon Bedrock Prompt Management is now Available in GA
- Prompt Engineering Guide

---

## GENCOST03-BP02 Control model response length

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practices encourages model responses to be as short as possible without sacrificing usability.

### Implementation guidance

Model response length should be kept as concise as possible, so long as it satisfies the use case. In Amazon Bedrock, consider specifying a response length hyperparameter to control and predict the upper-limit of the response length. Additionally, you may consider adding a phrase to your prompts which encourages the model to be succinct, further reducing the length of the model's response while encouraging the model to maintain a high degree of performance. Small optimizations in token count for model responses can improve model's generated output cost.

In scenarios where a full-text response is unnecessary, consider introducing determinism to the model. You might instruct the model to evaluate its response against a set of keyed options, returning the key which maps to the model's response. For example:

End of prompt template

If after carefully evaluating all of the information available to you that you respond in the affirmative, simply respond with the word True. Otherwise, respond False, providing a detailed explanation for your decision.

Such behavior as the one shown above encourages model responses to be succinct. Moreover, this behavior has the added benefit introducing determinism into the system for True responses.

### Implementation steps

1. Understand how the model response is to be used, defined a minimalist response scheme (for example, 0 for affirmative and 1 for rejection).
2. Inform the model in the prompt of the requested model response scheme, and ask the model to respond in kind.
3. Introduce a response length control to limit response tokens.
   - Set a hard limit on the response length by configuring the response length hyperparameter accordingly.
   - Extend the prompt template to encourage deterministic responses.
4. Set a hard limit on the response length by configuring the response length hyperparameter accordingly.
5. Continue testing and optimizing the model's response to verify it satisfies the workload requirements.

### Further reading

- AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on Amazon Bedrock (AIM377)
- Amazon Bedrock Prompt Management is now Available in GA

---

## GENCOST03-BP03 Implement prompt caching to reduce token costs

**Risk if not established:** Medium

**Desired outcome:** Reduce inference costs by caching commonly used prompt components and using cached tokens at a reduced rate.

### Implementation guidance

Prompt caching is an optional feature available on supported models in Amazon Bedrock that can reduce inference response latency and input token costs. By caching portions of your context, the model can use the cache to skip recomputation, allowing Bedrock to achieve cost savings through lower token rates.

Prompt caching can help when you have workloads with long and repeated contexts that are frequently reused across multiple queries. For example, if you have a chatbot where users can upload documents and ask questions about them, caching the document content avoids reprocessing it for each user query.

When using prompt caching, cached tokens are charged at a reduced rate. Depending on the model, tokens written to cache may be charged at a higher rate than uncached input tokens. Tokens not read from or written to cache are charged at the standard input token rate.

Cache checkpoints have model-specific minimum and maximum token requirements. You can only create a checkpoint if your prompt prefix meets the minimum token count. For example, Claude 3.7

Sonnet requires at least 1,024 tokens per checkpoint. The cache has a five minute TTL that resets with each successful hit.

### Implementation steps

1. Identify opportunities for caching:
   - Review workload for repeated prompt components
   - Verify prompts meet minimum token requirements
   - Assess potential cost savings from reduced token rates
2. Enable prompt caching for supported models:
   - Turn on caching in Amazon Bedrock console
   - For APIs, set appropriate caching flags
   - Configure cache checkpoints at optimal locations
3. Monitor caching metrics:
   - Track cache hit and miss rates
   - Monitor token costs for cached compared to uncached content
   - Analyze latency improvements
4. Optimize cache usage:
   - Tune checkpoint placement
   - Adjust prompt structure to maximize cache hits
   - Balance cache write costs with read savings

### Further reading

- Effectively use prompt caching on Amazon Bedrock
- Prompt caching for faster model inference
- Effectively use prompt caching on Amazon Bedrock
- Supercharge your development with Claude Code and Amazon Bedrock prompt caching
- Reduce costs and latency with Amazon Bedrock Intelligent Prompt Routing and prompt caching
- Amazon Bedrock Prompt Management is now Available in GA

---

## GENCOST03-BP04 Annotate user input to enable cost-aware content filtering

**Risk if not established:** Medium

**Desired outcome:** Enable more efficient and cost-effective content filtering by processing only the relevant portions of input that require guardrails evaluation.

### Implementation guidance

By implementing selective content filtering through input tags, you can significantly reduce token costs while preserving the effectiveness of your content safeguards. Please note that the input tags are not supported when using ApplyGuardrail API, so you need to implement content filtering on your application side to derive the benefits of input tags.

- Review your application architecture to identify where content filtering is needed.
- Determine which content sections require filtering or trusted content.
- Implement input tagging following the Amazon Bedrock documentation.
- Test filtering effectiveness and performance impact.
- Monitor costs and adjust tag usage to optimize spend while maintaining safety.

### Implementation steps

1. Use XML-style tags to mark specific sections of input prompts for content filtering. Add tags using the format:

<amazon-bedrock-guardrails-guardContent_xyz> [Content to be filtered] </amazon-bedrock-guardrails-guardContent_xyz>

Generate a unique random tag suffix (xyz) for each request to reduce prompt injection attacks. Use alphanumeric characters between 1-20 characters.

Include the tag suffix in the guardrailConfig:

{ "amazon-bedrock-guardrailConfig": { "tagSuffix": "xyz" } }

2. Apply tags selectively to user queries and input, current conversation turns, and new or unverified content.
3. Leave system prompts, verified search result, historical conversation context, and other trusted content untagged.
4. Define a minimalist response scheme (for example, 0 for affirmative and 1 for rejection).
5. Inform the model in the prompt of the requested model response scheme, and ask the model to respond in kind.
6. Set a hard limit on the response length by configuring the response length hyperparameter accordingly.
7. Continue testing and optimizing the model's response to verify it satisfies the workload requirements. Monitor and optimize your implementation by:
   - Tracking token usage with and without selective filtering
   - Measuring latency impact across different tag configurations
   - Verifying filtering effectiveness on tagged vs untagged content
   - Adjusting tag placement based on application needs

Example implementation

The following use cases are well-suited for input tagging:

- RAG applications: Tag only user queries while leaving retrieved passages unfiltered .
- Chat applications: Tag new user messages while preserving conversation history.
- Content moderation: Tag user-generated content while allowing verified content to pass through.
- Document processing: Tag extracted text portions needing review while trusting source material.

### Further reading

- AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on Amazon Bedrock (AIM377)
- Amazon Bedrock Prompt Management is now Available in GA
- GENCOST04-BP01 Reduce vector length on embedded tokens

---

## GENCOST04-BP01 Reduce vector length on embedded tokens

**Risk if not established:** Medium

**Desired outcome:** A reduced total cost of ownership for embeddings and data-driven generative AI workflows.

### Implementation guidance

Consider using a smaller vector when embedding documents into a vector store. The vector size hyperparameter specifies the size of the resulting vector when embedding unstructured data. A smaller resulting vector implies the embedding model will generate fewer tokens on output, thus resulting in a reduced cost to embed documents. This approach may result in less performant data retrieval, so using a smaller vector should be done deliberately with the cost-performance trade- off in mind.

Alternatively, some embedding models feature compressed vector types. Compressed vector types are smaller than uncompressed vectors, further reducing the cost of inference for search and embedding tasks. Consider this element when selecting an embedding model, as not all embedding models support compressed vectors.

### Implementation steps

1. Identify the smallest vector length supported by the selected embedding foundation model.
2. Embed data using the smallest vector length.
   - You may have to modify the chunk size of the document or introduce overlapping chunks to maintain high relevance on output.
3. Perform latency and load testing on your data retrieval workloads to verify that model response quality is still sufficient.
4. Re-test with increased vector size or modified document chunking strategy to improve model response quality.
   - In some cases, changing the search algorithm may improve model response quality as well.

### Further reading

- AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on Amazon Bedrock (AIM377)
- Amazon Bedrock Prompt Management is now Available in GA
- GENCOST05-BP01 Create stopping conditions to control long-running workflows

---

## GENCOST05-BP01 Create stopping conditions to control long-running workflows

**Risk if not established:** High

**Desired outcome:** Maximum costs for an agent's runtime can be predicted based on the implemented stopping conditions.

### Implementation guidance

For generative AI prompt flows where you lack control over the duration of the workflow, consider introducing a time-out mechanism or regaining control over the flow. This scenario is particularly common within agentic architectures. Agent architectures assist customers by taking on additional tasks. Sometimes these tasks can run for an extended duration, which may incur additional cost considerations, especially when they call external resources. Consider introducing a timeout over the agent to limit long-running processes from incurring costs unnecessarily. Additionally, evaluate asynchronous workflows orchestrated through events. Asynchronous workflows create opportunities to interrupt or halt long-running events after an extended duration. Consider the entire architecture before determining the best place to interrupt long-running workflows for cost savings.

### Implementation steps

1. Estimate the maximum time needed for an agent to complete its runtime.
   - Include model response times, tool execution times, and network latency in the estimation.
2. Implement stopping conditions that enable an agent to run to the maximum duration.
   - Stopping conditions may be a timeout mechanism like the one in Amazon Bedrock.
   - Alternatively, stopping conditions may be implemented in the prompt flow layer or within a software abstraction layer.
3. Re-architect your workflows to facilitate stopping conditions.
   - Set timeouts on external tools such as Lambda functions or API endpoints, verify that your prompts understand how to handle timeout responses.
   - Set token limits on model responses to simulate timeout functionality by stopping models from printing long-running responses.

### Further reading

- AWS re:Invent 2023 - Simplify generative AI app development with Agents for Amazon Bedrock
- User Guide: Amazon Bedrock Agents
- Best practices for building robust generative AI applications with Amazon Bedrock Agents - Part
- Best practices for building robust generative AI applications with Amazon Bedrock Agents - Part
- Identify if generative AI is the right solution: Always ask if generative AI is right for your
- Design for environmental efficiency: Select and deploy generative AI components with
- Implement dynamic resource optimization: Deploy infrastructure that automatically adjusts
- Energy-efficient infrastructure and services
- Consume sustainable data processing and storage services
- Consume energy efficient models

---
