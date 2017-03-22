Contributers:
Solomon Mori
Yiyang Li

# Bouncer
*You don't belong here*

Bouncer is a host-based intrusion detection system designed to monitor information sent between pages of a Web application and identifies if the information constitutes an attack or not; the attack is identified if it is determined that it does not belong to the grammar learned for the specified context. This is done by loading the grammar and query into Prolog to see if the query can be built with the grammar. The grammar is learned by applying grammar induction to a repository of server logs that show the normal use case grammar in the specific context. Context here refers to a specific origin URL and a specific destination URL. 


Requirements
============



