# Generative AI Lens — foundations

Design principles, Responsible AI dimensions, the generative AI lifecycle, data architecture and agentic patterns from the *AWS Well-Architected Framework — Generative AI Lens* (2026). Read this when a review needs framing beyond the individual best practices: which lifecycle stage the workload is in, which Responsible AI dimensions are in play, or what the Lens means by a term.

## Design principles

The following design principles apply to generative AI workloads created on AWS:

- Design for controlled autonomy: Implement comprehensive guardrails and boundaries that govern how AI systems operate, scale, and interact. By establishing clear operational requirements, security controls, and failure conditions, you can keep AI systems within safe, efficient, and cost-effective parameters while maintaining reliability. This principle addresses security, cost optimization, and reliability concerns for autonomous AI operations.
- Implement comprehensive observability: Monitor and measure specific aspects of your generative AI system, from security and performance to cost and environmental impact. By collecting metrics across every layer, including user feedback, model behavior, resource utilization, and security events, you can maintain operational excellence while optimizing system behavior. This holistic approach enables data-driven decisions about system improvements and rapid problem resolution.
- Optimize resource efficiency: Select and configure AI components based on empirical requirements rather than assumptions. By right-sizing models, optimizing data operations, and implementing dynamic scaling, you can balance performance needs with cost and sustainability goals. This principle helps you achieve efficient resource utilization while maintaining necessary capabilities and reducing environmental impact.
- Establish distributed resilience: Design systems that remain operational despite component or regional failures. By implementing redundancy, automated recovery mechanisms, and geographic distribution of resources, you can maintain consistent service delivery while managing costs and performance. This helps you achieve reliability while supporting efficient global operations.
- Standardize resource management: Maintain centralized catalogs and controls for critical components like prompts, models, and access permissions. By implementing structured management systems, you can maintain security, govern resource usage, enable version control, and optimize costs while maintaining operational excellence.
- Secure interaction boundaries: Protect and control data flows and system interfaces. By implementing least-privilege access, secure communications, input/output sanitization, and comprehensive monitoring, you can maintain system security while achieving reliable and efficient operations. This principle addresses security requirements while supporting overall system integrity.

## Responsible AI

As with any new technology, generative AI creates new challenges as well. Potential users must evaluate the promise of the technology while also analyzing the risks. Responsible AI is the practice of designing, developing, and using AI technology with the goal of maximizing benefits and minimizing risks. At AWS, we define responsible AI using a core set of dimensions that we assess and update over time as AI technology evolves:

- Fairness: Considering impacts on different groups of stakeholders.
- Explainability: Understanding and evaluating system outputs.
- Privacy and security: Appropriately obtaining, using, and protecting data and models.
- Safety: Reducing harmful system output and misuse.
- Controllability: Having mechanisms to monitor and steer AI system behavior.
- Veracity and robustness: Achieving correct system outputs, even with unexpected or adversarial inputs.
- Governance: Incorporating best practices into the AI supply chain, including providers and deployers.
- Transparency: Enabling stakeholders to make informed choices about their engagement with an AI system.

Elements of the Responsible AI framework are weighted more heavily for generative AI systems as opposed to traditional machine learning solutions (like veracity or truthfulness). However, the implementation of Responsible AI requires a systematic review of the system along the defined dimensions.

Responsible AI: Aligning innovation with your mission The promise of generative AI represents one of the most significant opportunities for business transformation in decades. As organizations race to harness this technology, the most successful implementations share a common thread: they align AI capabilities with organizational principles and values from day one.

For example, take a financial services company envisioning the next generation of customer experience. You see the potential to offer personalized 24/7 financial guidance, instantly process

loan applications, and provide sophisticated investment advice at scale. The opportunity is compelling: reduced operational costs, enhanced customer satisfaction, and the ability to serve industries previously unreachable through traditional channels.

This transformation is achievable, but success depends on building with intention. At AWS, we've identified eight key dimensions that help organizations implement AI solutions that not only drive business value but also align with their organizational missions:

Fairness

