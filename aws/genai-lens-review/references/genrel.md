# Reliability — Generative AI Lens best practices

Source: *AWS Well-Architected Framework — Generative AI Lens* (2026). 10 best practices in this pillar.

## Contents

- [GENREL01-BP01]( #genrel01-bp01 ) Scale and balance foundation model throughput as a function of utilization — risk if absent: **Medium**
- [GENREL02-BP01]( #genrel02-bp01 ) Implement redundant network connections among model endpoints and supporting infrastructure — risk if absent: **Medium**
- [GENREL03-BP01]( #genrel03-bp01 ) Use logic to manage prompt flows and gracefully recover from failure — risk if absent: **Medium**
- [GENREL03-BP02]( #genrel03-bp02 ) Implement timeout mechanisms on agentic workflows — risk if absent: **High**
- [GENREL04-BP01]( #genrel04-bp01 ) Implement a prompt catalog — risk if absent: **Medium**
- [GENREL04-BP02]( #genrel04-bp02 ) Implement a model catalog — risk if absent: **Low**
- [GENREL05-BP01]( #genrel05-bp01 ) Load-balance inference requests across all regions of availability — risk if absent: **Medium**
- [GENREL05-BP02]( #genrel05-bp02 ) Replicate embedding data across all regions of availability — risk if absent: **Medium**
- [GENREL05-BP03]( #genrel05-bp03 ) Verify that agent capabilities are available across all regions of availability — risk if absent: **Medium**
- [GENREL06-BP01]( #genrel06-bp01 ) Design for fault-tolerance for high-performance distributed computation tasks — risk if absent: **High**

---

## GENREL01-BP01 Scale and balance foundation model throughput as a function of utilization

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by matching the configured or provisioned throughput to your foundation models to the workload's demand. This results in optimal resource utilization and consistent performance under varying loads.

### Implementation guidance

When managing throughput for foundation models, consider implementing a comprehensive monitoring and scaling strategy. Use a robust monitoring system that provides detailed insights for tracking throughput metrics and creating alarms for quota utilization.

To handle traffic spikes and maintain consistent performance, implement request buffering using a message queue service, which can help smooth out irregular traffic patterns and avoid overwhelming the model endpoints. Use a service quota management system to adjust service limits based on your workload requirements, while implementing auto-scaling mechanisms to enable dynamic capacity management based on demand.

Consider placing queues between generative AI applications and models so that models do not deny or drop requests due to throughput constraints. This architecture lends itself to event-driven messaging patterns, making it a particularly robust option for architectures with high demand.

For handling common throughput bottlenecks, consider implementing token bucket algorithms for rate limiting or using provisioned throughput options when dealing with token rate limits. To address concurrent request limits, implement request queuing or distribute requests across multiple Regions. For model loading overhead, maintain a warm pool of model instances or implement model caching strategies. Each of these solutions should be monitored for effectiveness using your chosen metrics and monitoring system.

Provisioned Throughput endpoints or cross-Region inference profiles on Amazon Bedrock may help to alleviate scaling bottlenecks for fully-managed inference hosting. Provisioned Throughput provides dedicated infrastructure that can achieve higher, more stable throughput than allowed through default quotas for on demand models hosted on Amazon Bedrock. Provisioned Throughput capacity can be monitored in Amazon CloudWatch, which helps you proactively scale when capacity nears critical thresholds.

Cross-Region inference profiles distribute inference demand over a region of availability. For model endpoints hosted on Amazon SageMaker AI Inference Endpoints, consider using traditional throughput scaling techniques like EC2 Autoscaling groups behind a load balancer. If your increased throughput needs are periodic and predictable, consider deploying larger instance types in advance of the increased need. Ultimately, it is encouraged to proactively engage with AWS support to increase service quotas based on known workload demands.

### Implementation steps

1. Set up comprehensive monitoring using CloudWatch:
   - Create custom dashboards for throughput metrics
   - Configure alarms for quota utilization
   - Enable detailed monitoring for critical resources
2. Implement request management:
   - Deploy queue-based architecture for request buffering
   - Set up rate limiting at the application layer
   - Configure retry mechanisms with exponential backoff
3. Configure scaling mechanisms:
   - Set up auto-scaling policies based on demand
   - Configure provisioned throughput where appropriate
   - Implement cross-region request distribution
4. Establish ongoing optimization:
   - Regular review of utilization patterns
   - Periodic adjustment of quotas and scaling parameters
   - Continuous monitoring and refinement of thresholds

### Further reading

- Increase throughput with cross-Region inference
- Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock
- Enable Amazon Bedrock cross-Region inference in multi-account environments
- Building well-architected serverless applications: Regulating inbound request rates - part 1
- Getting Started with cross-Region inference in Amazon Bedrock
- GENREL02-BP01 Implement redundant network connections among model endpoints and

---

## GENREL02-BP01 Implement redundant network connections among model endpoints and supporting infrastructure

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by reducing the likelihood of performance degradation due to network issues.

### Implementation guidance

Implement network connection redundancy between components in your generative AI application to provide high availability and fault tolerance. This involves creating multiple network paths between critical components, using technologies such as multi-AZ deployments, cross-Region connectivity, and software-defined networking. Consider implementing load balancers to distribute traffic across redundant connections and automatically route around failures.

Deploy your generative AI application across multiple subnets within a VPC. Use AWS PrivateLink or a similar network technology to facilitate secure, private network communications between VPC-hosted applications and other AWS services. Use a multi-AZ architecture, with applications deployed across at least two Availability Zones.

In addition to deploying applications with high availability, deploy vector databases and agentic systems across multiple Availability Zones as well. With vector database solutions like Amazon OpenSearch Service Serverless, you can configure your OpenSearch cluster deployment across multiple Availability Zones, creating VPC Endpoints to have reliable network connectivity to the cluster.

Similar considerations should be extended to agentic workflows. On Amazon Bedrock, agent workflows make calls to API endpoints and AWS Lambda functions. Consider deploying these capabilities in a multi-AZ deployment as well.

infrastructure

For multi-Region deployments, implement a global traffic management solution to route requests to the nearest available endpoint. Use private network connections where possible to improve security and reduce latency. Implement automatic failover mechanisms to reroute traffic in case of network issues. Continue deploying resources into VPCs, but consider using one of the various multi-Region VPC communication services to facilitate secure, reliable network connectivity for your services and applications.

Use network configuration tools like VPC peering, AWS Transit Gateway, or Amazon VPC Lattice to connect your applications and services in VPCs across Regions. Consider combining this capability with Amazon Bedrock's cross-Region inference capabilities for high availability network connectivity across Regions.

### Implementation steps

1. Identify critical network paths in your generative AI architecture:
   - Map dependencies between foundation models, databases, and other components
   - Determine required bandwidth and latency for each connection
2. Design redundant network topology:
   - Implement multi-AZ deployments for high availability
   - Set up cross-Region connectivity for disaster recovery
   - Configure load balancers for traffic distribution
3. Implement private networking:
   - Use VPC peering or transit gateways for secure inter-component communication
   - Set up VPN or direct connect for on-premises integration if required
4. Configure automatic failover:
   - Implement health checks for network paths
   - Set up automated failover mechanisms using DNS or overlay networking
5. Test and validate redundancy:
   - Conduct failure simulations to verify failover effectiveness
   - Perform regular failover drills to verify operational readiness

### Further reading

- Securely Access Services Over AWS PrivateLink
- Connect to Amazon services using AWS PrivateLink in Amazon SageMaker AI
- Use AWS PrivateLink to set up private access to Amazon Bedrock
- Overseeing AI Risk in a Rapidly Changing Landscape
- GENREL03-BP01 Use logic to manage prompt flows and gracefully recover from failure
- GENREL03-BP02 Implement timeout mechanisms on agentic workflows

---

## GENREL03-BP01 Use logic to manage prompt flows and gracefully recover from failure

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by reducing the likelihood of performance degradation logical errors in your prompt flows.

### Implementation guidance

Define expected behavior for generative AI applications before, during, and after prompts. Create layers of abstraction between users and models to facilitate retries, error handling, and graceful failures. For multi-step prompt flows, implement logic statements to check if your prompts contain the expected information. Apply similar logic to verify your model's respond with expected content.

For prompt flows containing data from external sources, implement logic to verify the relevant data from the external source exists. Define a fallback action or default modality in the absence of relevant data. Apply similar reasoning to model responses enriched with embeddings from a vector search engine. Consider applying checks on the model's response to identify the relevance of the returned data or a fallback action if no data is returned at all.

Agentic workflows commonly make calls to external systems. Develop agents with error handling in mind. Consider how errors are propagated back up to agents. Upon receiving an error, an agent should take appropriate action to retry or gracefully fail. One way to accomplish this is to have the agent classify responses from external systems as actionable or not. Actionable responses are anticipated and well-understood responses (for example, a database query returning at least one result). An inactionable response traditionally requires error handling at the software layer (for example, error codes or empty responses). Agents can be prompted to classify responses in these cases and take action appropriately. This method may serve to reduce non-determinism and increase reliability of agent workflows.

When developing multistep prompt flows or prompt chains, consider using Amazon Bedrock Flows to orchestrate multistep prompts. Bedrock Flows enables graceful failure and recovery for long prompt chains, which allows your applications to take appropriate action on failure. Bedrock Flows has nodes for controlling flow logic, which include iterator nodes and condition nodes. Customers may consider using these nodes to implement graceful recovery instead of developing a custom abstraction layer.

### Implementation steps

1. Establish error classification system:
   - Categorize common failure types
   - Define severity levels
   - Create response templates for each error category
   - Set up automated detection mechanisms
2. Implement recovery mechanisms:
   - Design retries strategies with exponential backoff
   - Create fallback prompt templates
   - Develop circuit breaker implementations
   - Set up automated recovery workflows
3. Configure monitoring and alerting:
   - Track recovery success rates
   - Monitor remediation effectiveness
   - Set up alerts for repeated failures
   - Implement performance tracking
4. Create continuous improvement process:
   - Analyze failure patterns
   - Update remediation strategies
   - Refine prompt templates
   - Optimize recovery workflows

### Further reading

- Demo - Amazon Bedrock Flows
- Build an end-to-end generative AI workflow with Amazon Bedrock Flows
- Amazon Bedrock Flows is now generally available with enhanced safety and traceability
- Simplifying the Prompts Lifecycle with Prompt Management and Prompt Flows for Amazon

---

## GENREL03-BP02 Implement timeout mechanisms on agentic workflows

**Risk if not established:** High

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by freeing resources that might have been consumed by unexpected long-running execution loops.

### Implementation guidance

Agentic workflows act on behalf of a user by making calls to external systems. External systems may themselves perform several time-consuming tasks which the agent is not aware of, resulting in idle agents that could run for an extended period. To maintain a reliable agentic system, implement controls to manage agentic timeout.

One approach to controlling agentic runtime or lifecycle is to implement runtime timeouts on the external infrastructure. For example, if an agent makes a call to a function through an Action Group, consider applying a timeout to the corresponding function. The timeout should be set to include the maximum allowable time needed to complete a process, accounting for additional latency for edge cases such as cold starts. You may consider rounding this value up to avoid unnecessary early terminations.

Alternatively, consider connecting agentic workflows to an event system, developing an asynchronous process management architecture. Introducing an asynchronous event system gives users the most flexibility and visibility into agent process lifecycle or flow. By requiring the compute underpinning an Action Group to publish events, workload owners maintain insight into

where an agent may encounter stalled flow or process. Consider using events to publish agent updates and act appropriately to stop long-running invocations.

Error handling at the agent layer should be transparent to users. When errors occur, communicate clear details about the issue while maintaining system security by avoiding exposure of sensitive internal information. The response should outline specific next steps so that users can complete their tasks independently if the agent remains unavailable. This approach promotes operational resilience while maintaining security best practices, as users receive actionable guidance without compromising system integrity.

### Implementation steps

1. Create an agent workflow configuration:
   - Define maximum runtime thresholds
   - Set up timeout controls at function and workflow levels
   - Configure event publishing for process monitoring
2. Implement timeout mechanisms:
   - Add timeouts at the agent layer to terminate sessions waiting for user input
   - Configure timeouts on external compute resources
   - Set up dead letter queues for timed-out processes
3. Establish monitoring and alerting:
   - Track agent execution times
   - Monitor timeout frequency
   - Alert on repeated timeouts
4. Define recovery procedures:
   - Create graceful termination processes
   - Implement cleanup routines for timed-out sessions
   - Set up automated retry mechanisms where appropriate

### Further reading

- AWS re:Invent 2023 - Simplify generative AI app development with Agents for Amazon Bedrock
- Automate tasks in your application using AI agents
- Best practices for building robust generative AI applications with Amazon Bedrock Agents - Part
- Best practices for building robust generative AI applications with Amazon Bedrock Agents - Part
- GENREL04-BP01 Implement a prompt catalog
- GENREL04-BP02 Implement a model catalog

---

## GENREL04-BP01 Implement a prompt catalog

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by creating a central store for prompts that can be used for generative AI workloads.

### Implementation guidance

Prompt catalogs function as a centralized system for developing, testing, and managing prompts. Implement a prompt catalog to maintain different versions of prompts. Prompts should be released to a live version once passing the appropriate testing thresholds and benchmarks. In the case where a prompt results in unexpected or undesirable behavior, a prompt catalog enables the ability to roll back to the previous version.

Additionally, maintain versioned information on hyperparameter ranges for prompts. Prompt behavior can change drastically when tuning hyperparameters such as temperature, top_p, or top_k. Value ranges for these hyperparameters should be paired with and validated against prompt versions as part of the prompt engineering process.

Prompt catalogs should maintain test results for a prompt against several model versions. A given foundation model can have several versions, and prompt test results for each model version can vary accordingly. Consider developing a catalog that maintains prompt versions for each of the available models.

### Implementation steps

1. Design catalog structure:
   - Define prompt metadata schema (like version, author, and purpose)
   - Create categorization system for different prompt types
   - Establish naming conventions and tagging standards
   - Define access control requirements
2. Implement version control:
   - Set up version tracking for prompts
   - Create changelog management process
   - Define rollback procedures
   - Establish backup and recovery processes
3. Create testing framework:
   - Define success criteria for prompts
   - Establish validation procedures
   - Create test suites for different use cases
   - Set up automated testing pipelines
4. Configure prompt metadata:
   - Document hyperparameter ranges
   - Track performance metrics
   - Record model compatibility
   - Maintain usage statistics
5. Establish governance processes:
   - Define approval workflows
   - Create audit trails
   - Set up review procedures
   - Implement quality controls
   - Codify in your organizations AI usage or policy document

### Further reading

- AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on Amazon Bedrock (AIM377)
- Amazon Bedrock Prompt Management is now Available in GA

---

## GENREL04-BP02 Implement a model catalog

**Risk if not established:** Low

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by helping to make sure the deployed model is the appropriate model for the given use case.

### Implementation guidance

Model catalogs provide a centralized location to review models, model versions, and model cards. Traditionally, model catalogs are meant to store model artifacts developed by customers. Foundation models are rarely developed from scratch, and as a result, foundation model catalogs should maintain first-party models, third-party models, and custom models developed from third- party models.

Consider implementing a model catalog for foundation models that records and tracks model access, model versions, and model card information. Maintain a model catalog in your environment to track available models. Model catalogs should provide a central location for model management, particularly if there is a need to roll back to a particular model or model version.

AI policy documents should provide clear details regarding the usage, maintenance, and updating of the model catalog. The AI policy document is intended to be the central authority for operational questions pertaining to AI workloads and supporting infrastructure. Keep this document up to date with the appropriate materials necessary to scale the usage of the model catalog throughout the organization.

### Implementation steps

1. Set up catalog structure:
   - Create model classification system (by type, purpose, and provider)
   - Define model metadata schema
   - Establish versioning conventions
   - Design access control framework
2. Configure model tracking:
   - Record model lineage and dependencies
   - Track model versions and updates
   - Document model customizations
   - Maintain performance benchmarks
3. Implement model cards:
   - Define required model information
   - Document model capabilities and limitations
   - Record training data characteristics
   - Specify intended use cases and constraints
   - Include ethical considerations and biases
4. Establish model governance:
   - Create model approval workflows
   - Define deployment procedures
   - Set up model monitoring
   - Implement security controls
   - Track model usage and access
5. Create maintenance procedures:
   - Define model update process
   - Establish deprecation policies
   - Create archival procedures
   - Set up backup and recovery
6. Implement validation framework:
   - Create model testing procedures
   - Define acceptance criteria
   - Set up performance benchmarking
   - Establish quality gates

### Further reading

- Amazon Bedrock API Reference
- Amazon Bedrock Marketplace
- Find serverless models with the Amazon Bedrock model catalog
- Bring your own endpoint
- Amazon Bedrock Marketplace: Access over 100 foundation models in one place
- GENREL05-BP01 Load-balance inference requests across all regions of availability
- GENREL05-BP02 Replicate embedding data across all regions of availability
- GENREL05-BP03 Verify that agent capabilities are available across all regions of availability

---

## GENREL05-BP01 Load-balance inference requests across all regions of availability

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by creating a highly available environment for serving inference requests.

### Implementation guidance

Use load balancing and multi-Region deployment strategies to distribute inference requests across multiple AWS Regions and Availability Zones. This helps maintain consistent performance and availability in the face of regional disruptions or network issues. Consider using Amazon Bedrock's cross-Region inference profiles to route requests to the nearest available endpoint. For self-hosted models on Amazon SageMaker AI, implement a multi-AZ deployment with an Amazon SageMaker AI Inference Endpoint configured for auto-scaling to automatically distribute and scale traffic across Regions.

This strategy provides improved reliability, reduced risk of single points of failure, and better geographic coverage for global users. Potential trade-offs include increased network latency and operational complexity.

### Implementation steps

1. Configure Amazon Bedrock cross-Region inference profiles or deploy self-hosted models on Amazon SageMaker AI Inference Endpoints across multiple Availability Zones.
2. Set up an Amazon SageMaker AI Inference Endpoint with auto-scaling enabled to distribute traffic based on health and latency.
3. Implement health checks and automated failover to maintain availability.
4. Monitor performance metrics like latency, error rates, and throughput across Regions.

### Further reading

- Supported Regions and models for inference profiles
- Getting Started with cross-Region inference in Amazon Bedrock

---

## GENREL05-BP02 Replicate embedding data across all regions of availability

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by validating that models have access to the appropriate data to service inference requests across an entire Region of availability.

### Implementation guidance

Replicate the data required for generative AI workloads, such as embeddings and knowledge bases, and make that data readily available across all designated Regions. This helps prevent data access from becoming a bottleneck and maintains consistent performance for users regardless of their location. Use solutions like Amazon S3 cross-Region replication, Amazon OpenSearch Service cross- cluster replication, and AWS Glue data pipelines to distribute data efficiently.

Consider data sovereignty requirements and regulatory restrictions that may limit your ability to freely replicate data, including embeddings, across all Regions. Carefully review the data residency and compliance needs for your specific use case and workload. Implement data distribution strategies that respect these constraints, such as keeping embeddings within a defined geographic area or using Region-specific data stores.

Replicating data across Regions can incur additional storage and data transfer costs. Optimize data partitioning and compression to minimize the overall storage footprint. Use Amazon S3 Intelligent Tiering to automatically move less frequently accessed data to more cost-effective storage classes. Replicating data provides improved data availability and reduced latency for users. If done properly, this practice helps you maintain compliance with data sovereignty regulations. Trade-offs may include increased costs and potential consistency challenges within the allowed Regions.

### Implementation steps

1. Assess data sovereignty requirements and regulatory constraints for your generative AI workload, including the distribution of embeddings.
2. Identify the Regions where you can freely replicate embeddings and other data based on your compliance needs.
3. Set up cross-Region replication for embedding data stores like Amazon S3 and Amazon OpenSearch Service within the allowed Regions.
4. Implement data ingestion pipelines using AWS Glue to keep the allowed Regions synchronized for embeddings and other data.
5. Configure monitoring and alerting to detect data replication issues and compliance violations.
6. Optimize data partitioning, compression, and storage tiering to minimize the cost of cross- Region data replication.

### Further reading

- Supported Regions and Models for inference profiles
- Ensure availability of your data using cross-cluster replication with Amazon OpenSearch Service

---

## GENREL05-BP03 Verify that agent capabilities are available across all regions of availability

**Risk if not established:** Medium

**Desired outcome:** When implemented, this best practice improves the reliability of your generative AI workload by verifying that agents have access to the appropriate supporting infrastructure such as APIs or functions, so they may service a wider region of availability.

### Implementation guidance

Agents for Amazon Bedrock can be made available across regions, so long as the models and supporting infrastructure exist in the desired regions. Amazon Bedrock Agents make API calls on behalf of a user. Once deployed to a new region, these agents must have access to the same or regionally-equivalent API. Consider deploying your APIs across multiple regions behind a CloudFront distribution with latency-based routing. When possible, leverage Amazon Route 53 with latency-based routing to direct traffic within your VPC (and on the Amazon backbone) rather than taking private traffic public to route to an internal service. If your agent is not making calls to a foundation model using a cross-region inference profile, be sure to configure model access in all required regions.

When using agents in your generative AI architecture, make the supporting infrastructure, such as APIs and functions, available across all Regions where your agents are deployed. This involves replicating the necessary components and configuring appropriate routing mechanisms to maintain consistent agent functionality regardless of user location.

### Implementation steps

1. Deploy supporting agent infrastructure (APIs, functions) in primary and secondary Regions.
2. Implement latency-based routing or similar mechanisms to distribute agent requests.
3. Verify that agents can access the required resources in all Regions.
4. Monitor agent performance and resource utilization across Regions.

### Further reading

- Latency-based routing
- Using latency-based routing with Amazon CloudFront for a multi-Region active-active
- GENREL06-BP01 Design for fault-tolerance for high-performance distributed computation tasks

---

## GENREL06-BP01 Design for fault-tolerance for high-performance distributed computation tasks

**Risk if not established:** High

**Desired outcome:** When implemented, this best practice improves the reliability of your model customization workloads, automating recovery during fine-tuning, pre-training, and other model customization workloads.

### Implementation guidance

Model pre-training, continuous pre-training, fine-tuning, and distillation are some of the many high-performance distributed computation tasks sometimes required to optimize foundation models for generative AI workloads. These tasks require the orchestration of dozens or hundreds of virtual machines, running workloads over days, weeks, months or longer. These tasks are particularly susceptible to disruptions, which could delay or stop training progress. Consider a managed or automated process that provisions and orchestrates the infrastructure on your behalf, handles errors, and preserves the workload's integrity.

Amazon SageMaker AI HyperPod clusters allow customers to pre-train or fine-tune large language models using managed infrastructure. Amazon EC2 UltraClusters facilitate large language model hosting for purpose-built machine learning accelerators. Additionally, Amazon Bedrock offers managed fine-tuning, continuous pre-training, or model distillation for a selection of third-party models.

Amazon SageMaker AI HyperPod, with both Amazon EKS and Slurm orchestration, establishes comprehensive checkpointing mechanisms that automatically save training state at regular intervals to persistent storage like Amazon S3 or FSx for Lustre.

For EKS-based HyperPod, use fault tolerance capabilities by implementing application-level checkpointing in your training scripts, and store checkpoints on shared persistent volumes that survive pod restarts and node failures. Configure Kubernetes health checks and restart policies to automatically detect and recover from failed training pods while preserving progress from the last checkpoint.

For Slurm-based HyperPod, use the auto-resume functionality to provide zero-touch resiliency infrastructure that automatically recovers training jobs from the last saved checkpoint when hardware failures occur. Configure your training jobs to run inside exclusive allocations using salloc or sbatch, and verify that your entrypoint scripts maintain environment consistency across node replacements. Both systems benefit from SageMaker AI HyperPod's built-in cluster health monitoring that continuously checks GPU health with DCGM policies, network connectivity with EFA health checks, and automatically replaces faulty nodes. The multi-head node support in Slurm further enhances fault tolerance by providing backup head nodes that automatically take over if the primary head node fails.

When implementing fault-tolerant distributed training manually, evaluate options that can recover the training and customization progress. Create training job recovery points by checkpointing model training. Keep track of training progress, and determine when to halt training based on observed metrics. Consider leveraging performant storage solutions (like Amazon FSx for Lustre) that provide distributed compute tasks rapid access to large data volumes at scale. Managed training and model customization solutions provide these capabilities, but you can also consider self-hosting for some model training and customization initiatives.

Use managed services and purpose-built infrastructure to handle the complexity and resource requirements of distributed model customization workloads. AWS offers several solutions that can help improve the reliability and efficiency of these tasks:

- Amazon SageMaker AI HyperPod: A managed service that automates the provisioning and orchestration of distributed training infrastructure, including handling node failures, checkpointing, and other fault-tolerance mechanisms. HyperPod is optimized for large language model training and can use specialized hardware like AWS Trainium instances.
- Amazon Bedrock: Provides managed workflows for fine-tuning, continued pre-training, and model distillation, abstracting away the underlying infrastructure management and failure handling.
- AWS Batch: A fully-managed batch processing service that can run distributed computational tasks, including model customization, with automatic scaling, retry logic, and resource optimization.

When implementing fault tolerance manually, focus on strategies like checkpointing, progress tracking, and automated recovery. Use high-performance storage solutions like Amazon FSx for Lustre to provide rapid access to training data. Configure your workflow to handle node failures, spot instance interruptions, and other disruptions gracefully.

Continuously monitor the distributed workloads for performance, resource utilization, and failures. Use Amazon CloudWatch to set alerts and thresholds, and use Amazon EventBridge to run automated remediation actions. Analyze logs and metrics to identify bottlenecks and optimize the distributed architecture over time.

### Implementation steps

1. Evaluate managed services like SageMaker AI HyperPod, Bedrock, and Batch for your model customization needs.
2. If implementing a custom distributed workflow, provision high-performance storage and compute resources.
3. Implement checkpointing, progress tracking, and automated retry mechanisms to handle failures.
4. Configure monitoring, alerting, and automated remediation for the distributed workloads.
5. Continuously analyze performance, costs, and reliability to optimize the distributed architecture.

### Further reading

- Amazon SageMaker AI HyperPod
- Customize your model to improve its performance for your use case
- Resilience-related Kubernetes labels by SageMaker AI HyperPod
- Speed up training on Amazon SageMaker AI using Amazon FSx for Lustre and Amazon EFS file
- Customize models in Amazon Bedrock with your own data using fine-tuning and continued pre-
- Amazon BedrockModel Customization Workshop Notebooks
- Amazon SageMaker AI Hyperpod Recipes
- Introducing Amazon SageMaker AI HyperPod: a purpose-built infrastructure for distributed
- Introducing Amazon SageMaker AI HyperPod, a purpose-built infrastructure for distributed
- Ray jobs on Amazon SageMaker AI HyperPod: scalable and resilient distributed AI

---
