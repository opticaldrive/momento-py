# momento-py
A screenshot service API.
tl;dr you give us url we give you screenshot.
(appreciated if you hack us or not)

Stage: Bastion development

Terminology/Setup:
Items with "*", naming WIP. Actually everything naming WIP
Server
- Delegates screenshot tasks to Nodes over a http api or something
- tl;dr fancy load balancer?
- API
- DB
- Users
- User Facing
 
Nodes
- Runs playwright in a nested container and a simple api with auth for the server to call. 
- Has API middleman of server and playwright websockets thing
- Podman nested containers
- Bastion
-- Surrounding container, contains containers with playwright image
-- Contains API that the Server calls.
-- Playwright image(Name Very WIP)
--- Must be as hardened as possible as a priority.
--- Bastion connects over websockets. 