When your AI system interacts with customers, those interactions reflect your brand values. Consider a mortgage application system: it must evaluate applications based on relevant financial criteria while verifying that decisions aren't influenced by unwanted discriminatory factors. This means implementing robust testing frameworks to detect potential bias, regularly auditing outcomes across different customer segments, and maintaining clear documentation of decision criteria. Leading organizations are integrating these considerations into their development processes, which means that their AI systems enhance rather than compromise their commitment to equitable service.

Explainability

The ability to understand and communicate how AI makes decisions is both a good practice and is essential for business operations. A wealth management AI advisor must be able to articulate the reasoning behind its investment recommendations. This requires implementing interpretability techniques and developing frameworks to translate complex model decisions into understandable explanations for both customers and regulators. Organizations that excel here find they build deeper customer trust and navigate regulatory requirements more effectively.

Privacy and security

Customers want to trust generative AI applications with their most sensitive information. This trust is earned by strong application security and data privacy controls. When implementing AI systems, this trust must be preserved through robust data protection and infrastructure security mechanisms. Leading organizations are implementing sophisticated data governance frameworks that include encryption, access controls, and data minimization practices. They also develop clear policies about data usage, verify that AI systems access only the information necessary for their specific functions, and seek to maintain regulatory compliance.

Safety AI systems must operate within a clearly defined use case scope that aligns with your organization's risk tolerance and values. Consider a trading recommendation system: it needs guardrails to remove suggestions that could violate regulatory requirements or exceed risk thresholds. Forward- thinking organizations are implementing comprehensive safety frameworks that include content filtering, output validation, and clear escalation paths for edge cases.

Controllability The ability to monitor and adjust AI system behavior aligns with business objectives and risk parameters. Leading organizations implement robust monitoring systems that track performance metrics, user feedback, and system outputs. They maintain clear procedures for adjusting or disabling AI systems when necessary, keeping human oversight effective even as systems scale.

Veracity and robustness AI systems must deliver reliable, veratious results consistently, even when facing unexpected situations. Organizations at the forefront of AI adoption are implementing comprehensive testing frameworks that challenge their systems with diverse inputs, monitoring accuracy across different scenarios, and maintaining clear protocols for handling edge cases. They're building systems that not only perform well in ideal conditions but remain reliable under stress. At the forefront of this field are concepts like automated reasoning, which use mathematically provable statements to capture and correct hallucinations in real-time.

Governance Clear governance frameworks align AI systems with organizational policies and regulatory requirements. Leading organizations are establishing AI governance committees that include technical, business, and risk management perspectives. They're developing comprehensive documentation practices, clear escalation paths, and regular review processes so that AI systems continue to serve business objectives while managing risk effectively.

Transparency Building trust requires openness about AI system capabilities and limitations. Successful organizations clearly communicate when and how AI is being used, what data informs decisions, and what controls are in place. This commitment to transparency enhances user trust in the AI system, encouraging adoption.

The path to sustainable AI innovation Organizations that embrace these dimensions from the start are achieving remarkable results. They're deploying AI solutions faster because governance frameworks are already in place. They're scaling more effectively because they've built trust with stakeholders. Most importantly, they're creating sustainable competitive advantages by aligning AI capabilities with their organizational missions.

This is more than risk management. It's about building AI systems that create lasting value while strengthening your organization's reputation and relationships with stakeholders. As you embark on your AI journey, consider how these dimensions can help you build solutions that don't just perform well technically, but truly advance your organization's mission and values.

The opportunity is clear: by implementing responsible AI practices from day one, you position your organization to lead in the AI-enabled future, building solutions that drive innovation while maintaining the trust that is fundamental to long-term success.

Moving forward Assess how these dimensions align with your organization's values and objectives. Engage stakeholders across functions to develop frameworks that support rapid innovation while verifying that AI implementations strengthen rather than compromise your mission. The foundation you establish today determines how effectively you can scale and innovate with AI.

References

- AWS Responsible AI Policy
- Responsible AI Best Practices: Promoting Responsible and Trustworthy AI Systems
- Amazon AI Fairness and Explainability Whitepaper
- AWS generative AI Best Practices Framework
- AWS Responsible AI Landing Page

