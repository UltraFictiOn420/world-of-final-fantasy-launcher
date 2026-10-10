# Changelog

## v1.0.0 - 2026-10-10

- Publish the standard-user launch workaround as inspectable batch source.
- Use the game directory as the working directory.
- Apply `RunAsInvoker WIN7RTM` only to the launcher's process environment.
- Remove the prototype's `/wait` and success-path `pause`; the command window
  closes immediately after requesting game startup.
- Keep clear messages for missing files, Steam, elevated callers, and existing
  game instances. Never stop a running game.
- Supply the Steam App ID as optional plain text; never overwrite game files.
- Add installation, security, test-status, troubleshooting, and removal documents.

Startup success was reported for the original launch method on one PC. The final
non-waiting build's actual gameplay and save behavior remain unverified.
