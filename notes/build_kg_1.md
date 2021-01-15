# Notes:
Context: Enterprise  
Source: Relational Database  
Use Case: Business Intelligence  
Target: Answer Business Question

## Data integration
Data integration is the problem of combining data residing at different source, and providing the user with a unified view of this data.

Source schema -- Mapping -->  Ontology / Global schema

Problem:
- Source is too complicated
- Data - Meaning Gap  
  eg. How many orders were placed in May 2020?  
  Will get different number from different department, because order have different meanin
  g to different people


## What is Knowledge Graph
Data Integration + Concepts and Relationships = Linked Data and Metadata encoded in a Graph  -->  Integrate Knowledge + Data at scale


## How to create Knowledge Graph

### People
Data Producer: Data Engineer  
Data Product Manager: Knowledge Scientist  
Data Consumer: Business Analyst / Data Scientist

### Iteration Process
#### Knowledge Capture
1. Analyze as-is process
2. Collect Documentation
3. Develop Knowledge Report
- Output: Knowledge Report
#### Knowledge Implementation
4. Create/Extend Ontology
5. Implement Mapping
6. Create Extract Queries
7. Validate Data
- Output: Enterprise Knowledge Graph
#### Self Service Analytics
8. Build Report
9. Answer Business Question
10. Move to production

### Context of Knowledge Report

#### Concept
- Name
- ID
- Table Name / SQL
#### Attribute
- Name
- Applied to Concept
- Table Name / SQL
- Column Name
- Datatype
- Is NULL possible
- Cardinality
#### Relationship
- Name 
- From Concept
- To Concept
- Table Name / SQL
- Cardinality

### Implement Mapping
R2RML - Standardized mapping language from relational database to RDF graphs

### Create Data / Execute Query
Two options
- Virtualization (NoETL) :  SPARQL -- Mapping (R2RML) --> SQL --> RDBMS
- Materialization (ETL) :  RDBMS -- Mapping (R2RML) --> Graph DB


## Tools
gra.of


# Summary
Knowledge Graph contains lots of information, but where we should get these information, and how to input these information into the Knowledge Graph. This course give answer to these two questions.
- For Enterprise, lots of information are already storing in RDBMS. These are the information we need to extract and put into Knowledge Graph.
- Building Knowledge Graph is not a time one work. We should put information into Knowledge Graph iteratly. Every time we try to make the Knowledge Graph can answer one more business question.
- There are standardized mapping language (R2RML) from relational database to RDF graphs, we can use it to build Knowledge Graph.