## Generative AI lifecycle

The generative AI lifecycle consists of seven key phases: scoping, model selection, model customization, development and integration, deployment, and continuous improvement. Each phase of the generative AI lifecycle is evaluated against the six pillars of the Well-Architected Framework. This process helps verify that workloads are built and maintained according to best practices across critical aspects of system design and operation.

Generative AI lifecycle

Scoping The scoping phase prioritizes understanding the business problem. The initial scoping phase refers to the stage where the project's goals, requirements, and potential use cases are clearly defined. This sets the foundation for the development process by identifying a high-impact, feasible application, aligning stakeholders to the project's goals, and determining how success is measured. A robust scoping phase can significantly improve the chances of the project delivering valuable outcomes, which streamlines development by focusing efforts on the most critical aspects of the project.

The primary focus of the scoping phase should be to determine the relevance of generative AI in solving the problem. Consider the risks and costs of investment for generative AI to solving that problem. Self-assess with questions like:

- What kinds of models do we need to consider?
- Will an off-the-shelf model satisfy the requirements of this business problem or will there be a need to customize the model?
- Does one single model address the problem, or will there be a need for several models in an orchestrated workflow?

Cost considerations for a sustainable solution are critical to consider at this stage as well. Many components can introduce additional costs to a generative AI workload, like prompt lengths, data architecture and access patterns, model selection, and agent orchestration.

Establish the success metrics for how to measure and evaluate the model's performance. Determine the technical and organizational feasibility of the proposed project. Develop a comprehensive risk profile for the proposed generative AI solution. Discuss technology risks as well as business risks. If applicable, assess the availability and quality of data needed to customize the model. Create security scoping matrices for different use cases. By clearly outlining project goals early on, you can avoid misunderstandings and verify that everyone is working towards the same objectives.

Model selection The model selection phase prioritizes the selection and adoption of a generative AI model. This phase involves evaluating different models based on your specific requirements and use cases.

During the selection process, consider various tools and components, including choosing between different model hosting options. Different workloads may benefit most from batch inference, real- time inference, or a combination of inference profiles. To accommodate model selection, make several options available in the form of a model routing solution, use a model catalog to quickly onboard new models, and architect model availability solutions.

Determine which model best aligns with your desired functionalities and performance metrics. During selection, consider factors like modality, size, accuracy, training data, pricing, context window, inference latency, and compatibility within your existing infrastructure. Understand data usage policies by model hosting providers. If you are using SageMaker AI for training or hosting, you should evaluate instance types for model deployment. If RAG will be used, consider the selection and availability requirements for vector databases. In some cases, you may need to train your own model from scratch based on your unique requirements. Pre-training foundations models from scratch are out of scope for this document.

Model customization The model customization phase aligns the model with the application's goals. Model customization is a process of taking a pre-trained model and customizing it to fit the particular use case by using techniques like prompt engineering, RAG, agents, fine-tuning, continuous pre-training, model distillation, and human feedback alignment. These are some popular model customization techniques, and you can use some or all of these techniques in the process of developing a generative AI workload. These techniques transform a generic model into a solution tailored to the specific data, context, and user expectations of the application. This process is iterative and involves continuous refinement and evaluation to verify that the model performs accurately and ethically within the defined context.

Craft prompts to guide the model towards generating the desired outputs. Implement template management for prompts. If needed, train the model on additional data relevant to the specific application to improve its performance on that domain. Incorporate human feedback to refine the model's behavior and align it with desired ethical and quality standards. This improves the quality of outputs and helps you tailor the model to the specific needs of the user and application, which enhances the model's ability to produce accurate and relevant results within the specified context. Allow for proactive mitigation of potential biases or undesired outputs by aligning the model with the desired ethical guidelines.

Development and integration The development and integration phase integrates the developed model into an existing application or system, which makes it fully functional and ready for production use. This process includes optimizing the model for inference, orchestrating agent workflows, fueling RAG workflows, and building user interfaces. At this stage, you will bridge the gap between a trained model and its practical application and make the model ready to be used effectively in a real-world scenario.

