## About the connector
Web scraping is data scraping used for extracting data from websites. This connector facilitates automated operations related to extracting data from websites.
<p>This document provides information about the Web Scraper Connector, which facilitates automated interactions, with a Web Scraper server using FortiSOAR&trade; playbooks. Add the Web Scraper Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Web Scraper.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet CSE

Contributors: Naili Mahdi

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-web-scraper</pre>

## Prerequisites to configuring the connector
There are no prerequisites to configuring this connector.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
None.

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Web Page Source</td><td>Extract the source code of the web page for the given URL</td><td>get_web_page_source <br/></td></tr>
<tr><td>Get Web Page Screenshot</td><td>Takes a screenshot of a web page and creates an attachment in the FortiSOAR Attachment module</td><td>get_screenshot <br/></td></tr>
</tbody></table>

### operation: Get Web Page Source

#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>URL</td><td>Provide the URL of the web page for which you would like to extract a web page source code
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "code_output": {}
}</pre>
### operation: Get Web Page Screenshot
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>URL</td><td>Provide the URL of the web page for which you would like to take a screenshot
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "code_output": {}
}</pre>
