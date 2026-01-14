##### Table of Contents  
[1. Data Space Introduction](#1-data-space-introduction)</br>
  [1.1 IDSA protocol core components](##11-idsa-protocol-core-components)</br>
  [1.2 IDSA protocol core goals](#12-idsa-protocol-core-goals)</br>
  [1.3 IDSA key features and principles](#13-idsa-key-features-and-principles)</br>
[2. Data Space within Crete Valley](#2-data-space-within-crete-valley)</br>
   [2.1 Crete Valley Middleware (IDSA Control Plane)](#21-crete-valley-middleware-idsa-control-plane)</br>
   [2.2 Crete Valley Connector (IDSA Data Plane)](#22-crete-valley-connector-idsa-data-plane)</br>
[3. Deployment and Configuration of the Crete Valley Connector Guide](#3-deployment-and-configuration-of-the-crete-valley-connector-guide)</br>
   [3.1 Prerequisites](#31-prerequisites)</br>
   [3.2 Deployment of the Crete Valley Connector](#32-deployment-of-the-crete-valley-connector)</br>
   [3.3 Configuration of the Connector](#33-configuration-of-the-connector)</br>
[4. API libraries](#4-api-libraries)</br>
   [4.1 User Login & Authorization](#41-user-login--authorization)</br>
   [4.2 My Data Offerings List](#42-my-data-offerings-list)</br>
   [4.3 Provide Data](#43-provide-data)</br>
   [4.4 Consume Data](#44-consume-data)</br>


# 1. Data Space Introduction

<p align="justify">A data space is a federated, decentralized infrastructure that allows organizations to share data securely and govern its usage according to mutually agreed-upon rules. </p>

<p align="justify">A European data space is an EU-wide initiative to create a secure, interoperable ecosystem for sharing data across different European projects and sectors.
These spaces are designed to allow businesses, organizations, and citizens to share and access data in a way that respects privacy, security, and European laws, while enabling innovation and cross-sector collaboration. 
The goal is to create a trusted, common market/ network for data where organizations retain control over their own data. </p>

The IDSA initiative introduces the Data Space Protocol that defines the concept, structure, components the principles that should characterize European Data spaces : [IDSA documentation](https://internationaldataspaces.org/) 

</br>




## 1.1 IDSA protocol core components
<p align="justify">The Data Space structure omprises of two main components: Control Plane and Data Plane, each playing a crucial role in data management and
exchange </p>
<p align="justify">

- <b>Control Plane</b>: Ensures data access and sovereignty management and interoperability at the dataspace level. Its core functionalities are:
  - Cataloguing: To display available data and associated services.
  - Contract Negotiation: Allows data providers to set or negotiate terms of data usage.
  - Data plane configuration and coordination.
  
- <p align="justify"><b>Data Plane</b>: Handles the actual data transfer, implementing various communication protocols like HTTP, to suit specific use cases. This plane manages the practical aspects of data transfer once policies are negotiated.</p>

</br>

## 1.2 IDSA protocol core goals

The list of business goals, concepts and technologies that are involved within the IDSA Data Space
are the:
- Data driven Business ecosystems,
- Data sovereignty as a key capability,
- Data as an economicgood,
- Data exchange and data sharing,
- Meaningful data,
- Industrial Cloud Platforms,
- Big data an AI,
- IoT and industrial IoT,
- Blockchain,
- Federated frameworks for data sharing agreements and terms of use,
- General Data Protection Regulation and
- the Data Economy and Privacy in the connected world.
</br>

## 1.3 IDSA key features and principles

The list of key features and principles of a common European data space, are: 
- Trust
- Security & Data Sovereignty
- Ecosystem of Data
- Standardised Interoperability
- Value-Adding Apps
- Data Markets

<b>Following the Data Space Protocol it is possible to deploy private Data Spaces that can be used for private or public projects such as Crete Valley</b>

</br>
</br>

# 2. Data Space within Crete Valley

<p align="justify">Crete Valley Data Space aims to create a secure and privacy-preserving infrastructure to pool, access, share, process and use data. 
The Crete Valley Data Space is a clear and practical structure for access to and use of data in a fair, transparent, proportionate 
and/non-discriminatory manner and clear and trustworthy data governance mechanisms as they are defined by European rules and values. 
Data holders/providers have the capability, in the data space, to grant access to or to share certain personal or non-personal data under their control and restrictions. 
Data consumers have the capability, to participate, search, discover and request access to the available data. </p>

<p align="justify">The participants of the Crete Valley Data Space can participate both as Data providers and Data consumers. 
Additionally the data access policy and rules within Crete Valley Data Space are implemented through a traditional Subscription system routine that includes the Data exchange Subscription request from the Data Consumer and the Data exchange Subscription response from the Daata Provider. </p>

<b>The Core components that compose the Crete Valley Data Space ecosystem is the Middleware and the Connector. </b>

</br>

## 2.1 Crete Valley Middleware (IDSA Control Plane)

The Crete Valley Middleware is a central Graphical User Interface that operates as the Control Plane component that aims to configures and coordinates the Data Space organizations and Connectors and set the ground rules of the Data Access control and restrictions. The core functionalities of the Crete Valley Middleware are the following:

1.	Configuration (Onboarding) 
2.	Creation of Data Offering (Indexing)
    - Enable Data Offering Interopearbility (Semantic and technical Interopeability)
    - Enable Data Offering Access control (Specific Restrictions and rules)
5.	Data Offering Catalogue (Discovery)
6.	Subscription and access management (Negotiation)
7.	Provisioning and Consuming Data (Data Exchange)

<br/>

Some important definitions about the Crete Valley Middleware are:

<p align="justify"> <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/63fb679b-1412-4989-9a79-89b2b8b85354" /><b>   Data Offering Service type</b>: Is a predefined contextual frame that characterizises every data exchange (Data Provision & Consumption) within Crete Valley Middleware. Every Data Offering service type is followed by three attributes (Generic Category > Sub-category > Specific Business Object) that construct a defined «Topic» that describes the content of the data that will be exchanged.</p>

<p align="justify"><img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/63fb679b-1412-4989-9a79-89b2b8b85354" /><b>   Data Offering Service</b> : Is the initial entity that is created by a Data Provider, that defines the Content of the Data that will be shared among the Subscribed (to the Data OFfering) Users. The user selects a Data Offering Service Type among the defined Data Offering Service Type Catalogue that is presented on the Middleware. Every Data Provision is under an «umbrella» of a specific Data Offering service.</p>

<p align="justify"><img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/63fb679b-1412-4989-9a79-89b2b8b85354" /><b>   Subscription</b> : Is an agreement between a Data Provider and one or more Data Consumers regarding a Data Offering Service. A subscription is performed following the sequential steps: </br> </p>

1. Data Offering Service Discovery by Data Consumer
2. Subscription Request
3. Request Response by the Data Provider
4. Upon accepting the Subscription is enabled 
  

<p align="justify"><img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/63fb679b-1412-4989-9a79-89b2b8b85354" /><b>   Data Entity</b> : Is every Data file (assigned in the «umbrella» of a Data Offering Service) that is shared by the Data provider with the Subscribed users of this specific Data offering service</p>

<p align="justify"><img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/63fb679b-1412-4989-9a79-89b2b8b85354" /><b>   API libraries</b> : Are API tools/Commands the can be used as an alternative for the actions that can be performed within the Crete Valley Middleware. These can be used for the programmatical exploitation of and integration with the Crete Valley Middleware with an external application. These actions include, the Data Offering Service Discovery (Data Offering Service Catalogue list), Data Offering Service Subscription requests, Data Provision & Consumption etc. </p> 

<br/>

<p align="justify">
<img width="22" height="22" alt="image" src="https://github.com/user-attachments/assets/637a0907-246e-4300-be84-1d6136feb794" /><b>   The creation & activation of a user account for the Crete Valley Middleware is processed upon the request to European Dynamics</b> (please contact dimitrios.apostolidis@eurodyn.com)

<img width="22" height="22" alt="image" src="https://github.com/user-attachments/assets/637a0907-246e-4300-be84-1d6136feb794" /><b>   The creation of a new Data offering Service type or the attributes that compose that (Category, Sub-Category, Business Object), that serve a specific use case and is missing from the Crete Valley Middleware, is processed upon the request to European Dynamics</b> (please contact dimitrios.apostolidis@eurodyn.com)
</p>

The Crete Valley Middleware can be found in: [Crete Valley Middleware](https://crete-valley.eurodyn.com/)

</br>

## 2.2 Crete Valley Connector (IDSA Data Plane)

<p align="justify">The Connector is a complex structure composed of several key elements, including one or more
physical or virtual machines and the Connector Services layered on top of it. 
The Connector is the core component of the Crete Valley Data Space for implementing the concept of Data Space. It serves as the gateway for secure connecting participants and the secure exchange of raw/actual data within the Data Space ecosystem. 
A key benefit of this approach is the decentralization that enables data sovereignty—ensuring organizations retain full control over how their data is accessed and used. 

<b>Simply, Crete Valley Connector a dockerized piece of software that operates as a node the enables the distributed data exchange within the Data Space on behalf of a user. This dockerized software can be deployed locally in a server from any user that wants to connect to the Crete Valley Data Space ecosystem. </b>

The Deployment and the Configuration of the Crete Valley Connector is described in the process below:
</p>

</br>
</br>






# 3. Deployment and Configuration of the Crete Valley Connector Guide

## 3.1 Prerequisites 

The hardware and operating system prerequisites are:

- A 2-core processor
- 4GB RAM Memory
- 50GB of disk space or more

The software prerequisites include:

- Centos 7 or Windows Server Operative System (OS);
- Docker and docker-compose

Crete Valley Connector software and its components will be delivered utilizing the Docker containers of the folder <code style="color : #FF0000">"Crete Valley Connector Docker Files"</code> of this repository. </br>

<img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/637a0907-246e-4300-be84-1d6136feb794" />   Additionally to those folders and file within the <code style="color : #FF0000">"Crete Valley Connector Docker Files"</code> you need to contact and request the mandatory <code style="color : #FF0000">.env</code> file from the European Dynamics. 

</br>

## 3.2 Deployment of the Crete Valley Connector

<img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/637a0907-246e-4300-be84-1d6136feb794" />   For the scope of the following instructions, we suppose you built a server that runs under the local <code style="color : #FF0000">http://my-local-server</code> and your public domain under <code style="color : #FF0000">https://my-public-domain.com</code> .

</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/ceb41791-d6b1-4f1c-ba2f-eff7f5320d8f" /> You need to upload the appropriate files ("Crete Valley Connector Docker Files" & .env) either directly through <b>Filezilla</b> or through the <b>Command Prompt</b>. 
You can directly upload the folders&files or clone the folders&files of "Crete Valley Connector Docker Files":

```
cd /crete-valley-connector/
git clone https://github.com/Crete-Valley/Crete_Valley_Data_Space_Connector_Deployment_and_Configuration_Guide.git
cd /crete-valley-connector/Crete Valley Connector Docker Files
```

<img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/637a0907-246e-4300-be84-1d6136feb794" />   In this stage you need to make sure to put the <code style="color : #FF0000">.env</code> file (from the European Dynamics) in that folder. 

</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/98bfc605-56a2-49a4-9948-f37e490b7a59" />   You need to connect in your local server through the <b>Command Prompt</b>, install Docker (the Docker application has to be downloaded and installed accordingly to the OS of the server to host the deployment) and the needed libraries as shown below:

For the needed Libraries

```
$ sudo yum update
$ sudo yum install ca-certificates
$ sudo yum install curl
$ sudo yum install -y yum-utils
```

For the Docker

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg

$ sudo yum-config-manager \
  --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo

$ sudo yum install docker-ce docker-ce-cli containerd.io
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

Maybe you will need to login to a docker account

```
$ sudo docker login
$ sudo docker compose up -d
```

</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/4561eec8-c259-4404-8e81-4c2dbecf6707" /> Completing this step you are an inactive part of the Crete Valley Data Space. In order to be an active part of the Data space that can exchange data with the other users, you should define the appropriate ports of the Connector and register them through the Middleware to the Data Space. 

The next steps are responsible to configure the deployed Connector, in a way that will be able to communicate with the rest Connectors and will be integrated in the Crete Valley Middleware.

</br>

## 3.3 Configuration of the Connector

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/488642d8-bfea-4559-ab01-982a1881d45d" /> This step aims to open the appropriate ports in order to make the connector able to reach and be reached by the other connectors in order to share data. Specifically you need to define and expose (make https:// some of them) following URLs:

</br>

* <b>Local API:</b>

Local API Must Be Publicly Exposed In A Static Ip Via Https, before saved on the connection settings. This happens because Data App is served as an endpoint for peer to peer file transfer between you and other Crete Valley users. For the Local API URL, you should expose port <code style="color : #FF0000">:30001</code> of the local server to an https domain. For example, I would expose it as below:

<code style="color : #FF0000">https://crete-valley-localapi.my-public-domain.com</code> ➡️ <code style="color : #FF0000">http://my-local-server.com:30001
</code>

It is very important to expose this port to an https domain, using your F5 configuration or a reverse proxy.

</br>

* <b>ECC URL:</b>

Ecc Url Must Be Publicly Exposed In A Static Ip Via Https, before saved on the connection settings. This happens because Ecc Url is served as an endpoint for peer to peer file transfer between you and other Crete Valley users. For the ECC URL, you should expose port <code style="color : #FF0000">:8889</code> of the local server to an https domain. For example you can expose it as below:

<code style="color : #FF0000">https://crete-valley-ecc.my-public-domain.com</code>  ➡️ <code style="color : #FF0000">http://my-local-server.com:8889</code>

It is very important to expose this port to an https domain, using your F5 configuration or a reverse proxy. 

</br>

* <b>Broker Url:</b>

You do not need to expose this. You just need to use on the Middleware UI, this local URL:  <code style="color : #FF0000">http://my-local-server.com:1026</code>

</br>

* <b>Data APP:</b>

You do not need to expose this. You just need to use on the Middleware UI, this local URL:  <code style="color : #FF0000">https://be-dataapp-provider:8083</code>

</br>
</br>

Please ensure that:

1. Each URL is correctly mapped through your F5 or reverse proxy.
2. Regarding the URLs that need to be exposed, you can use NGINX. If this does not work please make a question to your IT responsible for networks.
3. All public URLs use HTTPS for secure external access.
4. The local ports (8889, 1026, 30001) are exposed from your Docker containers and reachable by the proxy.
5. DNS entries for your public domains are properly configured to route traffic to your exposed endpoints.

If you use any different domain naming conventions or internal network structures, simply maintain the same logical mapping between your local URLs and public URLs.

</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/0f593396-f1d0-463e-b570-7a991a55af61" /> In this stage you should request from ED the creation of users and the provision of the corresponding credentials.

</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/9e3b8c52-916d-49f7-aaa3-185665120868" /> After that you need to Log In to the Middleware and we recommend you to navigate to its functionality.

<img width="859" height="458" alt="Crete Valley Login" src="https://github.com/user-attachments/assets/76343f3e-ce66-4f35-addf-629d40249865" />

</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/81547cb2-3aea-48d5-83a2-15affd6fc9e8" /> The final step of the configuration if to set the Connector settings within the Crete Valley Middleware's "Connector Settings" page, in order to be configured within the Data space as shown below:

</br>

* Local API   : You need to use on the Middleware UI, this URL : https://crete-valley-localapi.my-public-domain.com/api
* ECC URL     : You need to use on the Middleware UI, this URL : https://crete-valley-ecc.my-public-domain.com/data
* Broker URL  : You just need to use on the Middleware UI, this local URL:  http://my-local-server.com:1026
* Data APP    : You just need to use on the Middleware UI, this local URL:  https://be-dataapp-provider:8083

<img width="959" height="693" alt="Crete Valley Connector settings" src="https://github.com/user-attachments/assets/1c2a5c3d-3b2f-4d6c-86e9-a36a5c6c7d87" />


</br>
</br>
</br>

# 4. API libraries

<p align="justify">The API tools/Commands can be used as an alternative for the actions that can be performed within the Crete Valley Middleware. These can be used for the programmatical exploitation of and integration with the Crete Valley Middleware with an external application. </p>

The user can have access in the API tools through the URL:

<code style="color : #FF0000">http://my-local-server.com</code> <code style="color : #FF0000">:30001/api/swagger-ui/index.html?configUrl=/api/v3/api-docs/swagger-config#/</code>
  
<p align="justify">The functionalities that can be executed through the API libraries include, the user Log In & Authorization, the owned Data Offering List, Data Provision & Data Consumption, as shown in the following image. Some extra functionalities are he Data Offering Service Discovery (Data Offering Service Catalogue list), Data Offering Service Subscription requests and Data Offering Service Subscription responses.</p>

</br>
</br>
<img width="1901" height="1145" alt="Swagger finished" src="https://github.com/user-attachments/assets/7bb13e02-a27c-44ed-b19b-13adb65be814" />

</br>
</br>

## 4.1 User Login & Authorization
<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/e48c87da-9ab3-4fce-8ebb-e038ba1bf409" />    In this stage the user posts its credentials and the system returns back an Authorization token.

</br>

<img width="1361" height="610" alt="Swagger user login" src="https://github.com/user-attachments/assets/32289ee4-a6bc-4262-9477-81e7a378dee5" />

</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/a60d2553-669a-4737-bbec-c9ca73b69bca" />    The user copies the Token within the "Access token" field.

</br>

<img width="1577" height="613" alt="Swagger user token" src="https://github.com/user-attachments/assets/5e9ac58b-0dbf-4f92-883b-e8782c0a459a" />

</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/b8676bce-688b-418f-86ad-14f714e19ca8" />
and proceeds to the Authorization, inserting the Authorization Token as shown below:

</br>
</br>

<img width="1367" height="667" alt="Swagger user token insertion" src="https://github.com/user-attachments/assets/e6a8bf65-a067-44a9-94bd-9fd128a7a8eb" />

</br>
</br>

## 4.2 My Data Offerings List 

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/13bda268-b86f-49bc-bbf5-0ec13952c18f" />    The user can retrieve the list of the Data Offerings services that have created through the corresponding API. The user should click the "Execute" button in order to retrieve the Data Offering list:

</br>

<img width="1360" height="726" alt="Swagger offered services" src="https://github.com/user-attachments/assets/49a5c098-0e74-4858-a15b-819f5d938808" />

</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/a60d2553-669a-4737-bbec-c9ca73b69bca" />    The user can use the ID of a Data Offering service in order to Provide Data to all the Subsribed users to it.

</br>
</br>

## 4.3 Provide Data

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/a56b5d31-3324-463f-bb35-452c8986f8d9" />   In order to provide data the user should have the ID of its Data Offering that desires to post data about. This can be done or through its Data Offering list from the API calls either through the Middleware UI as shown below:

</br>

<img width="1918" height="863" alt="Data offering ID" src="https://github.com/user-attachments/assets/84ef803a-67f0-405b-aafe-b971dcc41010" />


</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/a60d2553-669a-4737-bbec-c9ca73b69bca" />  Since the user has the desired ID, needs to set the parameters of the API, filling the following fields, namely:

* "title" : The title of the Data Entity that will be provided.
* "description" : The description of the Data Entity content.
* "filename" : The name of the Data Entity file.
* "file" : The content of the Data Entity file.
* "data_offering_id" : The ID of the related Data Offering service.

</br>

<img width="1352" height="612" alt="Swagger provide daata" src="https://github.com/user-attachments/assets/0282081a-7d4f-45e4-8091-bec089c31ebf" />


</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/b8676bce-688b-418f-86ad-14f714e19ca8" />    Since all the parameters are correct, the user should click the "Execute" button to share the data.

</br>
</br>

## 4.4 Consume Data

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/f9995fb4-ae88-44d1-9f5c-76f38d55b87a" />    In order to consume data, the user should identify the ID of the desired Data Entity that wants to consume. This can be done or by retrieving the list of the Data Entities that can be consumed either by navigating the "Consume Data" page and select the desired Data Entity through the Middleware:

</br>

The "Consume Data" page containing all the Data Entities that the user have received from the Data Offerings that has subscibed to:

</br>

<img width="1905" height="867" alt="Swagger cosnsume data" src="https://github.com/user-attachments/assets/e4108549-5bd7-45f6-86f2-a02653c3d637" />


</br>

The specific Data Entity that user wants to consume, and contains the ID of the Data Entity that will be used to the following API call:

</br>

<img width="1905" height="867" alt="Swagger data entity" src="https://github.com/user-attachments/assets/0211f9e7-2ebc-4722-aac9-c609afcee127" />

</br>
</br>

<img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/a60d2553-669a-4737-bbec-c9ca73b69bca" />    Having the Data Entity ID the user should, click the "Try it out" button, then  fill the "id" field and finally click the button "Execute" in order to retrieve the Data Entity file

</br>
</br>

<img width="1353" height="297" alt="Swagger cosnsume data by id" src="https://github.com/user-attachments/assets/7421cbb2-adee-4b02-8dd0-6a63de52976a" />

</br>
</br>

The response of that API contains the content and metadata of the retrieved Data Entity file.




