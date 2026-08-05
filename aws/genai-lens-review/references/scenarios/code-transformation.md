# Code transformation with generative AI

Reference scenario from the *AWS Well-Architected Framework — Generative AI Lens* (2026).

Organizations today face mounting pressure to modernize their legacy applications while maintaining business continuity and maximizing return on investment. With the majority of Fortune 500 companies still running software written over two decades ago and a large volume of enterprise workloads remaining on-premises, the need for efficient, scalable modernization solutions has never been more critical.

AWS Transform has emerged as a revolutionary solution that uses agentic AI to accelerate legacy application modernization multiple times faster than traditional methods while helping with

savings on licensing costs. This scenario provides enterprise IT leaders and solution architects with a comprehensive framework for implementing large-scale modernization initiatives using AWS Transform, aligned with AWS Well-Architected principles and proven enterprise implementation patterns.

## Scenario characteristics

This scenario uses AWS Transform's .NET modernization capability as an example of the overall AWS Transform potential solutions. Organizations typically manage hundreds to thousands of .NET Framework applications across multiple business units, requiring coordinated transformation efforts that can process applications in parallel while maintaining consistency and quality standards, which makes it a good fit for this scenario.

Modernization efforts must also minimize operational disruption and provide zero-downtime transitions, requiring sophisticated deployment strategies and rollback capabilities.

## Architecture and design

The AWS Transform .NET modernization architecture follows a layered approach designed to support enterprise-scale operations while maintaining security, reliability, and performance standards. The entire workflow is created and managed within the customer's AWS Transform service in the AWS Management Console.

The transformation workflow follows a structured five-phase process: 1. Phase 1: Source code ingestion: AWS CodeConnections securely retrieves application source code, configurations, and metadata from enterprise repositories, performing initial validation and integrity checks. 2. Phase 2: AI-Powered analysis: AWS Transform agents analyze .NET Framework versions, project types, dependencies, and architectural patterns while generating comprehensive compatibility reports and transformation recommendations. 3. Phase 3: Automated transformation: Specialized agents perform code conversion, dependency resolution, and build validation in isolated environments, iteratively resolving compilation errors and maintaining functional equivalence. 4. Phase 4: Quality validation: Automated testing frameworks execute unit tests, integration tests, and Linux compatibility validation while generating natural language summaries of transformations. 5. Phase 5: Deployment integration: Transformed applications are committed to new repository branches with comprehensive documentation, deployment artifacts, and CI/CD pipeline configurations.

## Configuration and implementation

The implementation begins with AWS Transform workspace setup requiring proper IAM roles, cross-account access configuration, and AWS CodeConnections integration.

Repository integration configuration involves creating connections to GitHub, GitLab, or BitBucket through AWS CodeConnections, requiring administrator validation and proper IAM role assignment to workspace environments.

Transformation job configuration requires defining project selection criteria, transformation parameters, and quality gates that align with enterprise standards.

Pilot application selection begins with two to three representative applications that demonstrate core transformation patterns while minimizing business risk. Select applications with comprehensive test coverage, clear documentation, and manageable dependency complexity to establish baseline transformation processes.

## Security and compliance

Data protection is achieved through encryption in transit and at rest, with source code and transformation artifacts secured using AWS Key Management Service (KMS) encryption.

The access control framework uses AWS IAM and AWS IAM Identity Center integration to implement role-based access control (RBAC) with principle of least privilege enforcement. Transformation activities are logged and audited through AWS CloudTrail with comprehensive event monitoring and anomaly detection.

Source code security maintains strict separation between source code access and transformation processing through dedicated AWS accounts and network isolation. Transformation environments are network-isolated to stop unauthorized access to proprietary code and intellectual property.

The audit trail is maintained comprehensively, as transformation activities generate audit logs capturing user actions, system events, and decision points throughout the modernization lifecycle.

Transformation workflows integrate with enterprise change management processes through automated approvals, documentation generation, and rollback capabilities. Transformed code includes detailed change documentation explaining modifications and their business impact.

## Validation and testing

Validation and testing occurs both before and after code transformation. The legacy application undergoes a build-and-test step to validate code integrity ahead of transformation. Post transformation, the application once again undergoes one or more build-and-test steps to verify a successful transformation.

## Lessons learned and best practices

Organizations achieve optimal results by prioritizing applications with high business impact and manageable complexity. Beginning with applications that have comprehensive test coverage and clear documentation establishes reliable transformation patterns for more complex scenarios.