Implement the selected model into your workflow by incorporating components like conversational interfaces, prompt catalogs, agents, and knowledge bases. To integrate with existing systems or applications, connect the model to relevant databases, data pipelines, and other applications within the organization. Implement security measures and responsible AI practices, such as guardrails, to reduce risks common to generative AI, such as hallucination.

Optimize the model to perform efficiently in real-time inference within the target application hardware. This may include further fine-tuning models, implementing model distillation techniques, and making ongoing adjustments based on performance metrics. Verify the model can handle increasing workload demands and maintain consistent performance under production conditions. Validate that complimentary application components feature scalable and reliable performance as well.

Allow other applications to interact with the model by creating application programming interfaces (APIs). Build or use an existing user-friendly interface for interacting with the model, including input prompts and output display mechanisms. A well-designed user interface and seamless integration can significantly improve user adoption. Validate how well the integrated components work together with automated testing, and make necessary adjustments to improve overall system performance. As you prepare the production environment, establish monitoring systems to track performance and identify potential issues.

Deployment The deployment phase rolls out the generative AI solution in a controlled manner and scales it to handle real-world data and usage patterns. At this stage, the model is moved from a development environment to production, making it accessible to users by integrating it into an application or system. This involves setting up the necessary infrastructure to serve predictions and monitor its performance in real-world scenarios.

Deployment includes implementing CI/CD pipelines where applicable, helping maintain system uptime and resiliency, and managing the day-to-day running of the system. Infrastructure as code (IaC) principles are often employed using tools like AWS CDK, AWS CloudFormation, or Terraform to manage resources. Version control systems and automated pipelines are crucial for maintaining and updating the system. Documentation and versioning of infrastructure components help maintain system stability and enable quick rollbacks if needed. Validate your adherence with security and privacy requirements.

Continuous improvement The final phase involves continuous improvement of the system. This refers to the ongoing process of monitoring a deployed model's performance, collecting user feedback, and making iterative adjustments to the model to enhance its accuracy, quality, and relevance over time. Continuous improvement aims to constantly refine the system based on real-world usage and new data. Invest in ongoing education and training for teams. Stay updated on advancements in generative AI, and regularly reassess and update your AI strategy.

To review performance monitoring, track key metrics like accuracy, toxicity, and coherence of the generated outputs to identify areas for improvement. To identify biases or areas where the model needs adjustments, gather feedback from users regarding the quality and usefulness of the generated outputs. Update the training data set with new examples or refined data based on user feedback to improve model performance. As user needs and the data landscape evolve, continuously improve the model to stay relevant and effective. Enhance quality with regular refinement to mitigate biases and improve the generated outputs. Experiment with new techniques by exploring new algorithms, architectures, or training methods to potentially further enhance the overall solution.

## Data architecture

Organizations might need to reimagine their data strategies to unlock the transformative potential of generative AI, moving beyond traditional data management to create dynamic, AI- ready data environments that enable rapid experimentation, personalization, and innovation at scale. As enterprises strive to capture value from generative AI, data has emerged as the strategic differentiator. Gen AI models thrive on high-quality, context-rich, and well-governed data. However, issues like fragmented data environments, inconsistent governance, and unclear ownership slow down generative AI experimentation and scale. A deliberate data strategy is essential to accelerate generative AI innovation while mitigating data risks.

The value driven from generative AI applications depends on the ability to use both structured and unstructured data. The exponential growth of unstructured data creates a challenge for data leaders to make this data usable. Identifying, classifying, and organizing unstructured data with the wide variety of formats and volumes creates complexity in data management environments and can lead to security risks, cost overheads, and issues with storage, interpretation, and compliance. Maintaining quality, accuracy, and authorized access further adds to the challenges of data management landscape. These considerations together with the need to use unstructured data for generative AI led to a quest for next-generation data strategies.

There are three primary use cases for data in generative AI: pre-training, customization, and retrieval-augmented generation (RAG).

