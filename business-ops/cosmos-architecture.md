# Cosmos monitoring platform — architecture

Cosmos is the monitoring platform used by Customer Ops.
The DG agent is a collection of Python/bash.
The GUI is JavaScript (Scott believes React), on an nginx web server, serving data from a PostgreSQL DB.
Code also appears to include PHP, JavaScript, and jQuery.
Pollers/agents run on each DG (and on NUC devices at non-DG gateway sites); they do SNMP walks and pings and send results via API to the Postgres DB on the central server in QTS. DGs only gather and pass back data — no alerting.
Alert logic runs on the central server in QTS.
DB backups and restore-tested copies are in place.
Business logic (thresholds, suppression rules): Scott believes it is in both DB (settings) and server code (checks).
Scott picked up details from conversations with Dan Apa.

**Approx date:** April 2026

**Source:** Charter IRL 2361/2363 thread (attached to "Charter presentation slide deck review"), 2026-04-13
