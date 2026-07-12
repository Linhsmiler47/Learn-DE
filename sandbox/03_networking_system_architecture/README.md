# Phase 03 — Networking and System Architecture

## Learning Objectives

- Understand client-server architecture and how OS processes/services communicate.
- Understand IP, ports, DNS, HTTP/HTTPS, TCP fundamentals, and REST APIs.
- Understand reverse proxies, load balancers, caching, and message queues at a conceptual level.
- Understand distributed systems basics: HA, scalability, fault tolerance, batch vs event-driven.

## Prerequisites

- Phase 01 — Linux basics
- Phase 02 — Git basics (for tracking your notes/diagrams)

## Reference Materials (`ref roadmap/`, read-only)

- [HTTP and HTTPS: how the protocol works](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/KIẾN%20THỨC%20CƠ%20BẢN/LESSON%202%20-%20HTTP%20và%20HTTPS%20là%20gì%20-%20Cách%20hoạt%20động%20của%20giao%20thức%20này.docx)
- [What is a REST API](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/KIẾN%20THỨC%20CƠ%20BẢN/LESSON%202%20-%20KIẾN%20THỨC%20CƠ%20BẢN%20-%20REST%20API%20Là%20gì.docx)

> The reference material only covers HTTP/REST at a surface level — the rest of this phase (DNS, TCP, load balancers, HA/fault tolerance, distributed systems fundamentals) has no source material and is built from external references.

## Core Concepts

- Client-server model, ports, IP addressing, DNS resolution
- TCP fundamentals (handshake, reliability guarantees) vs UDP
- HTTP/HTTPS, REST API design
- Reverse proxies, load balancers, application vs database servers
- Caching, message queues, batch vs event-driven processing
- High availability, scalability, fault tolerance — what each actually means operationally

## Exercises

- Diagram a request's full path from browser to database and back, labeling every hop.
- Use `curl`/`dig`/`traceroute` to trace an actual HTTP request and DNS resolution.
- Stand up a local reverse proxy (nginx) in front of a toy web server and observe headers change.
- Write a one-page explanation of when you'd choose a message queue over a direct API call.

## Expected Output

- An architecture diagram (in `architecture/` style) of a generic 3-tier web app.
- Notes distinguishing batch, streaming, and event-driven processing with a real example of each.

## Validation Checklist

- [ ] You can explain, without notes, what happens between typing a URL and a page rendering.
- [ ] You can articulate the difference between horizontal and vertical scaling and when each applies.

## Common Mistakes

- Treating 'high availability' and 'scalability' as the same concept — they solve different problems.
- Assuming REST and HTTP are the same thing.

## Optional Challenges

- Set up a local load balancer (nginx or HAProxy) round-robining two instances of a toy app.

## Reflection Questions

- Where in this stack would a Data Engineering pipeline actually sit?
