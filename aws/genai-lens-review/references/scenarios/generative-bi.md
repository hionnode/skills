# Generative business intelligence

Reference scenario from the *AWS Well-Architected Framework — Generative AI Lens* (2026).

A key objective for organizations across industries is to enable business users to independently explore and analyze data through natural language interactions, deriving deeper insights from both structured and unstructured sources. Generative business intelligence (BI) uses AI-powered capabilities to transform how users interact with data, moving beyond traditional dashboards and reports to more intuitive, conversational experiences.

Generative BI solutions can combine various data types, including enterprise data warehouses, operational systems, documents, and third-party feeds to provide comprehensive analytics and insights. This approach helps organizations derive value from their data assets while maintaining necessary security and governance controls.

## Scenario characteristics

The following generative BI reference architectures are built around these key principles:

- Minimize operational overhead: Managed services and builder approaches both offer rapid deployment options and customizable solutions to meet diverse organizational needs.
- Natural language interactions: Users can query and analyze data using conversational interfaces.
- Comprehensive data access: Unify access to structured and unstructured data sources across the organization.
- Security and governance: Maintain strong access controls and audit capabilities throughout the solution.
- Scalability and performance: Provide responsive user experiences and support for concurrent usage at scale.

## Reference architecture

Managed services approach

1. Users are authenticated through AWS IAM Identity Center, integrating with an existing identity provider or using IAM Identity Center as a standalone identity provider.
2. Amazon Q Business indexes unstructured data from configured AWS and third party data sources, including access control lists where applicable.
3. Amazon Q in QuickSight is configured to retrieve data from AWS and third party data sources, using row level security and column level security definitions for granular access control.

Quick Q topics are created from these datasets for performant and accurate natural language querying.

4. Users explore and analyze data through natural language through the Amazon Q Business or Amazon Q in QuickSight web applications after logging into the identity provider configured in AWS IAM Identity Center. Amazon Q Business provides a conversation-first interface for tasks that anchor on surfacing insights from unstructured documents, while Amazon Q in QuickSight provides a visualization interface for tasks that anchor on surfacing insights from aggregate data analysis. Both interfaces may use insights surfaced from each other to augment.
5. Indexing, performance, and user interaction monitoring data are collected in Amazon CloudWatch for comprehensive metrics, logging, and alerting.

Embedding in custom applications approach

1. Unstructured data sources within AWS, such as Amazon S3, and third-party sources, such as Microsoft SharePoint, are connected and synced with an Amazon Bedrock Knowledge Base, providing natural language querying and response generation from unstructured data.
2. A central query engine is set up with Amazon Redshift by using an existing cluster, creating a new cluster, or creating an Amazon Redshift Serverless data warehouse.
3. Additional data sources may be connected using AWS Glue Data Catalog, integrated with the Amazon Redshift query engine.
4. Structured data sources configured in the Amazon Redshift query engine are connected and synced with an Amazon Bedrock Knowledge Base, providing natural language querying and response generation from structured data. Additional table metadata may be provided to improve query performance.
5. An Amazon Bedrock Agent with the applicable Knowledge Bases connected provides multi-turn natural language querying and insights across data sources.
6. Users interact with the custom application, which invokes the Amazon Bedrock Agent or Amazon Bedrock Knowledge Bases directly to analyze data and surface insights with natural language.
7. Indexing, performance, and user interaction monitoring data are collected in Amazon CloudWatch for comprehensive metrics, logging, and alerting.

Note The custom application is responsible for authenticating users and providing appropriate data access. This may be accomplished by using metadata filters on Amazon Bedrock Knowledge Bases and verifying that structured data sources are only accessed by authorized users or are otherwise using queries that protect data privacy.