Pre-training data architecture involves managing and processing vast, diverse datasets, often requiring petabytes of data and scalable computational resources capable of handling such large volumes of data. It demands highly scalable infrastructure to handle enormous data volumes efficiently. Key challenges include data quality management across diverse sources of largely unstructured data, efficient storage and retrieval of large-scale datasets, and the computational resources required for processing. Pre-training architectures must also consider data versioning, privacy protection for broad datasets, and sustainable practices for long-term data storage and processing.

Fine-tuning and model customization data architecture focuses on adapting pre-trained models to specific tasks or domains, typically using smaller, more focused datasets. This requires flexible architectures that can efficiently handle varying data sizes and types. Fine-tuning, including techniques like continuous pre-training, presents unique challenges in data selection and curation, increasing dataset quality and relevance, and reducing potential biases. Architectures for fine-

tuning must support rapid iteration, efficient data preprocessing, and careful versioning to track the relationship between datasets and model performance.

Retrieval-Augmented Generation (RAG) data architectures combine pre-trained models with dynamic retrieval from external knowledge bases. This approach demands low-latency data retrieval systems and seamless integration of external knowledge with model inference. RAG architectures need to address requirements such as efficient indexing of large knowledge bases, real-time data retrieval, and maintaining up-to-date information. They also need to consider privacy and security in accessing and using external data sources during inference.

Across these use cases, key considerations in generative AI data architecture include:

- Scalability to handle massive, diverse datasets
- Efficiency in data storage, retrieval, and processing
- Security and privacy protection for sensitive data
- Data quality management and bias mitigation
- Versioning and lineage tracking for reproducibility
- Cost-effective, sustainable data management practices

Strategic imperatives Data quality as the foundation

High quality, well-structured data is the bedrock of effective generative AI. Organizations must establish comprehensive data governance frameworks that maintain accuracy, completeness, and consistency across all data sources. This includes implementing automated data validation, cleansing processes, and continuous monitoring to maintain data integrity at scale.

Unified data architecture

Break down data silos by creating a unified data system that integrates structured and unstructured data from across the organization. Modern data architectures should support real- time data ingestion, processing, and delivery while maintaining security and helping you comply with regulatory standards. Cloud solutions enable the scalability and flexibility required for AI workloads.

To harness a broad information base for building AI models and AI-driven decision making, organizations must find ways to address data silos and enable unified access to data, independent

of where it resides. Unstructured data, in particular, poses a unique set of challenges. While it is critical to AI success, it remains difficult to ingest, store, process and govern. Overcoming these challenges requires scalable data stores capable of handling the volume and velocity of unstructured data. Additionally, there is a need for efficient methods to unify, curate, and prepare data efficiently across hybrid cloud environments.

Privacy-first approach

Implement privacy-by-design principles that protect sensitive information while enabling AI innovation. This includes techniques such as differential privacy, federated learning, and synthetic data generation. Organizations must balance data utility with privacy protection and help them comply with regulations like GDPR and CCPA.

Implementation framework Data democratization: Enable self-service data access for AI teams through intuitive data catalogs, automated data discovery, and standardized APIs. Empower business users and data scientists to find, understand, and use data without extensive IT intervention. This accelerates time-to-insight and reduces bottlenecks in AI development cycles.

Real-time data streaming: Implement streaming data architectures that support real-time AI applications. This enables use cases such as dynamic content generation, real-time personalization, and immediate response systems. Modern streaming services should handle high-velocity data while maintaining low latency and high availability.

Multimodal data integration: Prepare for AI models that work with text, images, audio, and video by creating unified storage and processing capabilities for multimodal data. This includes developing standardized metadata schemas, content indexing systems, and cross-modal search capabilities that enable AI systems to understand and generate diverse content types.

Key success factors Scalable infrastructure: Build elastic data infrastructure that can handle varying AI workloads and data volumes. This includes distributed storage systems, auto-scaling compute resources, and optimized data pipelines that can adapt to changing demands. Cloud-native architectures provide the flexibility and cost-effectiveness required for AI at scale.

Data observability: Implement comprehensive monitoring and observability tools that provide visibility into data quality, pipeline performance, and AI model behavior. This includes data lineage

tracking, anomaly detection, and performance metrics that enable proactive issue resolution and continuous improvement.

