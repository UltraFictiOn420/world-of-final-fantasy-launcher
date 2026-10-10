# Test status

## Confirmed observations

- The original standard-user prototype was used manually by one user on Windows
  11, who reported that WoFF opened without the previous startup crash.
- After that launch, Windows allowed a diagnostic process to open the game with
  query/read/write/operation access and read its executable header successfully.
  The diagnostic made no writes to game memory.
- Local executable inspection found x64 architecture, file version 2.0.0.0, and
  an embedded `asInvoker` manifest. Previously saved compatibility settings
  explicitly selected `RUNASADMIN WIN7RTM`.

## Final v1.0.0 build

The final source retains the prototype's launch directory and compatibility
flags. Its success path removes `/wait` and the post-game pause so it returns
immediately after starting the game. Automated tests cover source constraints,
error checks, duplicate-instance refusal when applicable, and packaging.

No automated test stops or starts a real game. The final launcher itself has not
yet been manually retested through a complete game session.

## Still needs testing

- Final launcher startup on the original PC.
- Loading, saving, extended gameplay, and repeated launches.
- Steam Input/controllers, achievements, overlay, and cloud synchronization.
- Other PCs, Windows versions, installation locations, and MAXIMA DLC behavior.
- Whether this addresses a particular player's crash; an access-violation event
  alone does not establish the cause.

Use a save backup and retain your old launch method. Reports should distinguish
startup success from confirmed gameplay and saving support.