Cross-functional collaboration: Foster collaboration between data teams, AI engineers, and business stakeholders through shared services, common vocabularies, and aligned incentives. Create centers of excellence that promote best practices, knowledge sharing, and standardized approaches to AI development and deployment.

Measuring success: Organizations should track key performance indicators including data quality scores, time-to-model deployment, AI application performance metrics, and business value generated from AI initiatives. Regular assessment of data strategy effectiveness helps you continuously improve and align with evolving business needs.

A well-executed data strategy is the catalyst that transforms generative AI from experimental technology into a core business capability. Organizations that invest in robust data foundations, embrace privacy-first approaches, and foster data-driven cultures will gain sustainable competitive advantages in the AI-powered future. By addressing these requirements through well-designed data architecture, organizations can build more powerful, reliable, and responsible generative AI systems.

The following sections explore these considerations in depth and provide guidance aligned with the Well-Architected Framework's six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

## Agentic AI

AI agents are autonomous entities that are capable of perceiving their environment, reasoning, and taking actions to achieve defined goals. Agents can interact with users, services, and other agents in complex, real-time environments. In generative AI, the core of an agentic system is usually a large language model (LLM), augmented with capabilities like retrieval (access to information), tools (interacting with its environment), and memory. The term agentic derives from agency (the ability to act independently, make decisions, and take actions within its environment). Agentic systems can have varying degrees of agency, ranging from making narrowly scoped actions to autonomously orchestrating themselves. When designing an agentic system, it's important to only increase the agency of the system when the task complexity requires it.

In this section of the Generative AI Lens, we'll discuss a few of the common agentic patterns we see in practice.

LLM-augmented workflows LLM-augmented workflows are systems where code paths are largely deterministic, with certain steps augmented with LLMs to make decisions. An example is simplistic document processing system. It might classify an incoming document as simple or complex and use tool calls to route the document to the correct path. It has a low degree of agency, but is still an agentic system as a whole because it's making decisions through tool invocations.

Autonomous agents The architecture of an autonomous agent is simple. These systems are typically built around an LLM that has been augmented with retrieval, tools, and memory orchestrated in a loop. This is commonly referred to as a ReACT (reason and act) loop. An agent is given a list of tools with instructions on how to use them and is orchestrated in a loop until the LLM is given a stop reason. These tools can be internal APIs, connections to data sources, or simple functions. Tools are often connected to the agent using the MCP protocol, and the LLM provides the agent with the reasoning capabilities needed to select the appropriate tool. The guidelines informing this reasoning capability are traditionally described in the system prompt, which should outline the goal, role, and other details the LLM needs to properly reason.

Hybrids In practice, many agentic systems use both workflows and autonomous agents with varied levels of agency. An example is the plan and solve loop which has a high degree of agency.

First, we use an LLM to create a plan and a task breakdown. The plan and task list are informed by the agent's system prompt, which broadly describes how the LLM should reason on the agent's behalf.

That task list gets fed into a queue and we use a series of ReACT agents to resolve those tasks.

When the task list is complete, we use another call to an LLM to decide if we have enough to return to the user or need to add more tasks to complete the users request.

This pattern could be scaled out using queues, auto-scaling, and asynchronous executions.

Conclusion As we navigate the evolving landscape of generative AI, the agentic paradigm represents a fundamental shift in how we architect intelligent systems. From simple LLM-augmented workflows to fully autonomous agents, these patterns enable us to build solutions that can perceive, reason, and act within their environments with varying degrees of agency. The key insight for practitioners is that agency exists on a spectrum. Our architectural choices should align the level of autonomy with the complexity of the problem at hand.

As agentic AI continues to mature, we anticipate these patterns will evolve and new architectures will emerge. The principles of well-architected design (reliability, security, performance efficiency, cost optimization, sustainability, and operational excellence) remain paramount as we build systems that act on our behalf. The future of generative AI is increasingly agentic, and mastering these architectural patterns today prepares us for the autonomous systems of tomorrow.

## Definitions

- Agent: An AI system that can perform tasks autonomously and interact with its environment to achieve specific goals.
- Bias and fairness testing: Evaluating and mitigating potential biases or unfair outcomes from AI models, particularly in areas like gender, race, or age.
- Continuous pre-training: The process of continuously updating a pre-trained model with new data to improve its performance and adapt to evolving domains or tasks.
- Chunking: Breaking up large data files into small, discreet chunks to allow the foundation model to fit that data into a context window.
- Data management: The process of identifying, collecting, storing, aggregating, searching, tracking, governing, and using data.
- Embedding: Transforms chunks of data into vectors that represent semantic meaning.
- Fine-tuning: The process of adapting a pre-trained model to a specific task or domain by training it on a smaller, task-specific dataset.
- Foundation models: Large language models pre-trained on vast amounts of data, serving as a foundation for downstream tasks and fine-tuning.
- Foundation model providers: Companies or organizations that develop and release foundation models for use by others.
- Generative AI: AI systems capable of generating new content, such as text, images, or code, based on input data or prompts.
- Hallucination: A phenomenon where a generative AI model produces outputs that are inconsistent, factually incorrect, or unrelated to the input prompt.
- Human oversight: Mechanisms for human experts to review, validate, and control critical decisions or outputs from AI models.
- Indexing: Process of inserting embedded chunks into a vector data store.
- Knowledge graph: A structured representation of real-world entities and their relationships, used to enhance the contextual understanding and reasoning capabilities of AI systems.
- LLMOps or GenAIOps: Operational practices and principles for managing the lifecycle of large language models (LLMs), including model selection, data preparation, deployment, monitoring, and governance.
- Model card: A document that provides key information about a machine learning model, including its intended use, training data, performance characteristics, and potential limitations or biases.
- Model customization: The process of modifying a foundation model using various techniques to control its behavior.
- Model distillation: A technique for creating a smaller, more efficient model that mimics the behavior of a larger, more advanced model.
- Model evaluation: The process of assessing the performance, robustness, and other characteristics of language models using various metrics and techniques.
- Model gateway: An interaction layer offering secure access to the model hub through standardized APIs.
- Model hub: A central repository providing access to enterprise foundation models from first- party, third-party, and open-source providers.
- Model interpretability: The ability to understand and explain the reasoning behind a model's outputs, increasing transparency and interpretability.
- Model orchestration: Encapsulation of multistep workflows which are characteristic of generative AI workflows.
- Pre-Training: Building a foundation model from scratch. Requires GPU clusters to run continuously for weeks.
- Prompt catalog: A centralized repository for storing, managing, and versioning prompts used to interact with generative AI models.
- Prompt engineering: The practice of carefully crafting prompts to guide language models to produce desired outputs.
- Provisioned throughput: Feature of Amazon Bedrock that allows you to provision a higher level of throughput at a fixed cost for predictable, high-throughput workloads.
- Quantization: Techniques for reducing the precision of model parameters, thereby decreasing the memory footprint and computational requirements.
- Responsible AI: The practice of developing and deploying AI systems in a manner that prioritizes fairness, transparency, accountability, and adherence to ethical principles.
- Retrieval-Augmented Generation (RAG): A technique/architectural style where a language model's output is augmented with relevant information retrieved from a corpus of documents. This technique is employed to make sure the responses are grounded with the documents and to reduce hallucination.
- Self-hosted models: AI models that are deployed and managed by the organization using them, rather than relying on a third-party provider.
- Serverless architecture: An architecture pattern where the cloud provider automatically manages the allocation and provisioning of computational resources, allowing for scalability and cost optimization.
- Tokenization: The process of breaking down input text into smaller units called tokens, which can be words, subwords, or characters, as a preprocessing step for natural language processing tasks.
- Vector store: A specialized data store for efficient storage and retrieval of high-dimensional vector embeddings, often used in semantic search and retrieval tasks. Vector stores such as Amazon OpenSearch Service serverless support different search algorithms.
- Zero-shot learning: The ability of a model to perform a task or make predictions on examples it has never seen before, without requiring task-specific training data.

For the latest AWS terminology, see the AWS glossary in the AWS Glossary Reference.
